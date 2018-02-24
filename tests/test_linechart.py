import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../simply_plot")

import simply_plot

class TestChart(unittest.TestCase):
    options = {
    	'title': 'Sales 2005 - 2008',
    	'x_axis_name': 'Month',
    	'y_axis_name': 'Sales',
    	'data': [(1, 2, 4, 8), (3, 6, 12, 24)],
    	'labels': ('2005', '2006', '2007', '2008')
    }

    chart = simply_plot.LineChart(**options)

    def test_chart_attributes(self):
        self.assertEqual(str, type(self.chart.title), msg="The 'title' attribute was not a string")
        self.assertEqual(str, type(self.chart.x_axis_name), msg="The 'x_axis_name' attribute was not a string")
        self.assertEqual(str, type(self.chart.y_axis_name), msg="The 'y_axis_name' attribute was not a string")
        self.assertEqual(list, type(self.chart.data), msg="The 'data' attribute was not a tuple or a list")
        self.assertEqual(list, type(self.chart.labels), msg="The 'labels' attribute was not a tuple or a list")

if __name__ == '__main__':
    unittest.main()
