specialCars = []
possibleBoards=[]
import copy
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
	def __init__(self, cost, cars, special):
		self.cost = cost
		self.cars = cars
		self.special = special
		self.board = [["."]*6 for i in range(0,6)]

		for i in range(0, 6):
			for j in range(0, 6):
				self.board[i][j] = '.'

		for car in self.cars:
			for i in range(0, len(car.x)):
				self.board[car.x[i]][car.y[i]]=car.letter

		print("\n")
		for i in range(0,6):
			print(self.board[i])
		print("\n")





def Move(self):
	arrayMatrix = []
	for car in self.cars:
		car.MoveCar()

	return arrayMatrix

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
		n=0
		for i in range(0,6):
			for j in range(0,6):
				self.matrix[i][j]=self.inp[n]
				n+=1
		#print matrix
		for i in range(0,6):
			print(self.matrix[i])

		#Find all unique letters
		letters=[]
		for i in range(0,36):
			if(inp[i] not in letters and inp[i]!="."):
				letters.append(inp[i])


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
				if(f[0]==car.letter):
					car.changeFuel(f[1])
					self.special.append(car.letter)
		for car in self.cars:
			car.orientation()

	
	def Move(self):
		self.MoveCar()


	def verticalMove(self):
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
				generatedBoard =BoardGen(self.cost+fuelCost, cars_copy, self.special)
				possibleBoards.append(generatedBoard)
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
				generatedBoard = BoardGen(self.cost + fuelCost, cars_copy, self.special)
				possibleBoards.append(generatedBoard)
				cars_copy = copy.deepcopy(self.cars)
				fuelCost += 1


		return
	#Generate a new board based on the possible moves (TO BE ADDED)
	def MoveCar(self):
		self.verticalMove()
		print("Here")
		self.horizontalMove()
	
	def __str__(self):
		output=''
		for i in self.cars:
			output+=str(i)
		return output


  
c = 'BB.PP...I.CC..IAAMGDDK.MGH.KL.GHFFL. B0 J2'
game=Board(c)
game.MoveCar()
#print(game)
