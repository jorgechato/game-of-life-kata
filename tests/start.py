import unittest
from utils.main import parse
from game.start import calculate_next


class RulesTest(unittest.TestCase):
    def test_rule1(self):
        """
        any live cell with fewer than two live neighbours dies, as if cause by underpopulation (1)
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

    @unittest.skip("any live cell with more than three live neighbours dies, as if by overcrowding")
    def test_rule2(self):
        """
        any live cell with more than three live neighbours dies, as if by overcrowding
        """
        self.fail("shouldn't happen")

    @unittest.skip("any dead cell with exactly three live neighbours becomes a live cell")
    def test_rule3(self):
        """
        any dead cell with exactly three live neighbours becomes a live cell
        """
        self.fail("shouldn't happen")

    @unittest.skip("any live cell with two or three live neighbours lives on to the next generation")
    def test_rule4(self):
        """
        any live cell with two or three live neighbours lives on to the next generation
        """
        self.fail("shouldn't happen")


if __name__ == '__main__':
    unittest.main()
