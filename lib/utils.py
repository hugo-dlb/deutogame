from copy import deepcopy
from math import floor


def get_planet_temperature_by_position(position):
	# returning the average temperature for positions <= 8
	# returning the minimum temperature for positions >= 9
	if position == 1:
		return 240
	elif position == 2:
		return 190
	elif position == 3:
		return 140
	elif position == 4:
		return 90
	elif position == 5:
		return 80
	elif position == 6:
		return 70
	elif position == 7:
		return 60
	elif position == 8:
		return 50
	elif position == 9:
		return 20
	elif position == 10:
		return 10
	elif position == 11:
		return 0
	elif position == 12:
		return -10
	elif position == 13:
		return -50
	elif position == 14:
		return -90
	elif position == 15:
		return -130


def next_level_cost(code, level, metalized=False):
	if metalized:
		if code == 'metal':
			return (60 * pow(1.5, level)) + (15 * pow(1.5, level)) * 1.33
		if code == 'crystal':
			return 48 * (pow(1.6, level)) + 24 * (pow(1.6, level)) * 1.33
		if code == 'deuterium':
			return 225 * pow(1.5, level) + 75 * pow(1.5, level) * 1.33
		if code == 'solar_plant':
			return 75 * pow(1.5, level) + 30 * pow(1.5, level) * 1.33
		if code == 'fusion_reactor':
			return 900 * pow(1.8, level) + 360 * pow(1.8, level) * 1.33 + 180 * pow(1.8, level) * 2
		if code == 'plasma':
			return 2000 * pow(2, level - 1) + 4000 * pow(2, level - 1) * 1.33 + 1000 * pow(2, level - 1) * 2
		if code == 'energy':
			return 0 + 800 * pow(2, level) * 1.33 + 400 * pow(2, level) * 2
	else:
		if code == 'metal':
			return (60 * pow(1.5, level)), (15 * pow(1.5, level)), 0
		if code == 'crystal':
			return 48 * (pow(1.6, level)), 24 * (pow(1.6, level)), 0
		if code == 'deuterium':
			return 225 * pow(1.5, level), 75 * pow(1.5, level), 0
		if code == 'solar_plant':
			return 75 * pow(1.5, level), 30 * pow(1.5, level), 0
		if code == 'fusion_reactor':
			return 900 * pow(1.8, level), 360 * pow(1.8, level), 180 * pow(1.8, level)
		if code == 'plasma':
			return 2000 * pow(2, level - 1), 4000 * pow(2, level - 1), 1000 * pow(2, level - 1)
		if code == 'energy':
			return 0, 800 * pow(2, level), 400 * pow(2, level)


def next_level_benefit(planet, code, metalized=False):
	if code == 'metal':
		return production(planet, code, planet.metal + 1, planet.temperature, metalized) - production(planet, code, planet.metal + 1,
			planet.temperature, metalized)
	if code == 'crystal':
		return production(planet, code, planet.crystal + 1, planet.temperature, metalized) - production(planet, code, planet.crystal + 1,
			planet.temperature, metalized)
	if code == 'deuterium':
		return production(planet, code, planet.deuterium + 1, planet.temperature, metalized) - production(planet, code,
			planet.deuterium + 1, planet.temperature, metalized)
	if code == 'plasma':
		p1 = planet
		p2 = planet.copy()
		p2.account.plasma += 1
		production_p1 = production(planet, 'metal', p1.metal, p1.temperature, True) + production(planet, 'crystal', p1.crystal,
			p1.temperature, True) + production(planet, 'deuterium', p1.deuterium, p1.temperature, True)
		production_p2 = production(planet, 'metal', p2.metal, p2.temperature, True) + production(planet, 'crystal', p2.crystal,
			p2.temperature, True) + production(planet, 'deuterium', p2.deuterium, p2.temperature, True)
		return production_p2 - production_p1


def next_level_profitability_metalized(planet, code):
	if code == 'metal':
		if planet.metal == 0:
			return 1
		else:
			return next_level_cost(code, planet.metal, True) / (
					production(planet, code, planet.metal + 1, planet.temperature, True) - production(planet, code, planet.metal,
				planet.temperature, True))
	if code == 'crystal':
		return next_level_cost(code, planet.crystal, True) / (
				production(planet, code, planet.crystal + 1, planet.temperature, True) - production(planet, code, planet.crystal,
			planet.temperature, True))
	if code == 'deuterium':
		return next_level_cost(code, planet.deuterium, True) / (
				production(planet, code, planet.deuterium + 1, planet.temperature, True) - production(planet, code, planet.deuterium,
			planet.temperature, True))
	if code == 'plasma':
		p2 = deepcopy(planet)
		p2_account = deepcopy(planet.account)
		p2.account = p2_account
		p2.account.plasma += 1
		production_p1_metalized = production(planet, 'metal', planet.metal, planet.temperature, True) + production(planet, 'crystal',
			planet.crystal, planet.temperature, True) + production(planet, 'deuterium', planet.deuterium, planet.temperature, True)
		production_p2_metalized = production(p2, 'metal', p2.metal, p2.temperature, True) + production(p2, 'crystal', p2.crystal,
			p2.temperature, True) + production(p2, 'deuterium', p2.deuterium, p2.temperature, True)
		plasma_cost = next_level_cost('plasma', planet.account.plasma, True)
		return plasma_cost / (production_p2_metalized - production_p1_metalized)


def production(planet, code, mine_level, temperature, metalized=False):
	if metalized:
		if code == 'metal':
			return 30 * (1 + (planet.account.plasma / 100)) * mine_level * pow(1.1,
				mine_level) * planet.account.server_speed if mine_level != 0 else 30 * planet.account.server_speed * (
					1 + (planet.account.plasma / 100))
		if code == 'crystal':
			return 20 * (1 + (planet.account.plasma * 0.0066)) * mine_level * pow(1.1,
				mine_level) * planet.account.server_speed * 1.33 if mine_level != 0 else 15 * planet.account.server_speed * 1.33 * (
					1 + (planet.account.plasma * 0.0066))
		if code == 'deuterium':
			return (((10 * (1 + (planet.account.plasma * 0.0033)) * mine_level * pow(1.1, mine_level)) * (
					-0.004 * temperature + 1.44)) * planet.account.server_speed * 2) - get_fusion_reactor_deuterium_cost_for_level(
				planet.fusion_reactor, planet.account.server_speed)
	else:
		if code == 'metal':
			return (30 * (1 + (planet.account.plasma / 100)) * mine_level * pow(1.1,
				mine_level + 1)) * planet.account.server_speed if mine_level != 0 else 30 * planet.account.server_speed * (
					1 + (planet.account.plasma / 100))
		if code == 'crystal':
			return (20 * (1 + (planet.account.plasma * 0.0066)) * mine_level * pow(1.1,
				mine_level)) * planet.account.server_speed if mine_level != 0 else 15 * planet.account.server_speed * (
					1 + (planet.account.plasma * 0.0066))
		if code == 'deuterium':
			return (((10 * (1 + (planet.account.plasma * 0.0033)) * mine_level * pow(1.1, mine_level)) * (
					-0.004 * temperature + 1.44)) * planet.account.server_speed) - get_fusion_reactor_deuterium_cost_for_level(
				planet.fusion_reactor, planet.account.server_speed)


def next_astrophysics_cost(level, metalized=False):
	a = 4000
	b = a * 2
	
	if level == 0:
		if metalized:
			return a + b * 1.33 + a * 2
		else:
			return a, b, a
	
	for i in range(1, level + 1):
		a = a * 1.75
	for i in range(1, level + 2):
		b = b * 1.75
	metal = a
	crystal = b
	deuterium = a
	a = 4000
	b = a * 2
	for i in range(1, level + 2):
		a = a * 1.75
	for i in range(1, level + 1):
		b = b * 1.75
	metal += a
	crystal += b
	deuterium += a
	
	if metalized:
		return metal + crystal * 1.33 + deuterium * 2
	else:
		return metal, crystal, deuterium


def get_mine_energy_consumption(code, mine_level):
	if code == 'metal':
		return 10 * mine_level * pow(1.1, mine_level)
	if code == 'crystal':
		return 10 * mine_level * pow(1.1, mine_level)
	if code == 'deuterium':
		return 20 * mine_level * pow(1.1, mine_level)


def get_solar_plant_energy_for_level(solar_plant_level):
	return 20 * solar_plant_level * pow(1.1, solar_plant_level)


def get_fusion_reactor_energy_for_level(fusion_reactor_level, energy_level):
	# todo investigate results to validate formula
	return 30 * fusion_reactor_level * pow((1.05 + (0.01 * energy_level)), fusion_reactor_level)


def get_fusion_reactor_deuterium_cost_for_level(fusion_reactor_level, server_speed):
	return floor(-10 * fusion_reactor_level * pow(1.1, fusion_reactor_level) * server_speed)


def energy_over_fusion_reactor(planet):
	energy_cost = next_level_cost('energy', planet.account.energy, True) / len(planet.account.planets)
	energy_profit = get_fusion_reactor_energy_for_level(planet.fusion_reactor, planet.account.energy + 1) - get_fusion_reactor_energy_for_level(
		planet.fusion_reactor, planet.account.energy)
	if energy_profit == 0:
		energy_profit = 1
	energy_upgrade_ratio = energy_cost / energy_profit
	
	fusion_reactor_cost = next_level_cost('fusion_reactor', planet.fusion_reactor, True)
	fusion_reactor_profit = get_fusion_reactor_energy_for_level(planet.fusion_reactor + 1, planet.account.energy) - get_fusion_reactor_energy_for_level(planet.fusion_reactor, planet.account.energy)
	fusion_reactor_upgrade_ratio = fusion_reactor_cost / fusion_reactor_profit
	
	return energy_upgrade_ratio <= fusion_reactor_upgrade_ratio

def get_average_planets_production_per_hour(planets):
	total_production_metalized = 0
	
	for planet in planets:
		total_production_metalized += (
				production(planet, 'metal', planet.metal, planet.temperature, True) + production(planet, 'crystal', planet.crystal,
			planet.temperature, True) + production(planet, 'deuterium', planet.deuterium, planet.temperature, True))
	
	return total_production_metalized / len(planets)


def astrophysics_over_task_benneb(task_production_gain_per_hour_metalized, astrophysics_total_cost_metalized, mine_cost_metalized,
		average_production_per_planet_per_hour_metalized):
	return (task_production_gain_per_hour_metalized * astrophysics_total_cost_metalized) <= (
			mine_cost_metalized * average_production_per_planet_per_hour_metalized)


def astrophysics_over_task(task_production_gain_per_hour_metalized, astrophysics_total_cost_metalized, mine_cost_metalized,
		average_production_per_planet_per_hour_metalized):
	return (astrophysics_total_cost_metalized / average_production_per_planet_per_hour_metalized) <= (
			mine_cost_metalized / task_production_gain_per_hour_metalized)
