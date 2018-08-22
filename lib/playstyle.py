class PlayStyle:
	
	def __init__(self, name='Default playstyle', position=15, use_satellites=True,
				 maximum_satellites_number_per_planet=500, use_solar_plant=True, use_fusion_reactor=True,
				 position_15_reordering=True, number_of_planets_before_reordering=7):
		self.name = name
		self.position = position
		self.use_satellites = use_satellites
		self.maximum_satellites_number_per_planet = maximum_satellites_number_per_planet
		self.use_solar_plant = use_solar_plant
		self.use_fusion_reactor = use_fusion_reactor
		self.position_15_reordering = position_15_reordering
		self.number_of_planets_before_reordering = number_of_planets_before_reordering
	
	
	def add_planet(self, planet):
		self.planets.append(planet)
	
	
	def __str__(self):
		return self.username + ', ' + str(len(self.planets)) + ' planets'
	
	
	def pretty(self):
		print('Playstyle name: ' + self.name)
		print('Position: ' + str(self.position))
		print('Sattelites usage: ' + str(self.use_satellites))
		if self.use_satellites:
			print('Maximum satellites number per planet: ' + str(self.maximum_satellites_number_per_planet))
		print('Solar plant usage: ' + str(self.use_solar_plant))
		print('Fusion reactor usage: ' + str(self.use_fusion_reactor))
		print('Position 15 reordering: ' + str(self.position_15_reordering))
		if self.position_15_reordering:
			print('Number of planets before reordering: ' + str(self.number_of_planets_before_reordering))
