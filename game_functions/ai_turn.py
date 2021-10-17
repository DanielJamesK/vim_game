import random

def ai_turn(stonesRemaining):
  stonesRemoved = random.randint(1, min(3, stonesRemaining) )
  stonesRemaining -= stonesRemoved
  print("The A.I. removed", stonesRemoved, "stone(s). There is currently", stonesRemaining, "stones remaining.")

  return stonesRemaining