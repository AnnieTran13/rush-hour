
class Car:
	def __init__(self,letter):
		self.letter = letter
		self.x = []
		self.y = []
		self.vertical = False
		self.fuel=100
	
	def orientation(self):
		if(self.y[0]==self.y[1]):
			self.vertical=True
		return		
		
	def __str__(self):
		return self.letter
		
	def changeFuel(self,number):
		self.fuel = number
		return

class Game:
	#creating 2D array
	def __init__(self,inp):
		
		self.inp = inp[:36]
		self.fuel = c[37:].split(" ")
		self.matrix = [["0"]*6 for i in range(0,6)]
		n=0
		for i in range(0,6):
			for j in range(0,6):
				self.matrix[i][j]=self.inp[n]
				n+=1
				
		for i in range(0,6):
			print(self.matrix[i])
		letters=[]
		for i in range(0,36):
			if(inp[i] not in letters and inp[i]!="."):
				letters.append(inp[i])	
		self.cars = []
		for i in letters:
			self.cars.append(Car(i))
		for car in self.cars:
			for i in range(0,6):
				for j in range(0,6):
					if (self.matrix[i][j] == str(car)):
						car.x.append(i)
						car.y.append(j)
		
		for car in self.cars:
			for f in self.fuel:
				if(f[0]==car.letter):
					car.changeFuel(f[1])
					
			
						
	
		for car in self.cars:
			car.orientation()
			
		print(str(self.cars[2].vertical))
		print(str(self.cars[3].vertical))
	
	
	
	
	def __str__(self):
		output=''
		for i in self.cars:
			output+=str(i)
		return output
			
		
				

c = 'BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL. B0 J2'
game=Game(c)
print(game)


			
	
