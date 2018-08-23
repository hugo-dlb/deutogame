from .utils import production
from .utils import next_level_cost
from .utils import next_level_profitability_metalized
from .utils import next_astrophysics_cost
from .utils import astrophysics_over_mine


class Planet:
	
	def __init__(self, diameter, temperature, server_speed=1, name='Colony', position=15, points=0, astrophysics=0, playstyle=None):
		self.server_speed = server_speed
		self.name = name
		self.diameter = diameter
		self.temperature = temperature
		self.position = position
		self.use_solar_plant = position != 15
		self.solar_plant = 0
		self.use_fusion_reactor = position == 15
		self.fusion_reactor = 0
		self.use_satellites = position != 15
		self.satellites = 0
		self.metal = 0
		self.cristal = 0
		self.deuterium = 0
		self.energy = 0
		self.resources = 0
		self.points = points
		self.astrophysics = astrophysics
		self.playstyle = playstyle
	
	
	def add_one_day_of_production(self):
		metal_production_metalized = production(self, 'metal', self.metal, self.temperature, True)
		cristal_production_metalized = production(self, 'cristal', self.cristal, self.temperature, True)
		deuterium_production_metalized = production(self, 'deuterium', self.deuterium, self.temperature, True)
		self.points += ((metal_production_metalized + cristal_production_metalized + deuterium_production_metalized) / 1000)
	
	
	def can_do_next_most_efficient_step(self):
		return self.get_next_most_efficient_step() is not None
	
	
	def get_next_most_efficient_step(self):
		if self.energy > 0:
			step = [self.get_next_most_efficient_step()]
		else:
			step = [self.get_next_most_efficient_energy_step(), self.get_next_most_efficient_step()]
		return step
	
	
	def get_next_most_efficient_step(self):
		# todo verify (returns cristal with everything at 0?)
		astro_total_cost_metalized = next_astrophysics_cost(self.astrophysics, True)
		metal_profitability = next_level_profitability_metalized(self, 'metal')
		cristal_profitability = next_level_profitability_metalized(self, 'cristal')
		deuterium_profitability = next_level_profitability_metalized(self, 'deuterium')
		
		mine_possibilities = [['metal', metal_profitability, self.metal], ['cristal', cristal_profitability, self.cristal],
			['deuterium', deuterium_profitability, self.deuterium]]
		most_profitable_mine = min(mine_possibilities, key=lambda mine: mine[1])
		most_profitable_mine_production_gain_per_hour_metalized = production(self, most_profitable_mine[0], most_profitable_mine[2] + 1,
			self.temperature, True) - production(self, most_profitable_mine[0], most_profitable_mine[2], self.temperature, True)
		most_profitable_mine_cost_metalized = next_level_cost(most_profitable_mine[0], most_profitable_mine[2] + 1, True)
		# todo get the average production of all the planets here
		average_production_per_planet_per_hour_metalized = production(self, 'metal', self.metal, self.temperature, True) + production(self,
			'cristal', self.cristal, self.temperature, True) + production(self, 'deuterium', self.deuterium, self.temperature, True)
		
		is_astrophysics_better = astrophysics_over_mine(most_profitable_mine_production_gain_per_hour_metalized, astro_total_cost_metalized,
			most_profitable_mine_cost_metalized, average_production_per_planet_per_hour_metalized)
		
		if is_astrophysics_better:
			return 'astrophysics'
		else:
			return most_profitable_mine[0]
	
	
	def get_next_most_efficient_energy_step(self):
		# todo
		if self.position == 15:
			# todo CEF
			return None
		else:
			if self.solar_plant < 201:
				# todo solar plant
				return None
			else:
				# todo satellites
				return None
	
	
	def do_next_most_efficient_step(self):
		step = self.get_next_most_efficient_step()
	
	
	# todo execute the step
	
	
	def __str__(self):
		return self.name + ', ' + str(self.diameter) + ' cells, ' + 'position ' + str(self.position) + ', ' + str(
			self.temperature) + '°, M' + str(self.metal) + ', C' + str(self.cristal) + ', D' + str(self.deuterium) + ', ' + str(
			self.points) + ' points'
