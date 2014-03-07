import argparse
import random
import string
import itertools


class WumpusProblem():
    def __init__(self, name="wumpus-problem", m=1, n=1, wumpuses=1, pits=1, gold=1, kill=False):
        self.m = m
        self.n = n
        self.wumpuses = wumpuses
        self.pits = pits
        self.gold = gold
        self.tiles = []
        self.kill = kill
        self.name = "{0}-{1}-{2}-{3}-{4}-{5}-{6}".format(name, m, n, wumpuses, pits, gold, kill)

    def getSize(self):
        return self.m, self.n

    def getWumpuses(self):
        return self.wumpuses

    def getPits(self):
        return self.pits

    def getGold(self):
        return self.gold

    def generate(self):
        def generateNTypes(m, n, tiles, count, type):
            for i in range(count):
                open_set = [(x, y) for x, y, t in tiles if t is None]
                length = len(open_set)

                if length == 0:
                    raise Exception()

                random_value = open_set[random.randint(0, length - 1)]
                value = [(x, y, t) for x, y, t in tiles if x == random_value[0] and y == random_value[1]][0]
                tiles[(value[0] - 1) + (value[1] - 1) * m] = (value[0], value[1], type)

        # Make a board of tiles
        self.tiles = [(x, y, None) for y in range(1, self.n + 1) for x in range(1, self.m + 1)]
        m, n = self.getSize()
        self.tiles[0] = (1, 1, "agent")
        generateNTypes(m, n, self.tiles, self.getWumpuses(), "wumpus")
        generateNTypes(m, n, self.tiles, self.getPits(), "pit")
        generateNTypes(m, n, self.tiles, self.getGold(), "gold")

    def getTiles(self):
        return self.tiles

    def getName(self):
        return self.name

    def getKill(self):
        return self.kill

class ProblemWriter(object):
    def __init__(self, problem):
        self.problem = problem

    def __repr__(self):
        def adjacentTiles(problem):
            n, m = problem.getSize()
            adjacents = ''
            if n > 1 and m > 1:  # rectangle
                for y in range(1, m):
                    for x in range(1, n):
                        adjacents += '(adjacent t-{0}-{1} t-{2}-{3}) (adjacent t-{2}-{3} t-{0}-{1})\n   '. \
                            format(x, y, x, y + 1)
                        adjacents += '(adjacent t-{0}-{1} t-{2}-{3}) (adjacent t-{2}-{3} t-{0}-{1})\n   '. \
                            format(x, y, x + 1, y)

                for x in range(1, n):  # connect bottom row
                    adjacents += '(adjacent t-{0}-{1} t-{2}-{3}) (adjacent t-{2}-{3} t-{0}-{1})\n   '. \
                        format(x, m, x + 1, m)

                for y in range(1, m):  # connect last row
                    adjacents += '(adjacent t-{0}-{1} t-{2}-{3}) (adjacent t-{2}-{3} t-{0}-{1})\n   '. \
                        format(n, y, n, y + 1)

            elif n == 1 and m > 1:  # 1 column
                for y in range(1, m):
                    adjacents += '(adjacent t-{0}-{1} t-{2}-{3}) (adjacent t-{2}-{3} t-{0}-{1})\n   '. \
                        format(1, y, 1, y + 1)
            elif n > 1 and m == 1:  # 1 row
                for x in range(1, n):
                    adjacents += '(adjacent t-{0}-{1} t-{2}-{3}) (adjacent t-{2}-{3} t-{0}-{1})\n   '. \
                        format(x, 1, x + 1, 1)

            return adjacents

        values = {'problemName': 'problemName',
                  'problemDomain': 'problemDomain',
                  'tiles': 'tiles',
                  'wumpuses': 'wumpuses',
                  'pits': 'pits',
                  'golds': 'golds',
                  'adjacentTiles': 'adjacentTiles',
                  'wumpusesAt': 'wumpusesAt',
                  'wumpusesAlive': 'wumpusesAlive',
                  'pitsAt': 'pitsAt',
                  'goldsAt': 'goldsAt',
                  'haveGolds': 'haveGolds',
                  'killWumpuses': '',
                  'arrows': 'arrow-1 - arrow',
                  'haveArrows': '(have agent arrow-1)'}

        a = string.Template(
            """(define (problem $problemName)
  (:domain $problemDomain)
  (:objects
   $tiles - tile
   $wumpuses - wumpus
   $pits - pit
   $golds - gold
   $arrows
   agent - agent
  )
  (:init
   $adjacentTiles
   $wumpusesAt
   $wumpusesAlive
   $pitsAt
   $goldsAt
   (position agent t-1-1)
   (alive agent)
   $haveArrows
  )
  (:goal (and (alive agent)
              (position agent t-1-1)
              $haveGolds
              $killWumpuses
              )))
""")

        m, n = self.problem.getSize()

        values['adjacentTiles'] = adjacentTiles(self.problem)
        values['problemName'] = self.problem.getName()
        values['problemDomain'] = 'wumpus'
        values['tiles'] = " ".join(['t-{0}-{1}'.format(x, y) for y in range(1, n + 1) for x in range(1, m + 1)])
        values['wumpuses'] = " ".join(['wumpus-{0}'.format(w) for w in range(1, self.problem.getWumpuses() + 1)])
        values['pits'] = " ".join(['pit-{0}'.format(p) for p in range(1, self.problem.getPits() + 1)])
        values['golds'] = " ".join(['gold-{0}'.format(g) for g in range(1, self.problem.getGold() + 1)])

        xs = filter(lambda x: x[2] == 'wumpus', self.problem.getTiles())
        wumpuses = ['(position wumpus-{0} t-{1}-{2})'.format(c, x[0], x[1]) for x, c in zip(xs, itertools.count(1, 1))]
        values['wumpusesAt'] = '\n   '.join(wumpuses)

        aliveWumpuses = len([t for t in self.problem.getTiles() if t[2] == 'wumpus'])
        values['wumpusesAlive'] = '\n   '.join(['(alive wumpus-{0})'.format(x) for x in range(1, aliveWumpuses + 1)])

        xs = filter(lambda x: x[2] == 'pit', self.problem.getTiles())
        wumpuses = ['(position pit-{0} t-{1}-{2})'.format(c, x[0], x[1]) for x, c in zip(xs, itertools.count(1, 1))]
        values['pitsAt'] = '\n   '.join(wumpuses)

        xs = filter(lambda x: x[2] == 'gold', self.problem.getTiles())
        wumpuses = ['(position gold-{0} t-{1}-{2})'.format(c, x[0], x[1]) for x, c in zip(xs, itertools.count(1, 1))]
        values['goldsAt'] = '\n   '.join(wumpuses)

        xs = filter(lambda x: x[2] == 'gold', self.problem.getTiles())
        wumpuses = ['(have agent gold-{0})'.format(c) for x, c in zip(xs, itertools.count(1, 1))]
        values['haveGolds'] = '\n   '.join(wumpuses)

        if self.problem.getKill():
            xs = filter(lambda x: x[2] == 'wumpus', self.problem.getTiles())
            wumpuses = ['(not (alive wumpus-{0}))'.format(c) for x, c in zip(xs, itertools.count(1, 1))]
            values['killWumpuses'] = '\n              '.join(wumpuses)

            arrowCount = len(wumpuses)
            values['arrows'] = '\n   '.join(['arrow-{0} - arrow'.format(c) for c in range(1, arrowCount+1)])
            values['haveArrows'] = '\n   '.join(['(have agent arrow-{0})'.format(c) for c in range(1, arrowCount+1)])

        return a.substitute(values)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('m', type=int, help='Number of columns')
    parser.add_argument('n', type=int, help='Number of rows')
    parser.add_argument('w', type=int, help='Number of wumpuses')
    parser.add_argument('p', type=int, help='Number of pits')
    parser.add_argument('g', type=int, help='Number of gold piles')
    parser.add_argument('-k', '--kill-all-wumpuses', action='store_true', help='Set to kill all wumpuses')

    args = parser.parse_args()

    if args.m < 1:
        print("m must be larger than 0")

    if args.n < 1:
        print("n must be larger than 0")

    if args.w < 1:
        print("w must be larger than 0")

    if args.p < 1:
        print("p must be larger than 0")

    if args.g < 1:
        print("g must be larger than 0")

    if args.w + args.g + args.p > args.m * args.n - 1:
        print("I'm not sure if this is possible... Try smaller numbers for w, g or p!")

    problem = WumpusProblem(m=args.m, n=args.n, wumpuses=args.w, pits=args.p, gold=args.g, kill=args.kill_all_wumpuses)
    problem.generate()

    writer = ProblemWriter(problem)

    print(writer)


if __name__ == '__main__':
    main()
