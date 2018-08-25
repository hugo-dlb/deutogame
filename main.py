from lib.scenario import Scenario
from lib.playstyle import PlayStyle
from lib.account import Account
from lib.planet import Planet
from lib.utils import *

SERVER_ECONOMY_SPEED = 3
SIMULATION_DAY_LENGTH = 365

p15_playstyle = PlayStyle('P15 playstyle', 15, False, 7)
mizerable = Account('Mizerable', SERVER_ECONOMY_SPEED, [], p15_playstyle)
p1 = Planet('PM', 188, -130, 15, mizerable)
mizerable.planets.append(p1)

normal_playstyle = PlayStyle('Normal playstyle', 10, False, 7)
miz = Account('Miz', SERVER_ECONOMY_SPEED, [], normal_playstyle)
p2 = Planet('PM', 188, 30, 10, miz)
miz.planets.append(p2)

scenario = Scenario('My scenario', [miz, mizerable], SIMULATION_DAY_LENGTH)
scenario.run()

for account in scenario.accounts:
	account.pretty()