def next_level_cost(code, level, metalized=False):
	if metalized:
		if code == 'metal':
			return round((60 * pow(1.5, level))) + round((15 * pow(1.5, level)) * 1.33)
		if code == 'cristal':
			return round(48 * (pow(1.6, level))) + round(24 * (pow(1.6, level)) * 1.33)
		if code == 'deuterium':
			return round(225 * pow(1.5, level)) + round(75 * pow(1.5, level) * 1.33)
		if code == 'solar_plant':
			return round(75 * pow(1.5, level)) + round(30 * pow(1.5, level) * 1.33)
		if code == 'fusion_reactor':
			return round(900 * pow(1.8, level)) + round(360 * pow(1.8, level) * 1.33) + round(180 * pow(1.8, level) * 2)
	else:
		if code == 'metal':
			return round((60 * pow(1.5, level))), round((15 * pow(1.5, level))), 0
		if code == 'cristal':
			return round(48 * (pow(1.6, level))), round(24 * (pow(1.6, level))), 0
		if code == 'deuterium':
			return round(225 * pow(1.5, level)), round(75 * pow(1.5, level)), 0
		if code == 'solar_plant':
			return round(75 * pow(1.5, level)), round(30 * pow(1.5, level)), 0
		if code == 'fusion_reactor':
			return round(900 * pow(1.8, level)), round(360 * pow(1.8, level)), round(180 * pow(1.8, level))


def next_level_benefit(planet, code, metalized=False):
	if code == 'metal':
		return production(planet, code, planet.metal + 1, planet.temperature, metalized) - production(planet, code, planet.metal + 1,
			planet.temperature, metalized)
	if code == 'cristal':
		return production(planet, code, planet.cristal + 1, planet.temperature, metalized) - production(planet, code, planet.cristal + 1,
			planet.temperature, metalized)
	if code == 'deuterium':
		return production(planet, code, planet.deuterium + 1, planet.temperature, metalized) - production(planet, code,
			planet.deuterium + 1, planet.temperature, metalized)


def next_level_profitability_metalized(planet, code):
	if code == 'metal':
		return round(next_level_cost(code, planet.metal, True) / (
				production(planet, code, planet.metal + 1, planet.temperature, True) - production(planet, code, planet.metal,
			planet.temperature, True)), 2)
	if code == 'cristal':
		return round(next_level_cost(code, planet.cristal, True) / (
				production(planet, code, planet.cristal + 1, planet.temperature, True) - production(planet, code, planet.cristal,
			planet.temperature, True)), 2)
	if code == 'deuterium':
		return round(next_level_cost(code, planet.deuterium, True) / (
				production(planet, code, planet.deuterium + 1, planet.temperature, True) - production(planet, code, planet.deuterium,
			planet.temperature, True)), 2)


def production(planet, code, mine_level, temperature, metalized=False):
	if metalized:
		if code == 'metal':
			return round(30 * mine_level * pow(1.1, mine_level) * planet.server_speed) if mine_level != 0 else 30 * planet.server_speed
		if code == 'cristal':
			return round(
				20 * mine_level * pow(1.1, mine_level) * planet.server_speed * 1.33) if mine_level != 0 else 15 * planet.server_speed
		if code == 'deuterium':
			return round(((10 * mine_level * pow(1.1, mine_level)) * (-0.004 * temperature + 1.44)) * planet.server_speed * 2)
	else:
		if code == 'metal':
			return round(
				(30 * mine_level * pow(1.1, mine_level + 1)) * planet.server_speed) if mine_level != 0 else 30 * planet.server_speed
		if code == 'cristal':
			return round((20 * mine_level * pow(1.1, mine_level)) * planet.server_speed) if mine_level != 0 else 15 * planet.server_speed
		if code == 'deuterium':
			return round(((10 * mine_level * pow(1.1, mine_level)) * (-0.004 * temperature + 1.44)) * planet.server_speed)


def next_astrophysics_cost(level, metalized=False):
	a = 4000
	b = a * 2
	
	if level == 0:
		if metalized:
			return round(a) + round(b * 1.33) + round(a * 2)
		else:
			return round(a), round(b), round(a)
	
	for i in range(1, level + 1):
		a = a * 1.75
	for i in range(1, level + 2):
		b = b * 1.75
	metal = a
	cristal = b
	deuterium = a
	a = 4000
	b = a * 2
	for i in range(1, level + 2):
		a = a * 1.75
	for i in range(1, level + 1):
		b = b * 1.75
	metal += a
	cristal += b
	deuterium += a
	
	if metalized:
		return round(metal) + round(cristal * 1.33) + round(deuterium * 2)
	else:
		return round(metal), round(cristal), round(deuterium)


def astrophysics_over_mine(mine_production_gain_per_hour_metalized, astro_total_cost_metalized, mine_cost_metalized,
		average_production_per_planet_per_hour_metalized):
	return (mine_production_gain_per_hour_metalized * astro_total_cost_metalized) <= (
			mine_cost_metalized * average_production_per_planet_per_hour_metalized)
