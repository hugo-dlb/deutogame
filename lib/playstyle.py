class PlayStyle:
	
	def __init__(self, name, position,
				 position_15_reordering, number_of_planets_before_reordering):
		self.name = name
		self.position = position
		self.position_15_reordering = position_15_reordering
		self.number_of_planets_before_reordering = number_of_planets_before_reordering
	
	
	def add_planet(self, planet):
		self.planets.append(planet)
	
	
	def __str__(self):
		return self.username + ', ' + str(len(self.planets)) + ' planets'
	
	
	def pretty(self):
		print('Playstyle name: ' + self.name)
		print('Position: ' + str(self.position))
		print('Position 15 reordering: ' + str(self.position_15_reordering))
		if self.position_15_reordering:
			print('Number of planets before reordering: ' + str(self.number_of_planets_before_reordering))
