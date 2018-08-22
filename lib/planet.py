class Planet:
	
	def __init__(self, diameter, temperature, server_speed = 1, name = 'Colony', position = 15, metal = 0, cristal = 0, deuterium = 0, points = 0):
		self.server_speed = server_speed
		self.name = name
		self.diameter = diameter
		self.temperature = temperature
		self.position = position
		self.metal = metal
		self.cristal = cristal
		self.deuterium = deuterium
		self.points = points
	
	
	def next_level_cost_by_code(self, mine_code):
		if(mine_code == 'metal'):
			return self.next_level_cost_by_level('metal', self.metal)
		if(mine_code == 'cristal'):
			return self.next_level_cost_by_level('cristal', self.cristal)
		if(mine_code == 'deuterium'):
			return self.next_level_cost_by_level('deuterium', self.deuterium)
	
	
	def next_level_cost_by_level(self, mine_code, level):
		if(mine_code == 'metal'):
			return round((60*pow(1.5,level))),round((15*pow(1.5,level)))
		if(mine_code == 'cristal'):
			return round(48*(pow(1.6,level))),round(24*(pow(1.6,level)))
		if(mine_code == 'deuterium'):
			return round(225*pow(1.5,level)),round(75*pow(1.5,level))
	
	
	def next_level_cost_by_level_metalized(self, mine_code, level):
		if(mine_code == 'metal'):
			return round((60*pow(1.5,level)))+round((15*pow(1.5,level))*1.33)
		if(mine_code == 'cristal'):
			return round(48*(pow(1.6,level)))+round(24*(pow(1.6,level))*1.33)
		if(mine_code == 'deuterium'):
			return round(225*pow(1.5,level))+round(75*pow(1.5,level)*1.33)
	
	
	def next_level_benefit(self, mine_code):
		if(mine_code == 'metal'):
			return next_level_benefit('metal', self.metal, self.temperature)
		if(mine_code == 'cristal'):
			return next_level_benefit('cristal', self.cristal, self.temperature)
		if(mine_code == 'deuterium'):
			return next_level_benefit('deuterium', self.deuterium, self.temperature)
	
	
	def next_level_profitability(self, mine_code):
		if(mine_code == 'metal'):
			return round(next_level_cost(mine_code, self.metal) / (production(mine_code, self.metal + 1,
			self.temperature, None) - production(mine_code, self.metal, self.temperature, None)))
		if(mine_code == 'cristal'):
			return round(next_level_cost(mine_code, self.cristal) / (production(mine_code, self.cristal + 1,
			self.temperature, None) - production(mine_code, self.cristal, self.temperature, None)))
		if(mine_code == 'deuterium'):
			return round(next_level_cost(mine_code, self.deuterium) / (production(mine_code, self.deuterium + 1,
			self.temperature, None) - production(mine_code, self.deuterium, self.temperature, None)))
	
	
	def production(mine_code, mine_level, temperature, metalized = False):
		if metalized:
			if (mine_code == 'metal'):
				return round(30 * mine_level * pow(1.1, mine_level) * self.server_speed)
			if (mine_code == 'cristal'):
				return round(20 * mine_level * pow(1.1, mine_level) * self.server_speed * 1.33)
			if (mine_code == 'deuterium'):
				return round(((10 * mine_level * pow(1.1, mine_level)) * (-0.004 * temperature + 1.44)) * self.server_speed * 2)
		else:
			if (mine_code == 'metal'):
				return round(30 * mine_level * pow(1.1, mine_level + 1) * self.server_speed)
			if (mine_code == 'cristal'):
				return round(20 * mine_level * pow(1.1, mine_level) * self.server_speed)
			if (mine_code == 'deuterium'):
				return round(((10 * mine_level * pow(1.1, mine_level)) * (-0.004 * temperature + 1.44)) * self.server_speed)
	
	
	def __str__(self):
		return self.name + ', ' + str(self.diameter) + ' cells, ' + 'position ' + str(self.position) + ', ' + str(self.temperature) + '°, M' + str(self.metal) + ', C' + str(self.cristal) + ', D' + str(self.deuterium)