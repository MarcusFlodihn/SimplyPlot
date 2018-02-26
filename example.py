import simplyplot

options = {
	'title': 'Sales 2005 - 2008',
	'x_axis_name': 'Month',
	'y_axis_name': 'Sales',
	'data': [500, 1000, 1250, 1750],
	'labels': ['2005', '2006', '2007', '2008']
}

my_chart = simplyplot.BarChart(**options)

my_chart.show()
