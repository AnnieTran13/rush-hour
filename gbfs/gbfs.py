from queue import PriorityQueue
import copy
from tkinter import *
from tkinter import filedialog
import math

specialCars = []
from operator import itemgetter
import time

openQueue = []
closed = {}
solutionFound = False


class Car:
    def __init__(self, letter):
        self.letter = letter
        self.x = []
        self.y = []
        self.vertical = False
        self.fuel = 100

    # Sets orientation of car
    def orientation(self):
        if (self.y[0] == self.y[1]):
            self.vertical = True
        return

    def __str__(self):
        return self.letter + ":\n x:" + str(self.x) + "\n y:" + str(self.y) + "\n"

    def changeFuel(self, number):
        self.fuel = number
        return


class BoardGen:
    def __init__(self, cars, pathLength, path, boardHistory):
        self.heuristic = 100
        self.path = path
        self.cars = cars
        self.carA = 0
        self.string = ""
        self.pathLength = pathLength
        self.boardHistory = boardHistory
        self.board = [["."] * 6 for i in range(0, 6)]

        for i in range(0, 6):
            for j in range(0, 6):
                self.board[i][j] = '.'

        finalMatrix = True
        while (finalMatrix):
            finalMatrix = self.createMatrix()

        for i in range(0, 6):
            for j in range(0, 6):
                self.string += str(self.board[i][j])
        if selectedHeuristic == "1":
            self.heuristic = self.numberCarsBlocking()
        elif selectedHeuristic == "2":
            self.heuristic = self.numberPositionsBlocking()
        elif selectedHeuristic == "3":
            self.heuristic = self.numberCarsBlockingMultiplied()
        elif selectedHeuristic == "4":
            self.heuristic = self.numberCarsBlockingBlocked()
        else:
            print("no heuristic selected")

        self.boardHistory[self.pathLength - 1] += self.string

        global solutionFound
        global canWrite
        if solutionFound and canWrite:
            canWrite = False
            openQueue.clear()
            global solution
            global searchPathLength
            solution = solution + "\n Runtime: " + str(time.time() - start_time) + " seconds"
            solution = solution + "\n Search Path Length: " + str(searchPathLength)
            solution = solution + "\n Solution Path Length: " + str(self.pathLength)
            solution = solution + "\n Solution Path: " + str(self.path) + "\n\n"
            for b in self.boardHistory:
                solution = solution + b + "\n"

            solution = solution = solution + "\n"
            for line in self.board:
                solution = solution + str(line) + "\n"

    # h1: The number of blocked cars
    def numberCarsBlocking(self):
        individualBlockingCars = []
        row = 2
        column = self.carA + 1
        while (column < 6):
            # print (self.board[row][column])
            if self.board[row][column] not in individualBlockingCars and self.board[row][column] != ".":
                individualBlockingCars.append(self.board[row][column])
            column += 1
        return len(individualBlockingCars)

    # h2: The number of blocked positions
    def numberPositionsBlocking(self):
        individualBlockingPositions = 0
        row = 2
        column = self.carA + 1
        while (column < 6):
            if self.board[row][column] != ".":
                individualBlockingPositions += 1
            column += 1
        return individualBlockingPositions

    # h3: The value of h1 multiplied by a constant ?? of your choice (2), where ?? > 1.
    def numberCarsBlockingMultiplied(self):
        lambdavalue = 2
        individualBlockingCars = []
        row = 2
        column = self.carA + 1
        while (column < 6):
            # print (self.board[row][column])
            if self.board[row][column] not in individualBlockingCars and self.board[row][column] != ".":
                individualBlockingCars.append(self.board[row][column])
            column += 1
        return lambdavalue * len(individualBlockingCars)

    # h4: The number of blocked cars+ the minimum amount of cars blocking the previously mentioned blocked car if it's vertical. If the car in front is horizontal return 1 (since it should be easily removed 90% of the time) and return 0 if path is clear
    def numberCarsBlockingBlocked(self):
        blockingCars = []
        blockingBlockedCars = 0
        solutions= []
        row = 2
        column = self.carA + 1
        # print(column)
        while (column < 6):
            # print (str(row) + " " + str(column) + " " +self.board[row][column]+"\n")
            if self.board[row][column] not in blockingCars and self.board[row][column] != ".":
                blockingCars.append(self.board[row][column])

                # Check if car is vertical
                verticalCar = False
                letter = ""
                for car in self.cars:
                    if car.letter == self.board[row][column]:
                        verticalCar = car.vertical
                        letter = car.letter

                if (verticalCar == True):
                    # Check if the car blocking has a car blocking it on top or under
                    if (self.board[row + 1][column] != self.board[row][column]
                            or self.board[row - 1][column] != self.board[row][column]
                            or self.board[row + 2][column] != self.board[row][column]
                            or self.board[row - 2][column] != self.board[row][column]):
                        blockingBlockedCars = blockingBlockedCars + 1
            solutions.append(blockingBlockedCars)
            column += 1
        if(len(solutions)>0):
            return len(blockingCars) + min(solutions)
        if(len(solutions)==0):
            return 1


    def createMatrix(self):
        for i in range(0, 6):
            for j in range(0, 6):
                self.board[i][j] = '.'
        for car in self.cars:
            if (car.letter == 'A'):
                self.carA = car.y[-1]
            for i in range(0, len(car.x)):
                self.board[car.x[i]][car.y[i]] = car.letter
                if (car.x[i] == 2 and car.y[i] == 5 and self.board[car.x[i]][car.y[i]] == 'A'):
                    print("Found a solution")
                    print(self.path)
                    print("--- %s seconds ---" % (time.time() - start_time))
                    global solutionFound
                    solutionFound = True
                orientation = car.vertical
                if (car.x[i] == 2 and car.y[i] == 5 and orientation == False):
                    self.cars.remove(car)
                    return True
        return False

    def __str__(self):
        return self.string

    def verticalMove(self):
        cars_copy = copy.deepcopy(self.cars)
        for i in range(0, len(cars_copy)):
            if (cars_copy[i].vertical == False):
                continue
            row = cars_copy[i].x[-1]
            columm = cars_copy[i].y[0]
            fuelCost = 1
            while row + fuelCost < 6 and self.board[row + fuelCost][columm] == ".":
                cars_copy[i].x = [pos + fuelCost for pos in cars_copy[i].x]
                if (int(cars_copy[i].fuel) >= 1):
                    cars_copy[i].changeFuel(int(cars_copy[i].fuel) - 1)
                    history = copy.deepcopy(self.boardHistory)
                    history.append(cars_copy[i].letter + " down " + str(fuelCost) + "\t")
                    generatedBoard = BoardGen(cars_copy, self.pathLength + 1,
                                              self.path + cars_copy[i].letter + " down " + str(fuelCost) + "-->",
                                              history)
                    openQueue.append({"priority": generatedBoard.heuristic,
                                      "board": generatedBoard,
                                      "string": str(generatedBoard)})
                cars_copy = copy.deepcopy(self.cars)
                fuelCost += 1

        cars_copy = copy.deepcopy(self.cars)
        for i in range(0, len(cars_copy)):
            if (cars_copy[i].vertical == False):
                continue
            row = cars_copy[i].x[0]
            columm = cars_copy[i].y[0]
            fuelCost = 1
            while row - fuelCost > -1 and self.board[row - fuelCost][columm] == ".":
                cars_copy[i].x = [pos - fuelCost for pos in cars_copy[i].x]
                if (int(cars_copy[i].fuel) >= 1):
                    cars_copy[i].changeFuel(int(cars_copy[i].fuel) - 1)
                    history = copy.deepcopy(self.boardHistory)
                    history.append(cars_copy[i].letter + " up " + str(fuelCost) + "\t")
                    generatedBoard = BoardGen(cars_copy, self.pathLength + 1,
                                              self.path + cars_copy[i].letter + " up " + str(fuelCost) + "-->",
                                              history)
                    openQueue.append({"priority": generatedBoard.heuristic,
                                      "board": generatedBoard,
                                      "string": str(generatedBoard)})
                cars_copy = copy.deepcopy(self.cars)
                fuelCost += 1

        return

    def horizontalMove(self):
        cars_copy = copy.deepcopy(self.cars)
        for i in range(0, len(cars_copy)):
            if (cars_copy[i].vertical == True):
                continue
            columm = cars_copy[i].y[-1]
            row = cars_copy[i].x[0]
            fuelCost = 1
            while columm + fuelCost < 6 and self.board[row][columm + fuelCost] == ".":
                cars_copy[i].y = [pos + fuelCost for pos in cars_copy[i].y]
                if (int(cars_copy[i].fuel) >= 1):
                    cars_copy[i].changeFuel(int(cars_copy[i].fuel) - 1)
                    history = copy.deepcopy(self.boardHistory)
                    history.append(cars_copy[i].letter + " right " + str(fuelCost) + "\t")
                    generatedBoard = BoardGen(cars_copy, self.pathLength + 1,
                                              self.path + cars_copy[i].letter + " right " + str(fuelCost) + "-->",
                                              history)
                    openQueue.append({"priority": generatedBoard.heuristic,
                                      "board": generatedBoard,
                                      "string": str(generatedBoard)})
                cars_copy = copy.deepcopy(self.cars)
                fuelCost += 1

        cars_copy = copy.deepcopy(self.cars)
        for i in range(0, len(cars_copy)):
            if (cars_copy[i].vertical == True):
                continue
            columm = cars_copy[i].y[0]
            row = cars_copy[i].x[0]
            fuelCost = 1
            while columm - fuelCost > -1 and self.board[row][columm - fuelCost] == ".":
                cars_copy[i].y = [pos - fuelCost for pos in cars_copy[i].y]
                if (int(cars_copy[i].fuel) >= 1):
                    cars_copy[i].changeFuel(int(cars_copy[i].fuel) - 1)
                    history = copy.deepcopy(self.boardHistory)
                    history.append(cars_copy[i].letter + " left " + str(fuelCost) + "\t")
                    generatedBoard = BoardGen(cars_copy, self.pathLength + 1,
                                              self.path + cars_copy[i].letter + " left " + str(fuelCost) + "-->",
                                              history)
                    openQueue.append({"priority": generatedBoard.heuristic,
                                      "board": generatedBoard,
                                      "string": str(generatedBoard)})
                cars_copy = copy.deepcopy(self.cars)
                fuelCost += 1

        return

    # Generate a new board based on the possible moves (TO BE ADDED)
    def MoveCar(self):
        self.verticalMove()
        self.horizontalMove()


class Board:
    # creating 2D array
    def __init__(self, inp):
        self.cost = 0
        self.heuristic = 10
        self.special = []
        # Separate board from fuel amounts
        self.inp = inp[:36]
        self.fuel = inp[37:].split(" ")
        self.matrix = [["0"] * 6 for i in range(0, 6)]
        self.string = ""
        global solution
        n = 0
        for i in range(0, 6):
            for j in range(0, 6):
                self.matrix[i][j] = self.inp[n]
                n += 1
        for i in range(0, 6):
            for j in range(0, 6):
                self.string += str(self.matrix[i][j])

        # Find all unique letters
        letters = []
        for i in range(0, 36):
            if (inp[i] not in letters and inp[i] != "."):
                letters.append(inp[i])

        for i in range(0, 6):
            solution = solution + str(self.matrix[i]) + "\n"
        # for i in range(0, 6):
        # print(self.matrix[i])
        # create all cars
        self.cars = []
        for i in letters:
            self.cars.append(Car(i))

        # Find all X and Y positions of each car
        for car in self.cars:
            for i in range(0, 6):
                for j in range(0, 6):
                    if (self.matrix[i][j] == car.letter):
                        car.x.append(i)
                        car.y.append(j)
        # Set proper fuel level to each car
        for car in self.cars:
            for f in self.fuel:
                if (len(f) > 0):
                    if (f[0] == car.letter):
                        car.changeFuel(f[1])
                        self.special.append(car.letter)
        solution = solution + "\n Car fuel available: "
        for car in self.cars:
            solution = solution + car.letter + ":" + str(car.fuel) + " "
        for car in self.cars:
            car.orientation()

        finalMatrix = True;
        while (finalMatrix):
            finalMatrix = self.createMatrix()
        # print matrix
        self.matrix = [["."] * 6 for i in range(0, 6)]
        for index in range(0, len(self.cars)):
            for i in range(0, len(self.cars[index].x)):
                self.matrix[self.cars[index].x[i]][self.cars[index].y[i]] = self.cars[index].letter
        for i in range(0, 6):
            print(self.matrix[i])

    def createMatrix(self):
        for car in self.cars:
            for i in range(0, len(car.x)):
                self.matrix[car.x[i]][car.y[i]] = car.letter
                if car.x[i] == 2 and car.y[i] == 5 and self.matrix[car.x[i]][car.y[i]] == 'A':
                    print("Found a solution. Its correct from the start")
                    print("--- %s seconds ---" % (time.time() - start_time))
                    global solutionFound
                    solutionFound = True
                if car.x[i] == 2 and car.y[i] == 5 and car.vertical == False:
                    self.cars.remove(car)
                    return True
        return False

    def verticalMove(self):
        cars_copy = copy.deepcopy(self.cars)
        for i in range(0, len(cars_copy)):
            if (cars_copy[i].vertical == False):
                continue
            row = cars_copy[i].x[-1]
            columm = cars_copy[i].y[0]
            fuelCost = 1
            while row + fuelCost < 6 and self.matrix[row + fuelCost][columm] == ".":
                cars_copy[i].x = [pos + fuelCost for pos in cars_copy[i].x]
                if (int(cars_copy[i].fuel) >= 1):
                    cars_copy[i].changeFuel(int(cars_copy[i].fuel) - 1)
                    generatedBoard = BoardGen(cars_copy, 1,
                                              cars_copy[i].letter + " down " + str(fuelCost) + "-->",
                                              [cars_copy[i].letter + " down " + str(fuelCost) + "\t"])
                    openQueue.append({"priority": generatedBoard.heuristic,
                                      "board": generatedBoard,
                                      "string": str(generatedBoard)})
                cars_copy = copy.deepcopy(self.cars)
                fuelCost += 1

        cars_copy = copy.deepcopy(self.cars)
        for i in range(0, len(cars_copy)):
            if (cars_copy[i].vertical == False):
                continue
            row = cars_copy[i].x[0]
            columm = cars_copy[i].y[0]
            fuelCost = 1
            while row - fuelCost > -1 and self.matrix[row - fuelCost][columm] == ".":
                cars_copy[i].x = [pos - fuelCost for pos in cars_copy[i].x]
                if (int(cars_copy[i].fuel) >= 1):
                    cars_copy[i].changeFuel(int(cars_copy[i].fuel) - 1)
                    generatedBoard = BoardGen(cars_copy, 1,
                                              cars_copy[i].letter + " up " + str(fuelCost) + "-->",
                                              [cars_copy[i].letter + " up " + str(fuelCost) + "\t"])
                    openQueue.append({"priority": generatedBoard.heuristic,
                                      "board": generatedBoard,
                                      "string": str(generatedBoard)})
                cars_copy = copy.deepcopy(self.cars)
                fuelCost += 1

        return

    def horizontalMove(self):
        cars_copy = copy.deepcopy(self.cars)
        for i in range(0, len(cars_copy)):
            if (cars_copy[i].vertical == True):
                continue
            columm = cars_copy[i].y[-1]
            row = cars_copy[i].x[0]
            fuelCost = 1
            while columm + fuelCost < 6 and self.matrix[row][columm + fuelCost] == ".":
                cars_copy[i].y = [pos + fuelCost for pos in cars_copy[i].y]
                if (int(cars_copy[i].fuel) >= 1):
                    cars_copy[i].changeFuel(int(cars_copy[i].fuel) - 1)
                    generatedBoard = BoardGen(cars_copy, 1,
                                              cars_copy[i].letter + " right " + str(fuelCost) + "-->",
                                              [cars_copy[i].letter + " right " + str(fuelCost) + "\t"])
                    openQueue.append({"priority": generatedBoard.heuristic,
                                      "board": generatedBoard,
                                      "string": str(generatedBoard)})
                cars_copy = copy.deepcopy(self.cars)
                fuelCost += 1

        cars_copy = copy.deepcopy(self.cars)
        for i in range(0, len(cars_copy)):
            if (cars_copy[i].vertical == True):
                continue
            columm = cars_copy[i].y[0]
            row = cars_copy[i].x[0]
            fuelCost = 1
            while columm - fuelCost > -1 and self.matrix[row][columm - fuelCost] == ".":
                cars_copy[i].y = [pos - fuelCost for pos in cars_copy[i].y]
                if (int(cars_copy[i].fuel) >= 1):
                    cars_copy[i].changeFuel(int(cars_copy[i].fuel) - 1)
                    generatedBoard = BoardGen(cars_copy, 1,
                                              cars_copy[i].letter + " left " + str(fuelCost) + "-->",
                                              [cars_copy[i].letter + " left " + str(fuelCost) + "\t"])
                    openQueue.append({"priority": generatedBoard.heuristic,
                                      "board": generatedBoard,
                                      "string": str(generatedBoard)})

                cars_copy = copy.deepcopy(self.cars)
                fuelCost += 1

        return

    # Generate a new board based on the possible moves (TO BE ADDED)
    def MoveCar(self):
        closed[self.string] = self.string
        self.verticalMove()
        self.horizontalMove()

    def __str__(self):
        output = ''
        for i in self.cars:
            output += str(i)
        return output


def removeClosed():
    for index in range(0, len(openQueue)):
        try:
            key = openQueue[index]['string']
            found = closed[key]
            del openQueue[index]
            return True
        except:
            found = 0  # do nothing

    return False


solution = ""
searchPathLength = 0
count = 0
canWrite = True
selectedHeuristic = input("Enter Heuristic Number")
root = Tk()
root.title("Hello There")

root.filename = filedialog.askopenfilename(title="Select A File", filetypes=(("text files", "txt"),))
theFile = open(root.filename, "r")
while (True):
    solutionFound = False
    line = theFile.readline()
    if (len(line) < 36):
        print("Thanks for playing")
        print(solution)
        count += 1
        file = open("gbfs-sol " + str(count) + " h" + str(selectedHeuristic) + ".txt", "w")
        file.write(solution)
        file.close()
        solution = ""
        canWrite = False
        exit()

    if solution != "":
        count += 1
        file = open("gbfs-sol " + str(count) + " h" + str(selectedHeuristic) + ".txt", "w")
        file.write(solution)
        file.close()
        solution = ""
        canWrite = False
    solution = ""
    solution = solution + "Initial board configuration: " + line + "\n\n"
    start_time = time.time()

    if not line:
        break
    print(line)
    canWrite = True
    searchPathLength = 0
    game = Board(line)
    game.MoveCar()
    fileSearch = open("gbfs-search" + str(count + 1) + " h" + str(selectedHeuristic) + ".txt", "w")
    while (len(openQueue) > 0):
        if (solutionFound == True):
            openQueue.clear()
            closed.clear()
            break

        foundClosed = True
        while (foundClosed):
            foundClosed = removeClosed()
        openQueue = sorted(openQueue, key=itemgetter('priority'))
        # print(str(len(openQueue)) + " " + str(len(closed)))
        if len(openQueue) > 0:
            searchPathLength += 1
            fileSearch.write(str(math.floor(openQueue[0]['priority'])) + " " + str(0) + " " + str(
                math.floor(openQueue[0]['board'].heuristic)) + " " + openQueue[0]['string'] + "\n")
            openQueue[0]['board'].MoveCar()
            key = openQueue[0]['string']
            closed[key] = key
            del openQueue[0]
    if (solutionFound == False):
        print("No solution found")
        print("--- %s seconds ---" % (time.time() - start_time))
        openQueue.clear()
        closed.clear()
