
class Game:
	#creating 2D array
	def __init__(self,inp):
		self.inp = inp
		self.matrix = [["0"]*6 for i in range(0,6)]
		n=0
		for i in range(0,6):
			for j in range(0,6):
				self.matrix[i][j]=self.inp[n]
				n+=1
				
		for i in range(0,6):
			print(self.matrix[i])
				
c = 'BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL.'
Game(c)



			
	
