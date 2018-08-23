from .utils import production

class Planet:
	
	def __init__(self, diameter, temperature, server_speed=1, name='Colony', position=15, points=0, astrophysics=0, use_solar_plant=True, use_fusion_reactor=True, use_satellites=True):
		self.server_speed = server_speed
		self.name = name
		self.diameter = diameter
		self.temperature = temperature
		self.position = position
		self.use_solar_plant = use_solar_plant
		self.solar_plant = 0
		self.use_fusion_reactor = use_fusion_reactor
		self.fusion_reactor = 0
		self.use_satellites = use_satellites
		self.satellites = 0
		self.metal = 0
		self.cristal = 0
		self.deuterium = 0
		self.energy = 0
		self.resources = 0
		self.points = points
		self.astrophysics = astrophysics
		self.playstyle = astrophysics
	
	
	def add_one_day_of_production(self):
		metal_production_metalized = production(self, 'metal', self.metal, self.temperature)
		cristal_production_metalized = production(self, 'cristal', self.cristal, self.temperature)
		deuterium_production_metalized = production(self, 'deuterium', self.deuterium, self.temperature)
		self.points += ((metal_production_metalized + cristal_production_metalized + deuterium_production_metalized) / 1000)
	
	
	def __str__(self):
		return self.name + ', ' + str(self.diameter) + ' cells, ' + 'position ' + str(self.position) + ', ' + str(
			self.temperature) + '°, M' + str(self.metal) + ', C' + str(self.cristal) + ', D' + str(self.deuterium) + ', ' + str(self.points) + ' points'
