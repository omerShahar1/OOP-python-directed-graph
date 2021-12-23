from unittest import TestCase

from GraphAlgo import GraphAlgo
from GraphInterface import GraphInterface


class TestGraphAlgo(TestCase):
    algo = GraphAlgo(GraphInterface())

    def test_get_graph(self):
        self.algo.load_from_json("../data/A0.json")
        self.fail()

    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        self.fail()

    def test_tsp(self):
        self.fail()

    def test_center_point(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()
