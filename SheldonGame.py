class SheldonGame:
    def calculate_sheldon_result(self, player1, player2):

        if player1 == 'scissors' and player2 == 'paper':
            return 'Scissors cuts Paper'

        if player1 == 'paper' and player2 == 'rock':
            return 'Paper covers Rock'

        if player1 == 'rock' and player2 == 'lizard':
            return 'Rock crushes Lizard'

        if player1 == 'lizard' and player2 == 'spock':
            return 'Lizard poisons Spock'

        if player1 == 'spock' and player2 == 'scissors':
            return 'Spock smashes Scissors'

        if player1 == 'scissors' and player2 == 'lizard':
            return 'Scissors decapitates Lizard'

        if player1 == 'lizard' and player2 == 'paper':
            return 'Lizard eats Paper'

        if player1 == 'paper' and player2 == 'spock':
            return 'Paper disproves Spock'

        if player1 == 'spock' and player2 == 'rock':
            return 'Spock vaporizes Rock'

        if player1 == 'rock' and player2 == 'scissors':
            return 'Rock crushes Scissors'

        if player1 == 'paper' and player2 == 'paper':
            return 'Tie game'

        if player1 == 'rock' and player2 == 'rock':
            return 'Tie game'

        if player1 == 'scissors' and player2 == 'scissors':
            return 'Tie game'

        if player1 == 'lizard' and player2 == 'lizard':
            return 'Tie game'

        if player1 == 'spock' and player2 == 'spock':
            return 'Tie game'

        return 'Player two wins'
