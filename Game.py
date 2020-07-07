class Game:

    def calculate_result(self, player1, player2):

        if player1 == player2:
            return 'Tie game'

        if player1 == 'paper' and player2 == 'rock':
            return 'Player one wins'

        if player1 == 'rock' and player2 == 'scissors':
            return 'Player one wins'

        if player1 == 'scissors' and player2 == 'paper':
            return 'Player one wins'

        return 'Player two wins'
