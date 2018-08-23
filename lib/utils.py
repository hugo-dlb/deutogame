def next_level_cost(code, level, metalized=False):
	if metalized:
		if code == 'metal':
			return round((60 * pow(1.5, level))) + round((15 * pow(1.5, level)) * 1.33)
		if code == 'cristal':
			return round(48 * (pow(1.6, level))) + round(24 * (pow(1.6, level)) * 1.33)
		if code == 'deuterium':
			return round(225 * pow(1.5, level)) + round(75 * pow(1.5, level) * 1.33)
		if code == 'solar_plant':
			return round(75 * pow(1.5, level- 1)) + round(30 * pow(1.5, level - 1) * 1.33)
		if code == 'fusion_reactor':
			return round(900 * pow(1.8, level - 1)) + round(360 * pow(1.8, level - 1) * 1.33) + round(180 * pow(1.8, level - 1) * 2)
	else:
		if code == 'metal':
			return round((60 * pow(1.5, level))), round((15 * pow(1.5, level))), 0
		if code == 'cristal':
			return round(48 * (pow(1.6, level))), round(24 * (pow(1.6, level))), 0
		if code == 'deuterium':
			return round(225 * pow(1.5, level)), round(75 * pow(1.5, level)), 0
		if code == 'solar_plant':
			return round(75 * pow(1.5, level - 1)), round(30 * pow(1.5, level - 1)), 0
		if code == 'fusion_reactor':
			return round(900 * pow(1.8, level - 1)), round(360 * pow(1.8, level - 1)), round(180 * pow(1.8, level - 1))


def next_level_benefit(planet, code, metalized=False):
	if code == 'metal':
		return production(planet, code, planet.metal + 1, planet.temperature, metalized) - production(planet, code, planet.metal + 1, planet.temperature, metalized)
	if code == 'cristal':
		return production(planet, code, planet.cristal + 1, planet.temperature, metalized) - production(planet, code, planet.cristal + 1, planet.temperature, metalized)
	if code == 'deuterium':
		return production(planet, code, planet.deuterium + 1, planet.temperature, metalized) - production(planet, code, planet.deuterium + 1, planet.temperature, metalized)


def next_level_profitability_metalized(planet, code):
	if code == 'metal':
		return round(next_level_cost_by_level(code, planet.metal, True) / (
				production(planet, code, planet.metal + 1, planet.temperature, True) - production(planet, code, planet.metal,
			planet.temperature, True)))
	if code == 'cristal':
		return round(next_level_cost_by_level(code, planet.cristal, True) / (
				production(planet, code, planet.cristal + 1, planet.temperature, True) - production(planet, code, planet.cristal,
			planet.temperature, True)))
	if code == 'deuterium':
		return round(next_level_cost_by_level(code, planet.deuterium, True) / (
				production(planet, code, planet.deuterium + 1, planet.temperature, True) - production(planet, code, planet.deuterium,
			planet.temperature, True)))


def production(planet, code, mine_level, temperature, metalized=False):
	if metalized:
		if code == 'metal':
			return round(30 * mine_level * pow(1.1, mine_level) * planet.server_speed + 30 * planet.server_speed)
		if code == 'cristal':
			return round(20 * mine_level * pow(1.1, mine_level) * planet.server_speed * 1.33 + 15 * planet.server_speed)
		if code == 'deuterium':
			return round(((10 * mine_level * pow(1.1, mine_level)) * (-0.004 * temperature + 1.44)) * planet.server_speed * 2)
	else:
		if code == 'metal':
			return round(30 * mine_level * pow(1.1, mine_level + 1) * planet.server_speed)
		if code == 'cristal':
			return round(20 * mine_level * pow(1.1, mine_level) * planet.server_speed)
		if code == 'deuterium':
			return round(((10 * mine_level * pow(1.1, mine_level)) * (-0.004 * temperature + 1.44)) * planet.server_speed)


def next_astrophysics_cost(level, metalized=False):
	a = 4000
	b = a * 2
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


def get_next_most_efficient_step(account, planet):
	# todo
	astro_cost_metalized = next_astrophysics_cost(account.astrophysics, True)
	metal_cost_metalized = next_level_cost('metal', planet.metal, True)
	cristal_cost_metalized = next_level_cost('cristal', planet.cristal, True)
	deuterium_cost_metalized = next_level_cost('deuterium', planet.deuterium, True)