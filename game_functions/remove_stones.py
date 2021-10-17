from game_functions.players_turn import players_turn
from game_functions.ai_turn import ai_turn

def remove_stones(stonesRemaining, playerTurn):
  if playerTurn == True:
    return players_turn(stonesRemaining)
  else:
    return ai_turn(stonesRemaining)