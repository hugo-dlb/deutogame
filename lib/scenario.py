class Scenario:
	
	def __init__(self, name='Default scenario', players=[], day_length=365): 
		self.name = name
		self.players = players.copy()
		self.day_length = day_length
		self.started = False
		self.finished = False
		self.current_day = 0
	
	
	def add_player(self, player):
		self.players.append(player)
	
	
	def run(self):
		self.started = True
		self.current_day = 1
		for player in self.players:
			self.simulate_one_day(player)
	
	
	def simulate_one_day(self, player):
		for planet in player.planets:
			''' todo:
			planet.add_one_day_of_production
			while planet.can_afford_next_most_efficient_step:
				planet.do_next_most_efficient_step()
			'''
	
	
	
	def __str__(self):
		return self.name + ', ' + str(len(self.players)) + ' players' + ', ' + str(self.day_length) + ' day(s)'