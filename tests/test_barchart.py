import unittest
import sys
import os

sys.path.append('/..')

import simplyplot


class TestBarChart(unittest.TestCase):

    options = {
        'title': 'Sales 2005 - 2008',
        'x_axis_name': 'Month',
        'y_axis_name': 'Sales',
        'data': [2000, 1500, 2250, 1750],
        'labels': ['2005', '2006', '2007', '2008']
    }

    chart = simplyplot.BarChart(**options)

    def test_chart_attributes(self):
        self.assertEqual(str, type(self.chart.title))
        self.assertEqual(str, type(self.chart.x_axis_name))
        self.assertEqual(str, type(self.chart.y_axis_name))
        self.assertEqual(list, type(self.chart.data))
        self.assertEqual(list, type(self.chart.labels))

    def test_get_bar_positions(self):
        result = self.chart.get_bar_positions(
            self.chart.data,
            self.chart.bar_width,
            self.chart.bar_spacing
        )
        self.assertEqual(list, type(result))


if __name__ == '__main__':
    unittest.main()
