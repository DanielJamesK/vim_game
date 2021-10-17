from game_functions.get_stones import get_stones
from game_functions.remove_stones import remove_stones
from game_functions.check_game_status import check_game_status
from game_functions.alternate_player_turn import alternate_player_turn

# Function to handle errors on initial input and start the game.
def start_game():
  playerTurn = True
  stonesRemaining = get_stones()
  while stonesRemaining > 0:
    stonesRemaining = remove_stones(stonesRemaining, playerTurn)
    check_game_status(stonesRemaining, playerTurn)
    playerTurn = alternate_player_turn(playerTurn)