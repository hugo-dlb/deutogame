from .playstyle import PlayStyle

class Player:
	
	def __init__(self, username, planets=[], playstyle=None): 
		self.username = username
		self.planets = planets.copy()
		if playstyle:
			self.playstyle = playstyle
		else:
			self.playstyle = PlayStyle()
	
	
	def add_planet(self, planet):
		self.planets.append(planet)
	
	
	def set_playstyle(self, playstyle):
		self.playstyle = playstyle
	
	
	def __str__(self):
		return self.username + ', ' + str(len(self.planets)) + ' planets'