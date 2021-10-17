#get_stones function asks for a users input and returns it's value in a variable called stonesRemaining
def get_stones():
  stonesRemaining = int(input("Please select a number between 30 and 50 which will represent the amount of stones in the pile.\n"))

  # Error handling for incorrect user input
  while stonesRemaining > 50 or stonesRemaining < 30:
    stonesRemaining = int(input("Invalid input!\nPlease select a number between 30 and 50.\n"))

  return stonesRemaining
