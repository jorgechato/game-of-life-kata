import unittest
from utils.main import parse
from game.start import calculate_next


class RulesTest(unittest.TestCase):
    def test_rule1_0(self):
        """
        any live cell with fewer than two live neighbours dies, as if cause by underpopulation
        """
        start = parse(4, 8, '''
                      ........
                      ....*...
                      ....*...
                      ........
                    ''')

        end = parse(4, 8, '''
                      ........
                      ........
                      ........
                      ........
                    ''')

        result = calculate_next(start)

        self.assertEqual(end, result, msg="Objects should be equals")

    def test_rule1_1(self):
        """
        any live cell with fewer than two live neighbours dies, as if cause by underpopulation
        """
        start = parse(4, 8, '''
                      **......
                      ........
                      ........
                      ........
                    ''')

        end = parse(4, 8, '''
                      ........
                      ........
                      ........
                      ........
                    ''')

        result = calculate_next(start)

        self.assertEqual(end, result, msg="Objects should be equals")

    def test_rule1_2(self):
        """
        any live cell with fewer than two live neighbours dies, as if cause by underpopulation
        """
        start = parse(4, 8, '''
                      *.......
                      *.......
                      .......*
                      **.....*
                    ''')

        end = parse(4, 8, '''
                      ........
                      ........
                      **......
                      ........
                    ''')

        result = calculate_next(start)

        self.assertEqual(end, result, msg="Objects should be equals")

    def test_rule2_0(self):
        """
        any live cell with more than three live neighbours dies, as if by overcrowding
        """
        start = parse(4, 8, '''
                      ........
                      ......*.
                      .....***
                      ......*.
                    ''')

        end = parse(4, 8, '''
                      ........
                      .....***
                      .....*.*
                      .....***
                    ''')

        result = calculate_next(start)

        self.assertEqual(end, result, msg="Objects should be equals")

    def test_rule2_1(self):
        """
        any live cell with more than three live neighbours dies, as if by overcrowding
        """
        start = parse(4, 8, '''
                      **......
                      **......
                      *.......
                      ........
                    ''')

        end = parse(4, 8, '''
                      **......
                      ........
                      **......
                      ........
                    ''')

        result = calculate_next(start)

        self.assertEqual(end, result, msg="Objects should be equals")

    def test_rule3_0(self):
        """
        any live cell with two or three live neighbours lives on to the next generation
        """
        start = parse(4, 8, '''
                      ***.....
                      .*......
                      ........
                      ........
                    ''')

        end = parse(4, 8, '''
                      ***.....
                      ***.....
                      ........
                      ........
                    ''')

        result = calculate_next(start)

        self.assertEqual(end, result, msg="Objects should be equals")

    def test_rule3_1(self):
        """
        any live cell with two or three live neighbours lives on to the next generation
        """
        start = parse(4, 8, '''
                      ........
                      ........
                      ......**
                      .......*
                    ''')

        end = parse(4, 8, '''
                      ........
                      ........
                      ......**
                      ......**
                    ''')

        result = calculate_next(start)

        self.assertEqual(end, result, msg="Objects should be equals")

    def test_rule3_2(self):
        """
        any live cell with two or three live neighbours lives on to the next generation
        """
        start = parse(4, 8, '''
                      ........
                      ...**...
                      ...*.*..
                      ....*...
                    ''')

        end = parse(4, 8, '''
                      ........
                      ...**...
                      ...*.*..
                      ....*...
                    ''')

        result = calculate_next(start)

        self.assertEqual(end, result, msg="Objects should be equals")


if __name__ == '__main__':
    unittest.main()
