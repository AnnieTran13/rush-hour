from queue import PriorityQueue
import copy
specialCars = []
from queue import PriorityQueue
from operator import itemgetter
import time


open = []
closed = {}

class Car:
	def __init__(self,letter):
		self.letter = letter
		self.x = []
		self.y = []
		self.vertical = False
		self.fuel=100

	#Sets orientation of car
	def orientation(self):
		if(self.y[0]==self.y[1]):
			self.vertical=True
		return		
		
	def __str__(self):
		return self.letter + ":\n x:" + str(self.x) + "\n y:" + str(self.y)+"\n"
		
	def changeFuel(self,number):
		self.fuel = number
		return
		



class BoardGen:
	def __init__(self, cost, cars, special, path):
		self.cost = cost
		self.path = path
		self.cars = cars
		self.special = special
		self.string = ""
		self.board = [["."]*6 for i in range(0,6)]

		for i in range(0, 6):
			for j in range(0, 6):
				self.board[i][j] = '.'

		finalMatrix=True;
		while(finalMatrix):
			finalMatrix=self.createMatrix()

		for i in range(0,6):
			for j in range(0, 6):
				self.string+=str(self.board[i][j])

	def createMatrix(self):
		for car in self.cars:
			for i in range(0, len(car.x)):
				self.board[car.x[i]][car.y[i]]=car.letter
				if(car.x[i]==2 and car.y[i]==5 and self.board[car.x[i]][car.y[i]]=='A'):
					print("Found a solution")
					print (self.path)
					print("--- %s seconds ---" % (time.time() - start_time))
					exit()
				if (car.x[i] == 2 and car.y[i] == 5):
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
			while row + fuelCost < 6 and self.board[row+fuelCost][columm] == ".":
				cars_copy[i].x = [pos + fuelCost for pos in cars_copy[i].x]
				if (int(cars_copy[i].fuel) >= 1):
					cars_copy[i].changeFuel(int(cars_copy[i].fuel) - 1)
					generatedBoard = BoardGen(self.cost + 1, cars_copy, self.special, self.path + cars_copy[i].letter + " down " + str(fuelCost)+ "-->")
					open.append({"priority": self.cost + 1,
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
					generatedBoard = BoardGen(self.cost + 1, cars_copy, self.special, self.path + cars_copy[i].letter + " up " + str(fuelCost)+ "-->")
					open.append({"priority": self.cost + 1,
								 "board": generatedBoard,
								 "string": str(generatedBoard)})
				cars_copy = copy.deepcopy(self.cars)
				fuelCost += 1


		return

	def horizontalMove(self):
		cars_copy = copy.deepcopy(self.cars)
		for i in range(0,len(cars_copy)):
			if(cars_copy[i].vertical==True):
				continue
			columm = cars_copy[i].y[-1]
			row = cars_copy[i].x[0]
			fuelCost = 1
			while columm + fuelCost < 6 and self.board[row][columm + fuelCost] == ".":
				cars_copy[i].y = [pos + fuelCost for pos in cars_copy[i].y]
				if (int(cars_copy[i].fuel) >= 1):
					cars_copy[i].changeFuel(int(cars_copy[i].fuel) - 1)
					generatedBoard = BoardGen(self.cost + 1, cars_copy, self.special, self.path + cars_copy[i].letter + " right " + str(fuelCost)+ "-->")
					open.append({"priority": self.cost + 1,
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
					generatedBoard = BoardGen(self.cost + 1, cars_copy, self.special, self.path + cars_copy[i].letter + " left " + str(fuelCost)+ "-->")
					open.append({"priority": self.cost + 1,
								 "board": generatedBoard,
								 "string": str(generatedBoard)})
				cars_copy = copy.deepcopy(self.cars)
				fuelCost += 1


		return
	#Generate a new board based on the possible moves (TO BE ADDED)
	def MoveCar(self):
		self.verticalMove()
		self.horizontalMove()













class Board:
	#creating 2D array
	def __init__(self,inp):
		self.cost = 0
		self.heuristic = 0
		self.special=[]
		#Seperate board from fuel amounts
		self.inp = inp[:36]
		self.fuel = inp[37:].split(" ")
		self.matrix = [["0"]*6 for i in range(0,6)]
		self.string=""
		n=0
		for i in range(0,6):
			for j in range(0,6):
				self.matrix[i][j]=self.inp[n]
				n+=1
		for i in range(0,6):
			for j in range(0, 6):
				self.string += str(self.matrix[i][j])

		#Find all unique letters
		letters=[]
		for i in range(0,36):
			if(inp[i] not in letters and inp[i]!="."):
				letters.append(inp[i])

		#for i in range(0, 6):
			#print(self.matrix[i])
		#create all cars
		self.cars = []
		for i in letters:
			self.cars.append(Car(i))

		#Find all X and Y positions of each car
		for car in self.cars:
			for i in range(0,6):
				for j in range(0,6):
					if (self.matrix[i][j] == car.letter):
						car.x.append(i)
						car.y.append(j)
		#Set proper fuel level to each car
		for car in self.cars:
			for f in self.fuel:
				if(len(f)>0):
					if(f[0]==car.letter):
						car.changeFuel(f[1])
						self.special.append(car.letter)
		for car in self.cars:
			car.orientation()

		finalMatrix = True;
		while (finalMatrix):
			finalMatrix = self.createMatrix()
			# print matrix
		self.matrix = [["."] * 6 for i in range(0, 6)]
		for index in range(0, len(self.cars)):
			for i in range(0, len(self.cars[index].x)):
				self.matrix[self.cars[index].x[i]][self.cars[index].y[i]]=self.cars[index].letter
		for i in range(0, 6):
			print(self.matrix[i])

	def createMatrix(self):
		for car in self.cars:
			for i in range(0, len(car.x)):
				self.matrix[car.x[i]][car.y[i]]=car.letter
				if car.x[i]==2 and car.y[i]==5 and self.matrix[car.x[i]][car.y[i]]== 'A':
					print("Found a solution. Its correct from the start")
					for i in range(0, 6):
						print(self.matrix[i])
					print("--- %s seconds ---" % (time.time() - start_time))
					exit()
				if car.x[i] == 2 and car.y[i] == 5:
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
			while row + fuelCost < 6 and self.matrix[row+fuelCost][columm] == ".":
				cars_copy[i].x = [pos + fuelCost for pos in cars_copy[i].x]
				if (int(cars_copy[i].fuel) >= 1):
					cars_copy[i].changeFuel(int(cars_copy[i].fuel) - 1)
					generatedBoard = BoardGen(self.cost + 1, cars_copy, self.special, cars_copy[i].letter + " down " + str(fuelCost)+ "-->")
					open.append({"priority": self.cost + 1,
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
					generatedBoard = BoardGen(self.cost + 1, cars_copy, self.special, cars_copy[i].letter + " up " + str(fuelCost)+ "-->")
					open.append({"priority": self.cost + 1,
								 "board": generatedBoard,
								 "string": str(generatedBoard)})
				cars_copy = copy.deepcopy(self.cars)
				fuelCost += 1


		return

	def horizontalMove(self):
		cars_copy = copy.deepcopy(self.cars)
		for i in range(0,len(cars_copy)):
			if(cars_copy[i].vertical==True):
				continue
			columm = cars_copy[i].y[-1]
			row = cars_copy[i].x[0]
			fuelCost = 1
			while columm + fuelCost < 6 and self.matrix[row][columm + fuelCost] == ".":
				cars_copy[i].y = [pos + fuelCost for pos in cars_copy[i].y]
				if (int(cars_copy[i].fuel) >= 1):
					cars_copy[i].changeFuel(int(cars_copy[i].fuel) - 1)
					generatedBoard = BoardGen(self.cost + 1, cars_copy, self.special, cars_copy[i].letter + " right " + str(fuelCost)+ "-->")
					open.append({"priority": self.cost + 1,
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
					generatedBoard = BoardGen(self.cost + 1, cars_copy, self.special, cars_copy[i].letter + " left " + str(fuelCost)+ "-->")
					open.append({"priority": self.cost + 1,
								 "board": generatedBoard,
								 "string": str(generatedBoard)})

				cars_copy = copy.deepcopy(self.cars)
				fuelCost += 1


		return
	#Generate a new board based on the possible moves (TO BE ADDED)
	def MoveCar(self):
		closed[self.string]= self.string
		self.verticalMove()
		self.horizontalMove()
	
	def __str__(self):
		output=''
		for i in self.cars:
			output+=str(i)
		return output


def removeClosed():
	for index in range(0, len(open)):
			try:
				key = open[index]['string']
				found = closed[key]
				del open[index]
				return True
			except:
				found = 0 #do nothing

	return False


start_time = time.time()
# c= '...GF...BGF.AABCF....CDD...C....EE..'
c= 'IIB...C.BHHHC.AAD.....D.EEGGGF.....F'
#c = 'BB.............AAM.....M............'
game=Board(c)
game.MoveCar()
while (len(open)>0):
	foundClosed = True
	while(foundClosed):
		foundClosed=removeClosed()
	open = sorted(open, key=itemgetter('priority'))
	#print(str(len(open)) + " " + str(len(closed)))
	if len(open)>0:
		open[0]['board'].MoveCar()
		key = open[0]['string']
		closed[key]=key
		del open[0]

print("No solution found")
print("--- %s seconds ---" % (time.time() - start_time))