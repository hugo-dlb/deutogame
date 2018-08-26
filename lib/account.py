from .utils import *


class Account:
	
	def __init__(self, username, server_speed, planets, playstyle):
		self.username = username
		self.server_speed = server_speed
		self.astrophysics = 0
		self.energy = 0
		self.plasma = 0
		self.points = 0
		self.energy_points = 0
		self.resources = 0
		self.planets = planets.copy()
		self.playstyle = playstyle
		self.days_data = []
	
	
	def __str__(self):
		return self.username + ', ' + str(len(self.planets)) + ' planets, ' + str(self.points) + ' points, x' + str(
			self.server_speed) + ' server speed, astrophysics ' + str(self.astrophysics) + ' plasma ' + str(self.plasma) + ' energy ' + str(
			self.energy)
	
	
	def update_energy(self):
		for planet in self.planets:
			planet.update_energy()
	
	
	def get_mine_production(self, code):
		metal_production = 0
		crystal_production = 0
		deuterium_production = 0
		
		for planet in self.planets:
			metal_production += production(planet, 'metal', planet.metal, planet.temperature)
			crystal_production += production(planet, 'crystal', planet.crystal, planet.temperature)
			deuterium_production += production(planet, 'deuterium', planet.deuterium, planet.temperature)
		
		metal_average_production = round(metal_production / len(self.planets), 2)
		crystal_average_production = round(crystal_production / len(self.planets), 2)
		deuterium_average_production = round(deuterium_production / len(self.planets), 2)
		
		if code == 'metal':
			return metal_average_production
		elif code == 'crystal':
			return crystal_average_production
		elif code == 'deuterium':
			return deuterium_average_production
		elif code == 'total':
			return metal_average_production + crystal_average_production * 1.33 + deuterium_average_production * 2
	
	def print_total_production(self, metalized=False):
		metal_production = 0
		crystal_production = 0
		deuterium_production = 0
		
		for planet in self.planets:
			metal_production += production(planet, 'metal', planet.metal, planet.temperature, metalized)
			crystal_production += production(planet, 'crystal', planet.crystal, planet.temperature, metalized)
			deuterium_production += production(planet, 'deuterium', planet.deuterium, planet.temperature, metalized)
		
		metal_average_production = round(metal_production / len(self.planets), 2)
		crystal_average_production = round(crystal_production / len(self.planets), 2)
		deuterium_average_production = round(deuterium_production / len(self.planets), 2)
		
		if metalized:
			print('Production per hour metalized: ' + '{:,}'.format(round(metal_average_production + crystal_average_production + deuterium_average_production)).replace(',', ' ') + 'M')
		else:
			print('Metal production per hour: ' + '{:,}'.format(round(metal_average_production)).replace(',', ' ') + 'M')
			print('Crystal production per hour: ' + '{:,}'.format(round(crystal_average_production)).replace(',', ' ') + 'C')
			print('Deuterium production per hour: ' + '{:,}'.format(round(deuterium_average_production)).replace(',', ' ') + 'D')
	
	
	def get_average_level(self, code):
		code_sum = 0
		
		for planet in self.planets:
			if code == 'metal':
				code_sum += planet.metal
			elif code == 'crystal':
				code_sum += planet.crystal
			elif code == 'deuterium':
				code_sum += planet.deuterium
			elif code == 'solar_plant':
				code_sum += planet.solar_plant
			elif code == 'fusion_reactor':
				code_sum += planet.fusion_reactor
			elif code == 'satellites':
				code_sum += planet.satellites
		
		code_average = round(code_sum / len(self.planets), 2)
		return code_average
	
	
	def pretty(self):
		print('Username: ' + self.username)
		print('---')
		print('Planets: ' + str(len(self.planets)))
		print('Points: ' + str(self.points))
		print('Server Speed: x' + str(self.server_speed))
		print('Astrophysics: ' + str(self.astrophysics))
		print('Plasma: ' + str(self.plasma))
		print('Energy: ' + str(self.energy))
		print('---')
		print('Average Mines and Facilities:')
		
		metal_sum = 0
		crystal_sum = 0
		deuterium_sum = 0
		solar_plant_sum = 0
		satellites_sum = 0
		fusion_reactor_sum = 0
		
		for planet in self.planets:
			metal_sum += planet.metal
			crystal_sum += planet.crystal
			deuterium_sum += planet.deuterium
			solar_plant_sum += planet.solar_plant
			satellites_sum += planet.satellites
			fusion_reactor_sum += planet.fusion_reactor
		
		metal_average = round(metal_sum / len(self.planets), 2)
		crystal_average = round(crystal_sum / len(self.planets), 2)
		deuterium_average = round(deuterium_sum / len(self.planets), 2)
		solar_plant_average = round(solar_plant_sum / len(self.planets), 2)
		satellites_average = round(satellites_sum / len(self.planets), 2)
		fusion_reactor_average = round(fusion_reactor_sum / len(self.planets), 2)
		
		print('Metal: ' + str(metal_average))
		print('Crystal: ' + str(crystal_average))
		print('Deuterium: ' + str(deuterium_average))
		print('Solar Plant: ' + str(solar_plant_average))
		print('Satellites: ' + str(satellites_average))
		print('Fusion Reactor: ' + str(fusion_reactor_average))
