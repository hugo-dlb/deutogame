from .utils import production
from .utils import next_level_cost
from .utils import next_level_profitability_metalized
from .utils import next_astrophysics_cost
from .utils import astrophysics_over_mine


class Planet:
	
	def __init__(self, diameter, temperature, server_speed=1, name='Colony', position=15, astrophysics=0, account=None):
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
		self.astrophysics = astrophysics
		self.account = account
	
	
	def add_one_day_of_production(self):
		metal_production_metalized = production(self, 'metal', self.metal, self.temperature, True)
		cristal_production_metalized = production(self, 'cristal', self.cristal, self.temperature, True)
		deuterium_production_metalized = production(self, 'deuterium', self.deuterium, self.temperature, True)
		self.account.resources += ((metal_production_metalized + cristal_production_metalized + deuterium_production_metalized) / 1000)
	
	
	def can_do_next_most_efficient_step(self):
		step = self.get_next_most_efficient_step()
		if step == 'astrophysics':
			return self.account.resources >= next_astrophysics_cost(self.astrophysics, True)
		elif step == 'metal':
			return self.account.resources >= next_level_cost('metal', self.metal, True)
		elif step == 'cristal':
			return self.account.resources >= next_level_cost('cristal', self.cristal, True)
		elif step == 'deuterium':
			return self.account.resources >= next_level_cost('deuterium', self.deuterium, True)
		else:
			print('Unknown step: ' + step + ' !')
			return None
	
	def get_next_most_efficient_step(self):
		if self.energy > 0:
			step = self.get_next_most_efficient_step()
		else:
			step = self.get_next_most_efficient_energy_step()
		return step
	
	
	def get_next_most_efficient_step(self):
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
		if self.position == 15:
			return 'fusion_reactor'
		else:
			if self.solar_plant < 20:
				return 'solar_plant'
			else:
				return 'satellites'
	
	
	def do_next_most_efficient_step(self):
		step = self.get_next_most_efficient_step()
		if step == 'astrophysics':
			self.account.resources -= round(next_astrophysics_cost(self.astrophysics, True))
			self.account.points += round(next_astrophysics_cost(self.astrophysics, True) / 1000)
			if self.account.astrophysics == 0:
				self.account.astrophysics += 1
			else:
				self.account.astrophysics += 2
		elif step == 'metal':
			self.account.resources -= round(next_level_cost('metal', self.metal, True))
			self.account.points += round(next_level_cost('metal', self.metal, True) / 1000)
			self.metal += 1
		elif step == 'cristal':
			self.account.resources -= round(next_level_cost('cristal', self.cristal, True))
			self.account.points += round(next_level_cost('cristal', self.cristal, True) / 1000)
			self.cristal += 1
		elif step == 'deuterium':
			self.account.resources -= round(next_level_cost('deuterium', self.deuterium, True))
			self.account.points += round(next_level_cost('deuterium', self.deuterium, True) / 1000)
			self.deuterium += 1
		elif step == 'fusion_reactor':
			self.account.resources -= round(next_level_cost('fusion_reactor', self.fusion_reactor, True))
			self.account.points += round(next_level_cost('fusion_reactor', self.fusion_reactor, True) / 1000)
			self.fusion_reactor += 1
		elif step == 'solar_plant':
			self.account.resources -= round(next_level_cost('solar_plant', self.solar_plant, True))
			self.account.points += round(next_level_cost('solar_plant', self.solar_plant, True) / 1000)
			self.solar_plant += 1
		elif step == 'satellites':
			# todo somehow handle satellites
		else:
			print('Unknown step: ' + step + ' !')
			return None
	
	
	def __str__(self):
		return self.name + ', ' + str(self.diameter) + ' cells, ' + 'position ' + str(self.position) + ', ' + str(
			self.temperature) + '°, M' + str(self.metal) + ', C' + str(self.cristal) + ', D' + str(self.deuterium)
