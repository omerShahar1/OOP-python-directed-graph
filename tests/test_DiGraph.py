from unittest import TestCase
from DiGraph import DiGraph


class TestDiGraph(TestCase):
    graph = DiGraph()

    def test_v_size(self):
        size1 = self.graph.v_size()
        self.graph.add_node(1)
        size2 = self.graph.v_size()
        self.graph.add_node(1, (1, 2, 3))
        size3 = self.graph.v_size()
        self.assertEqual(size1+1, size2)
        self.assertEqual(size2, size3)

    def test_e_size(self):
        size1 = self.graph.e_size()
        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_edge(1, 2, 10)
        size2 = self.graph.e_size()
        self.assertEqual(size1 + 1, size2)

        self.graph.add_edge(1, 2, 20)
        size3 = self.graph.e_size()
        self.assertEqual(size2, size3)

        self.graph.add_edge(7000, 0, 20)
        size4 = self.graph.e_size()
        self.assertEqual(size3, size4)

    def test_get_all_v(self):
        self.fail()

    def test_all_in_edges_of_node(self):
        self.fail()

    def test_all_out_edges_of_node(self):
        self.fail()

    def test_get_mc(self):
        mc1 = self.graph.get_mc()
        self.assertEqual(mc1, 0)
        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_edge(1, 2, 10)
        mc2 = self.graph.get_mc()
        self.assertEqual(mc1+3, mc2)
        self.graph.remove_node(1)
        mc3 = self.graph.get_mc()
        self.assertEqual(mc2, mc3-2)

    def test_add_edge(self):
        self.fail()

    def test_add_node(self):
        self.fail()

    def test_remove_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()
