class Account:
	
	def __init__(self, username, server_speed, planets, playstyle):
		self.username = username
		self.server_speed = server_speed
		self.astrophysics = 0
		self.energy = 0
		self.plasma = 0
		self.points = 0
		self.resources = 0
		self.planets = planets.copy()
		self.playstyle = playstyle
	
	
	def __str__(self):
		return self.username + ', ' + str(len(self.planets)) + ' planets, ' + str(self.points) + ' points, x' + str(
			self.server_speed) + ' server speed, astrophysics ' + str(self.astrophysics) + ' plasma ' + str(self.plasma) + ' energy ' + str(
			self.energy)
	
	
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
