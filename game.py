specialCars = []
possibleBoards=[]
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
		return self.letter
		
	def changeFuel(self,number):
		self.fuel = number
		return

	#Generate a new board based on the possible moves (TO BE ADDED)
	def MoveCar(self,board):
		if(fuel!=0):
			if(vertical):
				Vertical(board)
			else:
				Horizontal(board)
					
					
		return board
		
	def Vertical(self,board):
		if(y==0):
			print()
		else if(y==5):
			print()
		else:
			print()
	
	def Horizontal(self,board):
		i=x[0]
		ii = x[-1]
		j=y[0]
		if(i==0):
			while(ii<6 and board[ii+1][j]=="."):
        for a in range(ii,6):
          self.x[a]+=1
        
   
		else if(ii==5):
      while(i>-1 and board[i-1][j]=="."):
        for a in range(0,i):
          self.x[a]-=1
    
		else:
          print("uh oh")



class Board:
	#creating 2D array
	def __init__(self,inp):
		self.cost = 0
		self.heuristic = 0
		#Seperate board from fuel amounts
		self.inp = inp[:36]
		self.fuel = c[37:].split(" ")
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
					if (self.matrix[i][j] == str(car)):
						car.x.append(i)
						car.y.append(j)
		#Set proper fuel level to each car
		for car in self.cars:
			for f in self.fuel:
				if(f[0]==car.letter):
					car.changeFuel(f[1])

		for car in self.cars:
			car.orientation()
			
		self.cars[0].MoveCar(self.matrix)
	
	def Move(self):
		arrayMatrix = []
		for car in self.cars:
			car.MoveCar(tempMatrix)
			
		return arrayMatrix
	
	
	def __str__(self):
		output=''
		for i in self.cars:
			output+=str(i)
		return output

class BoardGen:
  def __init__(self,cost,cars,special,board):
		self.cost = cost
    self.cars = cars
    self.special = special'
    self.matrix = board
  
  def __str__(self):
		output=''
		for i in self.cars:
			output+=str(i)
		return output
  def Move(self):
		arrayMatrix = []
		for car in self.cars:
			car.MoveCar(tempMatrix)
			
		return arrayMatrix
  
			


