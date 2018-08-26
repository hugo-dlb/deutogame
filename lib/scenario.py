class Scenario:
	
	def __init__(self, name, accounts, day_length):
		self.name = name
		self.accounts = accounts
		self.day_length = day_length
		self.started = False
		self.finished = False
		self.current_day = 0
	
	
	def add_account(self, account):
		self.accounts.append(account)
	
	
	def simulate_one_day(self):
		for account in self.accounts:
			for planet in account.planets:
				planet.add_one_day_of_production()
				while planet.can_do_next_most_efficient_step():
					planet.do_next_most_efficient_step()
			day_data = {}
			day_data['day_number'] = self.current_day
			day_data['username'] = account.username
			day_data['points'] = account.points
			day_data['astrophysics'] = account.astrophysics
			day_data['energy'] = account.energy
			day_data['plasma'] = account.plasma
			day_data['average_metal_mines'] = account.get_average_level('metal')
			day_data['average_crystal_mines'] = account.get_average_level('crystal')
			day_data['average_deuterium_mines'] = account.get_average_level('deuterium')
			day_data['average_solar_plant'] = account.get_average_level('solar_plant')
			day_data['average_satellites'] = account.get_average_level('satellites')
			day_data['average_fusion_reactor'] = account.get_average_level('fusion_reactor')
			day_data['metal_production'] = account.get_mine_production('metal')
			day_data['crystal_production'] = account.get_mine_production('crystal')
			day_data['deuterium_production'] = account.get_mine_production('deuterium')
			day_data['production_metalized'] = account.get_mine_production('total')
			account.days_data.append(day_data)
	
	
	def run(self):
		self.started = True
		while self.current_day < self.day_length:
			self.simulate_one_day()
			self.current_day += 1
		self.finished = True
	
	
	def __str__(self):
		return self.name + ', ' + str(len(self.accounts)) + ' accounts' + ', ' + str(self.day_length) + ' day(s)'
	
	
	def pretty(self):
		print('Scenario name: ' + self.name)
		print('Accounts:')
		for account in self.accounts:
			print('- ' + str(account))
		print('Day length: ' + str(self.day_length))
		print('Current day: ' + str(self.current_day))
