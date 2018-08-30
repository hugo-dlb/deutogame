from lib.scenario import Scenario
from lib.playstyle import PlayStyle
from lib.account import Account
from lib.renderer import Renderer
from lib.planet import Planet
from lib.utils import *
import cProfile

SERVER_ECONOMY_SPEED = 3
SIMULATION_DAY_LENGTH = 300

p15_playstyle = PlayStyle('P15 playstyle', 15, False, 7)
mizerable = Account('P15 (' + str(get_planet_temperature_by_position(15)) + '°)', SERVER_ECONOMY_SPEED, [], p15_playstyle)
p1 = Planet('PM', 188, get_planet_temperature_by_position(15), 15, mizerable)
mizerable.planets.append(p1)

p14_playstyle = PlayStyle('P14 playstyle', 14, False, 7)
microwave = Account('P14 (' + str(get_planet_temperature_by_position(14)) + '°)', SERVER_ECONOMY_SPEED, [], p14_playstyle)
p2 = Planet('PM', 188, get_planet_temperature_by_position(14), 14, microwave)
microwave.planets.append(p2)

p13_playstyle = PlayStyle('P13 playstyle', 13, False, 7)
p14acc = Account('P13 (' + str(get_planet_temperature_by_position(13)) + '°)', SERVER_ECONOMY_SPEED, [], p13_playstyle)
p3 = Planet('PM', 188, get_planet_temperature_by_position(13), 13, p14acc)
p14acc.planets.append(p3)

p10_playstyle = PlayStyle('P10 playstyle', 10, False, 7)
miz = Account('P10 (' + str(get_planet_temperature_by_position(10)) + '°)', SERVER_ECONOMY_SPEED, [], p10_playstyle)
p4 = Planet('PM', 188, get_planet_temperature_by_position(10), 10, miz)
miz.planets.append(p4)

accounts = [mizerable, microwave, p14acc, miz]

scenario = Scenario('P15 vs P14 vs P10', accounts, SIMULATION_DAY_LENGTH)
scenario.run()

renderer = Renderer()
renderer.display_scenario(scenario)