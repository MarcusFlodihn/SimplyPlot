import unittest
import sys
import os

sys.path.append('/..')

import simplyplot

class TestLineChart(unittest.TestCase):
    options = {
    	'title': 'Sales 2005 - 2008',
    	'x_axis_name': 'Month',
    	'y_axis_name': 'Sales',
    	'data': [(1, 2, 4, 8), (3, 6, 12, 24)],
    	'labels': ('2005', '2006', '2007', '2008')
    }

    chart = simplyplot.Chart2D(**options)

    def test_chart_attributes(self):
        self.assertEqual(str, type(self.chart.title))
        self.assertEqual(str, type(self.chart.x_axis_name))
        self.assertEqual(str, type(self.chart.y_axis_name))
        self.assertEqual(list, type(self.chart.data))
        self.assertEqual(list, type(self.chart.labels))

if __name__ == '__main__':
    unittest.main()
