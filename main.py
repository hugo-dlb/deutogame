from lib.scenario import Scenario
from lib.playstyle import PlayStyle
from lib.account import Account
from lib.planet import Planet
from lib.utils import next_astrophysics_cost
'''
SERVER_ECONOMY_SPEED = 3
SIMULATION_DAY_LENGTH = 365

miz = Account('Miz')
miz.add_planet(Planet(188, 30, SERVER_ECONOMY_SPEED, 'PM', position=10))
p15_playstyle = PlayStyle('P15 playstyle')
miz.playstyle = p15_playstyle

mizerable = Account('Mizerable')
regular_playstyle = PlayStyle('Regular playstyle', position=11, position_15_reordering=False)
mizerable.playstyle = regular_playstyle
mizerable.add_planet(Planet(188, 30, SERVER_ECONOMY_SPEED, 'PM', position=10, account=mizerable))

scenario = Scenario('My scenario', [miz, mizerable], SIMULATION_DAY_LENGTH)
scenario.run()

for account in scenario.accounts:
	print(account)
	for planet in account.planets:
		print(planet.get_next_most_efficient_step())
'''
print(next_astrophysics_cost(0, True))
print(next_astrophysics_cost(1, True))
print(next_astrophysics_cost(3, True))