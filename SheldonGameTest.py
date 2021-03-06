import unittest

from SheldonGame import SheldonGame


class SheldonGameTest(unittest.TestCase):

    def test_scissors_wins_paper(self):
        game = SheldonGame()
        result = game.calculate_sheldon_result('scissors', 'paper')
        self.assertEqual('Scissors wins', result)

    def test_scissors_wins_lizard(self):
        game = SheldonGame()
        result = game.calculate_sheldon_result('scissors', 'lizard')
        self.assertEqual('Scissors wins', result)

    def test_paper_wins_rock(self):
        game = SheldonGame()
        result = game.calculate_sheldon_result('paper', 'rock')
        self.assertEqual('Paper wins', result)

    def test_paper_wins_spock(self):
        game = SheldonGame()
        result = game.calculate_sheldon_result('paper', 'spock')
        self.assertEqual('Paper wins', result)

    def test_rock_wins_lizard(self):
        game = SheldonGame()
        result = game.calculate_sheldon_result('rock', 'lizard')
        self.assertEqual('Rock wins', result)

    def test_rock_wins_scissors(self):
        game = SheldonGame()
        result = game.calculate_sheldon_result('rock', 'scissors')
        self.assertEqual('Rock wins', result)

    def test_lizard_wins_spock(self):
        game = SheldonGame()
        result = game.calculate_sheldon_result('lizard', 'spock')
        self.assertEqual('Lizard wins', result)

    def test_lizard_wins_paper(self):
        game = SheldonGame()
        result = game.calculate_sheldon_result('lizard', 'paper')
        self.assertEqual('Lizard wins', result)

    def test_spock_wins_scissors(self):
        game = SheldonGame()
        result = game.calculate_sheldon_result('spock', 'scissors')
        self.assertEqual('Spock wins', result)

    def test_spock_wins_rock(self):
        game = SheldonGame()
        result = game.calculate_sheldon_result('spock', 'rock')
        self.assertEqual('Spock wins', result)

    def test_paper_ties(self):
        game = SheldonGame()
        result = game.calculate_sheldon_result('paper', 'paper')
        self.assertEqual('Tie game', result)

    def test_rock_ties(self):
        game = SheldonGame()
        result = game.calculate_sheldon_result('rock', 'rock')
        self.assertEqual('Tie game', result)

    def test_scissors_ties(self):
        game = SheldonGame()
        result = game.calculate_sheldon_result('scissors', 'scissors')
        self.assertEqual('Tie game', result)

    def test_lizard_ties(self):
        game = SheldonGame()
        result = game.calculate_sheldon_result('lizard', 'lizard')
        self.assertEqual('Tie game', result)

    def test_spock_ties(self):
        game = SheldonGame()
        result = game.calculate_sheldon_result('spock', 'spock')
        self.assertEqual('Tie game', result)


if __name__ == '__main__':
    unittest.main()
