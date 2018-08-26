from lib.scenario import Scenario
from lib.playstyle import PlayStyle
from lib.account import Account
from lib.renderer import Renderer
from lib.planet import Planet
from lib.utils import *

SERVER_ECONOMY_SPEED = 3
SIMULATION_DAY_LENGTH = 730

p15_playstyle = PlayStyle('P15 playstyle', 15, False, 7)
mizerable = Account('P15 (' + str(get_planet_temperature_by_position(15)) + '°)', SERVER_ECONOMY_SPEED, [], p15_playstyle)
p1 = Planet('PM', 188, get_planet_temperature_by_position(15), 15, mizerable)
mizerable.planets.append(p1)

normal_playstyle = PlayStyle('P10 playstyle', 10, False, 7)
miz = Account('P10 (' + str(get_planet_temperature_by_position(10)) + '°)', SERVER_ECONOMY_SPEED, [], normal_playstyle)
p2 = Planet('PM', 188, get_planet_temperature_by_position(10), 10, miz)
miz.planets.append(p2)

normal_playstyle = PlayStyle('P6 playstyle', 6, False, 7)
microwave = Account('P6 (' + str(get_planet_temperature_by_position(6)) + '°)', SERVER_ECONOMY_SPEED, [], normal_playstyle)
p2 = Planet('PM', 188, get_planet_temperature_by_position(6), 6, microwave)
microwave.planets.append(p2)

scenario = Scenario('P15 vs P10', [mizerable, miz, microwave], SIMULATION_DAY_LENGTH)
scenario.run()

renderer = Renderer()
renderer.display_scenario(scenario)