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
