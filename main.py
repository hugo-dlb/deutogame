from lib.player import Player
from lib.planet import Planet

SERVER_ECONOMY_SPEED = 3
SIMULATION_DAY_LENGTH = 30

miz = Player('Miz')
miz.add_planet(Planet(175, -130, SERVER_ECONOMY_SPEED, 'PM'))
miz.add_planet(Planet(175, -130, SERVER_ECONOMY_SPEED, 'P1'))
miz.add_planet(Planet(175, -130, SERVER_ECONOMY_SPEED, 'P2'))

mizerable = Player('Mizerable')
mizerable.add_planet(Planet(175, -130, SERVER_ECONOMY_SPEED, 'PM'))
mizerable.add_planet(Planet(175, -130, SERVER_ECONOMY_SPEED, 'P1'))
mizerable.add_planet(Planet(175, -130, SERVER_ECONOMY_SPEED, 'P2'))

print(miz)
print(mizerable)