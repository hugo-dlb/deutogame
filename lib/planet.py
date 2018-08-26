from .utils import *
from copy import deepcopy
from math import floor

class Planet:
	
	def __init__(self, name, diameter, temperature, position, account):
		self.name = name
		self.diameter = diameter
		self.temperature = temperature
		self.position = position
		self.solar_plant = 0
		self.fusion_reactor = 0
		self.satellites = 0
		self.metal = 0
		self.crystal = 0
		self.deuterium = 0
		self.energy = 0
		self.account = account
	
	
	def add_one_day_of_production(self):
		metal_production_metalized = production(self, 'metal', self.metal, self.temperature, True) * 24
		crystal_production_metalized = production(self, 'crystal', self.crystal, self.temperature, True) * 24
		deuterium_production_metalized = production(self, 'deuterium', self.deuterium, self.temperature, True) * 24
		self.account.resources += round(metal_production_metalized + crystal_production_metalized + deuterium_production_metalized)
	
	
	def can_do_next_most_efficient_step(self):
		step = self.get_next_most_efficient_step()
		if step == 'astrophysics':
			return self.account.resources >= round(next_astrophysics_cost(self.account.astrophysics, True) + (10000 + 20000 * 1.33 + 10000 * 2))
		elif step == 'metal':
			return self.account.resources >= round(next_level_cost('metal', self.metal, True))
		elif step == 'crystal':
			return self.account.resources >= round(next_level_cost('crystal', self.crystal, True))
		elif step == 'deuterium':
			return self.account.resources >= round(next_level_cost('deuterium', self.deuterium, True))
		elif step == 'fusion_reactor':
			return self.account.resources >= round(next_level_cost('fusion_reactor', self.fusion_reactor, True))
		elif step == 'solar_plant':
			return self.account.resources >= round(next_level_cost('solar_plant', self.solar_plant, True))
		elif step == 'plasma':
			return self.account.resources >= round(next_level_cost('plasma', self.account.plasma, True))
		elif step == 'energy':
			return self.account.resources >= round(next_level_cost('energy', self.account.energy, True))
		elif step == 'satellites':
			# building satellites 50 by 50
			return self.account.resources >= round((2000 * 1.33 + 500 * 2) * 50)
		else:
			print('Unknown step: ' + step + ' !')
			return None
	
	
	def get_next_most_efficient_step(self):
		if self.energy > 0:
			return self.get_next_most_efficient_task()
		else:
			return self.get_next_most_efficient_energy_task()
	
	
	def get_next_most_efficient_task(self):
		# todo add the cost of building all the mines on the potential new colony
		astrophysics_total_cost_metalized = next_astrophysics_cost(self.account.astrophysics, True) + (10000 + 20000 * 1.33 + 10000 * 2)
		metal_profitability = next_level_profitability_metalized(self, 'metal')
		crystal_profitability = next_level_profitability_metalized(self, 'crystal')
		deuterium_profitability = next_level_profitability_metalized(self, 'deuterium')
		plasma_profitability = next_level_profitability_metalized(self, 'plasma')
		
		possibilities = [['metal', metal_profitability, self.metal], ['crystal', crystal_profitability, self.crystal],
			['deuterium', deuterium_profitability, self.deuterium], ['plasma', plasma_profitability, self.account.plasma]]
		
		most_profitable_task = min(possibilities, key=lambda mine: mine[1])
		if most_profitable_task[0] != 'plasma':
			most_profitable_task_production_gain_per_hour_metalized = production(self, most_profitable_task[0], most_profitable_task[2] + 1,
				self.temperature, True) - production(self, most_profitable_task[0], most_profitable_task[2], self.temperature, True)
		else:
			p2 = deepcopy(self)
			p2_account = deepcopy(self.account)
			p2.account = p2_account
			p2.account.plasma += 1
			production_p1_metalized = production(self, 'metal', self.metal, self.temperature, True) + production(self, 'crystal', self.crystal, self.temperature, True) + production(self, 'deuterium', self.deuterium, self.temperature, True)
			production_p2_metalized = production(p2, 'metal', p2.metal, p2.temperature, True) + production(p2, 'crystal',
				p2.crystal, p2.temperature, True) + production(p2, 'deuterium', p2.deuterium, p2.temperature, True)
			most_profitable_task_production_gain_per_hour_metalized = production_p2_metalized - production_p1_metalized
		most_profitable_mine_cost_metalized = next_level_cost(most_profitable_task[0], most_profitable_task[2] + 1, True)
		average_production_per_planet_per_hour_metalized = get_average_planets_production_per_hour(self.account.planets)
		
		is_astrophysics_better = astrophysics_over_task(most_profitable_task_production_gain_per_hour_metalized,
			astrophysics_total_cost_metalized, most_profitable_mine_cost_metalized, average_production_per_planet_per_hour_metalized)
		
		if is_astrophysics_better:
			return 'astrophysics'
		else:
			return most_profitable_task[0]
	
	
	def get_next_most_efficient_energy_task(self):
		if self.position == 15:
			if self.solar_plant < 30:
				return 'solar_plant'
			else:
				if energy_over_fusion_reactor(self):
					return 'energy'
				else:
					return 'fusion_reactor'
		else:
			if self.solar_plant < 10:
				return 'solar_plant'
			else:
				return 'satellites'
	
	
	def do_next_most_efficient_step(self):
		# todo handle p15 reordering somehow
		step = self.get_next_most_efficient_step()
		if step == 'astrophysics':
			cost = round(next_astrophysics_cost(self.account.astrophysics, True) + (10000 + 20000 * 1.33 + 10000 * 2))
			self.account.points += round((next_astrophysics_cost(self.account.astrophysics, True) + (10000 + 20000 * 1.33 + 10000 * 2)) / 1000)
			if self.account.astrophysics == 0:
				self.account.astrophysics += 1
			else:
				self.account.astrophysics += 2
			temperature = get_planet_temperature_by_position(self.account.playstyle.position)
			self.account.planets.append(Planet('Colony', 188, temperature, self.account.playstyle.position, self.account))
		elif step == 'metal':
			cost = round(next_level_cost('metal', self.metal, True))
			self.metal += 1
		elif step == 'crystal':
			cost = round(next_level_cost('crystal', self.crystal, True))
			self.crystal += 1
		elif step == 'deuterium':
			cost = round(next_level_cost('deuterium', self.deuterium, True))
			self.deuterium += 1
		elif step == 'fusion_reactor':
			cost = round(next_level_cost('fusion_reactor', self.fusion_reactor, True))
			self.fusion_reactor += 1
		elif step == 'solar_plant':
			cost = round(next_level_cost('solar_plant', self.solar_plant, True))
			self.solar_plant += 1
		elif step == 'plasma':
			cost = round(next_level_cost('plasma', self.account.plasma, True))
			self.account.plasma += 1
		elif step == 'energy':
			cost = round(next_level_cost('energy', self.account.energy, True))
			self.account.energy += 1
		elif step == 'satellites':
			cost = round((2000 * 1.33 + 500 * 2) * 50)
			self.satellites += 50
		else:
			print('Unknown step: ' + step + ' !')
			return
		
		self.account.resources -= cost
		self.account.points += round(cost / 1000)
		self.account.update_energy()
	
	
	def update_energy(self):
		self.energy = 0
		
		self.energy += get_solar_plant_energy_for_level(self.solar_plant)
		self.energy += get_fusion_reactor_energy_for_level(self.fusion_reactor, self.account.energy)
		self.energy += self.satellites * (floor((self.temperature + 160) / 6))
		
		self.energy -= get_mine_energy_consumption('metal', self.metal)
		self.energy -= get_mine_energy_consumption('crystal', self.crystal)
		self.energy -= get_mine_energy_consumption('deuterium', self.deuterium)
	
	
	def __str__(self):
		return self.name + ', ' + str(self.diameter) + ' cells, ' + 'position ' + str(self.position) + ', ' + str(
			self.temperature) + '°, M' + str(self.metal) + ', C' + str(self.crystal) + ', D' + str(self.deuterium) + ', SP' + str(
			self.solar_plant) + ', FR' + str(self.fusion_reactor) + ' (energy ' + str(self.account.energy) + '), ' + str(self.satellites) + ' satellites, ' + str(
			self.energy) + ' energy'
	
	def get_production_string(self):
		metal_production = production(self, 'metal', self.metal, self.temperature)
		crystal_production = production(self, 'crystal', self.crystal, self.temperature)
		deuterium_production = production(self, 'deuterium', self.deuterium, self.temperature)
		print('Metal production per hour: ' + str(metal_production[0]) + 'M')
		print('Crystal production per hour: ' + str(crystal_production[1]) + 'C')
		print('Deuterium production per hour: ' + str(deuterium_production[2]) + 'D')
	
