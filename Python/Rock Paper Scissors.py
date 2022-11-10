def instructions():
   text = '''
   Let's play! You have to return which player won! In case of a draw return Draw!.
   Examples(Input1, Input2 --> Output):
   "scissors", "paper" --> "Player 1 won!"
   "scissors", "rock" --> "Player 2 won!"
   "paper", "paper" --> "Draw!"
   '''
   return text

def rps(p1, p2):
    if p1 == 'rock':
        if p2 == 'scissors':
            return 'Player 1 won!'
        elif p2 == p1:
            return 'Draw!'
        else:
             return 'Player 2 won!'
    elif p1 == 'scissors':
        if p2 == 'paper':
            return 'Player 1 won!'
        elif p2 == p1:
            return 'Draw!'
        else:
             return 'Player 2 won!'
    elif p1 == 'paper':
        if p2 == 'rock':
            return 'Player 1 won!'
        elif p2 == p1:
            return 'Draw!'
        else:
             return 'Player 2 won!'

#! Bestpratices
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"