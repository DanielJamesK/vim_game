def players_turn(stonesRemaining):

  valid_input = False
  while valid_input != True:
    stonesRemoved = int(input("Please select how many stones you would like to remove from the pile:\n"))
    if stonesRemoved > 3 or stonesRemoved < 1:
        # Error handling for incorrect user input.
        print("You must select between 1 and 3 stones. There is currently", stonesRemaining, "stones remaining.")
    elif stonesRemaining - stonesRemoved < 0:
        # Error handling if user removes more stones than available.
        print("You have selected to remove more stones than there are left! Please try again.") #Give user error!
    else:
        stonesRemaining -= stonesRemoved
        print("You removed", stonesRemoved, "stone(s). There is currently", stonesRemaining, "stones remaining.")
        valid_input = True
  
  return stonesRemaining