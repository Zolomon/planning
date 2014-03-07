from generator import WumpusProblem, ProblemWriter

__author__ = 'bengt'

import random
import unittest


class TestWumpusWorld(unittest.TestCase):
    def setUp(self):
        pass

    def test_wumpus(self):
        problem = WumpusProblem(m=4, n=4)
        self.assertEqual(problem.getSize(), (4, 4))
        self.assertEqual(problem.getWumpuses(), 1)
        self.assertEqual(problem.getPits(), 1)
        self.assertEqual(problem.getGold(), 1)

    def test_wumpus_generate(self):
        problem = WumpusProblem(m=4, n=4)
        problem.generate()
        tiles = problem.getTiles()
        self.assertEqual(len([(x, y, t) for x, y, t in tiles if t == "wumpus"]), 1)
        self.assertEqual(len([(x, y, t) for x, y, t in tiles if t == "pit"]), 1)
        self.assertEqual(len([(x, y, t) for x, y, t in tiles if t == "gold"]), 1)

        print(tiles)
        writer = ProblemWriter(problem)
        print(writer)

        problem = WumpusProblem(m=4, n=4, wumpuses=5, pits=5, gold=5)
        problem.generate()
        tiles = problem.getTiles()
        self.assertEqual(tiles[0][2], "agent")
        self.assertEqual(len([(x, y, t) for x, y, t in tiles if t == "wumpus"]), 5)
        self.assertEqual(len([(x, y, t) for x, y, t in tiles if t == "pit"]), 5)
        self.assertEqual(len([(x, y, t) for x, y, t in tiles if t == "gold"]), 5)

    def test_wumpus_1_4(self):
        problem = WumpusProblem(m=1, n=4, wumpuses=1, pits=1, gold=1)
        problem.generate()
        tiles = problem.getTiles()
        self.assertEqual(len([(x, y, t) for x, y, t in tiles if t == "wumpus"]), 1)
        self.assertEqual(len([(x, y, t) for x, y, t in tiles if t == "pit"]), 1)
        self.assertEqual(len([(x, y, t) for x, y, t in tiles if t == "gold"]), 1)
        print(tiles)
