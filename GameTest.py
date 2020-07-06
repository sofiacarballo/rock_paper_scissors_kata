import unittest

from Game import Game


class GameTest(unittest.TestCase):

    def test_paper_wins_rock(self):
        game = Game()
        result = game.calculate_result('paper', 'rock')
        self.assertEqual('Player one wins', result)


if __name__ == '__main__':
    unittest.main()
