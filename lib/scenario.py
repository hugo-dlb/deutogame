class Scenario:
	
	def __init__(self, name='Default scenario', accounts=[], day_length=365):
		self.name = name
		self.accounts = accounts.copy()
		self.day_length = day_length
		self.started = False
		self.finished = False
		self.current_day = 0
	
	
	def add_account(self, account):
		self.accounts.append(account)
	
	
	def run(self):
		self.started = True
		self.current_day = 1
		for account in self.accounts:
			self.simulate_one_day(account)
	
	
	def simulate_one_day(self):
		for account in self.accounts:
			for planet in account.planets:
				planet.add_one_day_of_production()
				# todo refactor, use utils, and finish method
				'''
				while planet.can_afford_next_most_efficient_step:
					planet.do_next_most_efficient_step()
				'''
	
	
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
