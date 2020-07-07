class SheldonGame:

    def calculate_sheldon_result(self, player1, player2):

        if player1 == 'scissors' and (player2 == 'paper' or player2 == 'lizard'):
            return 'Scissors wins'

        if player1 == 'paper' and (player2 == 'rock' or player2 == 'spock'):
            return 'Paper wins'

        if player1 == 'rock' and (player2 == 'lizard' or player2 == 'scissors'):
            return 'Rock wins'

        if player1 == 'lizard' and (player2 == 'spock' or player2 == 'paper'):
            return 'Lizard wins'

        if player1 == 'spock' and (player2 == 'scissors' or player2 == 'rock'):
            return 'Spock wins'

        if player1 == player2:
            return 'Tie game'

        return 'Player two wins'
