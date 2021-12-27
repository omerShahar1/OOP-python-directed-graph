from unittest import TestCase

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    algo = GraphAlgo(DiGraph())

    def test_get_graph(self):
        test1 = self.algo.get_graph()
        self.algo.load_from_json("../data/A0.json")
        test2 = self.algo.get_graph()
        self.assertNotEqual(test1, test2)

    def test_load_from_json(self):
        self.algo.load_from_json("../data/A1.json")
        test1 = self.algo.get_graph()
        self.algo.load_from_json("../data/A0.json")
        test2 = self.algo.get_graph()
        self.assertNotEqual(test1, test2)

    def test_save_to_json(self):
        self.algo.load_from_json("../data/A1.json")
        test1 = self.algo.get_graph()
        self.algo.save_to_json("test")
        self.algo.load_from_json("test")
        test2 = self.algo.get_graph()
        self.assertEqual(test1.e_size(), test2.e_size())
        self.assertEqual(test1.v_size(), test2.v_size())
        self.assertEqual(test1.get_mc(), test2.get_mc())
        self.assertNotEqual(test1, test2)

    def test_shortest_path(self):
        self.algo.get_graph().add_node(0)
        self.algo.get_graph().add_node(1)
        self.algo.get_graph().add_node(2)
        self.algo.get_graph().add_node(3)
        self.assertEqual(self.algo.shortest_path(0, 1)[0], float('inf'))
        self.algo.get_graph().add_edge(0, 2, 5)
        self.algo.get_graph().add_edge(2, 1, 5)
        self.assertEqual(self.algo.shortest_path(0, 1)[0], 10)

    def test_tsp(self):
        self.assertEqual(self.algo.TSP([1, 2, 4]), [[1, 2, 3, 4], 4.5])

    def test_center_point(self):
        self.algo.graph.add_node(0, (1, 2, 3))
        self.algo.graph.add_node(1, (1, 2, 3))
        self.algo.graph.add_node(2, (1, 2, 3))
        self.algo.graph.add_node(3, (1, 2, 3))
        self.algo.graph.add_node(4, (1, 2, 3))
        self.algo.graph.add_edge(0, 1, 1)
        self.algo.graph.add_edge(3, 0, 3)
        self.algo.graph.add_edge(0, 2, 2)
        self.algo.graph.add_edge(1, 3, 4)
        self.algo.graph.add_edge(4, 1, 3)
        self.algo.graph.add_edge(3, 4, 2)
        self.algo.graph.add_edge(2, 3, 3)
        self.assertEqual(self.algo.centerPoint(), (3, 5))

    def test_plot_graph(self):
        self.algo.load_from_json("../data/A1.json")
        self.algo.plot_graph()

    def test_shortest_path_for_center(self):
        self.fail()

    def test_find_next_node(self):
        self.fail()
