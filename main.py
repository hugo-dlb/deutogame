from lib.scenario import Scenario
from lib.playstyle import PlayStyle
from lib.player import Player
from lib.planet import Planet

SERVER_ECONOMY_SPEED = 3
SIMULATION_DAY_LENGTH = 365

miz = Player('Miz')
miz.add_planet(Planet(175, -130, SERVER_ECONOMY_SPEED, 'PM'))
miz.add_planet(Planet(175, -130, SERVER_ECONOMY_SPEED, 'P1'))
miz.add_planet(Planet(175, -130, SERVER_ECONOMY_SPEED, 'P2'))
p15_playstyle = PlayStyle('P15 playstyle', position=11)
miz.set_playstyle(p15_playstyle)

mizerable = Player('Mizerable')
mizerable.add_planet(Planet(175, -130, SERVER_ECONOMY_SPEED, 'PM'))
mizerable.add_planet(Planet(175, -130, SERVER_ECONOMY_SPEED, 'P1'))
mizerable.add_planet(Planet(175, -130, SERVER_ECONOMY_SPEED, 'P2'))
regular_playstyle = PlayStyle('Regular playstyle', position=11, position_15_reordering=False)
mizerable.set_playstyle(regular_playstyle)

scenario = Scenario('My scenario', [miz, mizerable], SIMULATION_DAY_LENGTH)

print(scenario)