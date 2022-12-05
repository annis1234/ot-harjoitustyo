import unittest
from services.plot_service import PLOT_SERVICE
from entities.tree import Tree

class TestPlot(unittest.TestCase):

    def setUp(self):
        self._plot_service = PLOT_SERVICE
        self._plot_service.create_plot("test_plot")
        self._plot_service.clear_plot()

    def test_create(self):
        tree1 = Tree("Mänty", 28, 30)
        self._plot_service.create_tree(tree1)
        trees = self._plot_service.return_trees()
        self.assertEqual(len(trees), 1)
        self.assertEqual(trees[0].tree_sp, "Mänty")

    def test_mean_height(self):
        tree1 = Tree("Mänty", 28, 20)
        tree2 = Tree("Mänty", 28, 30)
        self._plot_service.create_tree(tree1)
        self._plot_service.create_tree(tree2)
        self.assertEqual(self._plot_service.mean_height(), 25)

    def test_mean_d(self):
        tree1 = Tree("Mänty", 20, 25)
        tree2 = Tree("Mänty", 30, 25)
        self._plot_service.create_tree(tree1)
        self._plot_service.create_tree(tree2)
        self.assertEqual(self._plot_service.mean_diameter(), 25)

    def test_v_sum(self):
        tree1 = Tree("Mänty", 20, 20)
        tree2 = Tree("Mänty", 20, 20)
        self._plot_service.create_tree(tree1)
        self._plot_service.create_tree(tree2)
        self.assertEqual(self._plot_service.sum_vol(), 0.628)

    def test_main_tree_sp(self):
        tree1 = Tree("Mänty", 20, 20)
        tree2 = Tree("Mänty", 20, 20)
        tree3 = Tree("Kuusi", 25, 30)
        self._plot_service.create_tree(tree1)
        self._plot_service.create_tree(tree2)
        self._plot_service.create_tree(tree3)
        self.assertEqual(self._plot_service.main_tree_sp(), "Mänty")

    def test_handle_two_plots(self):
        self._plot_service.create_plot("test_plot2")
        self._plot_service.select_plot("test_plot2")
        tree1 = Tree("Mänty", 20, 20)
        self._plot_service.create_tree(tree1)
        self.assertEqual(len(self._plot_service.return_trees()), 1)

        self._plot_service.select_plot("test_plot")
        tree2 = Tree("Kuusi", 25, 25)
        self._plot_service.create_tree(tree2)

        self.assertEqual(len(self._plot_service.return_trees()), 1)

        self._plot_service.select_plot("test_plot2")
        self._plot_service.clear_plot()

        self.assertEqual(len(self._plot_service.return_trees()), 0)
        