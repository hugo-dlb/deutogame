from .playstyle import PlayStyle

class Account:
	
	def __init__(self, username, planets=[], playstyle=None): 
		self.username = username
		self.astrophysics = 0
		self.energy = 0
		self.points = 0
		self.resources = 0
		self.planets = planets.copy()
		if playstyle:
			self.playstyle = playstyle
		else:
			self.playstyle = PlayStyle()
	
	
	def add_planet(self, planet):
		self.planets.append(planet)
	
	
	def __str__(self):
		return self.username + ', ' + str(len(self.planets)) + ' planets'