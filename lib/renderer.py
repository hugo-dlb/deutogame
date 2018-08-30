from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import WheelZoomTool

class Renderer:
	
	
	def display_scenario(self, scenario):
		
		print('Rendering started...')
		
		sources = []
		
		for account in scenario.accounts:
			days = []
			username = []
			points = []
			astrophysics = []
			energy = []
			plasma = []
			average_metal_mines = []
			average_crystal_mines = []
			average_deuterium_mines = []
			average_solar_plant = []
			average_satellites = []
			average_fusion_reactor = []
			metal_production = []
			crystal_production = []
			deuterium_production = []
			production_metalized = []
			
			for day in account.days_data:
				days.append(day['day_number'])
				username.append(day['username'])
				points.append(day['points'])
				astrophysics.append(day['astrophysics'])
				energy.append(day['energy'])
				plasma.append(day['plasma'])
				average_metal_mines.append(day['average_metal_mines'])
				average_crystal_mines.append(day['average_crystal_mines'])
				average_deuterium_mines.append(day['average_deuterium_mines'])
				average_solar_plant.append(day['average_solar_plant'])
				average_satellites.append(day['average_satellites'])
				average_fusion_reactor.append(day['average_fusion_reactor'])
				metal_production.append(day['metal_production'])
				crystal_production.append(day['crystal_production'])
				deuterium_production.append(day['deuterium_production'])
				production_metalized.append(day['production_metalized'])
	
			output_file('./scenarios/' + scenario.name + '.html')
			
			source = ColumnDataSource(data=dict(
				x=days,
				y=points,
				day_number=days,
				username=username,
				points=points,
				astrophysics=astrophysics,
				energy=energy,
				plasma=plasma,
				average_metal_mines=average_metal_mines,
				average_crystal_mines=average_crystal_mines,
				average_deuterium_mines=average_deuterium_mines,
				average_solar_plant=average_solar_plant,
				average_satellites=average_satellites,
				average_fusion_reactor=average_fusion_reactor,
				metal_production=metal_production,
				crystal_production=crystal_production,
				deuterium_production=deuterium_production,
				production_metalized=production_metalized
			))
			
			sources.append([account.username, source])
		
		TOOLTIPS = [
			('Day', '@day_number'),
			('Username', '@username'),
			('Points', '@points{0,0.00}'),
			('Astrophysics', '@astrophysics'),
			('Energy', '@energy'),
			('Plasma', '@plasma'),
			('-', '-'),
			('Avg. Metal', '@average_metal_mines'),
			('Avg. Crystal', '@average_crystal_mines'),
			('Avg. Deuterium', '@average_deuterium_mines'),
			('-', '-'),
			('Avg. Solar Plant', '@average_solar_plant'),
			('Avg. Satellites', '@average_satellites{0,0.00}'),
			('Avg. Fusion Reactor', '@average_fusion_reactor'),
			('-', '-'),
			('Metal Prod.', '@metal_production{0,0.00}'),
			('Crystal Prod.', '@crystal_production{0,0.00}'),
			('Deuterium Prod.', '@deuterium_production{0,0.00}'),
			('-', '-'),
			("Total Prod. 'Metalized'", '@production_metalized{0,0.00}'),
		]
		
		max_points = 0
		for account in scenario.accounts:
			if account.points > max_points:
				max_points = account.points

		p = figure(plot_width=1600, plot_height=800, tooltips=TOOLTIPS, title=scenario.name, x_axis_label='Days', y_axis_label='Points', x_range=(0, scenario.day_length), y_range=(0, max_points))
		p.toolbar.active_scroll = p.select_one(WheelZoomTool)
		
		line_colors = ['lightblue', 'red', 'yellow', 'black', 'brown']
		
		i = 0
		for source in sources:
			p.line('x', 'y', source=source[1], legend=source[0], line_width=3, line_color=line_colors[i])
			i += 1

		show(p)
		print('Done.')