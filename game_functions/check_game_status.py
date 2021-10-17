from game_functions.announce_winner import announce_winner

def check_game_status(stonesRemaining, currentPlayer):
  if stonesRemaining > 0:
    return 
  else:
    announce_winner(currentPlayer)