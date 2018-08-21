class Player:
	
	def __init__(self, username, planets=[]): 
		self.username = username
		self.planets = planets.copy()
	
	
	def add_planet(self, planet):
		self.planets.append(planet)
	
	
	def __str__(self):
		return self.username + ', ' + str(len(self.planets)) + ' planets'