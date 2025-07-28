COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3
ROCK = 1
PAPER = 2
SCISSORS = 3


def rockPaperScissors(player, computer):
    if (computer == player):
        return TIE

    if computer == ROCK:
        if player == PAPER:
            return PLAYER_WINS
        elif player == SCISSORS:
            return COMPUTER_WINS
        else:
            return INVALID
    elif computer == PAPER:
        if player == ROCK:
            return COMPUTER_WINS
        elif player == SCISSORS:
            return PLAYER_WINS
        else:
            return INVALID
    else:
        if player == ROCK:
            return PLAYER_WINS
        elif player == PAPER:
            return COMPUTER_WINS
        else:
            return INVALID