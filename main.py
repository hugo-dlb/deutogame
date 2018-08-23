from lib.scenario import Scenario
from lib.playstyle import PlayStyle
from lib.account import Account
from lib.planet import Planet

SERVER_ECONOMY_SPEED = 3
SIMULATION_DAY_LENGTH = 365

miz = Account('Miz')
miz.add_planet(Planet(188, 30, SERVER_ECONOMY_SPEED, 'PM', position=10))
p15_playstyle = PlayStyle('P15 playstyle')
miz.set_playstyle(p15_playstyle)

mizerable = Account('Mizerable')
mizerable.add_planet(Planet(188, 30, SERVER_ECONOMY_SPEED, 'PM', position=10))
regular_playstyle = PlayStyle('Regular playstyle', position=11, position_15_reordering=False)
mizerable.set_playstyle(regular_playstyle)

scenario = Scenario('My scenario', [miz, mizerable], SIMULATION_DAY_LENGTH)
scenario.run()

for account in scenario.accounts:
	print(account)
	for planet in account.planets:
		print(planet.get_next_most_efficient_step())