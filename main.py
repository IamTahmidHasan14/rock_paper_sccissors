import random

player = int(input("Press 1 to start and 0 to Exit: "))
if player == 1:
  while not player == 0:
    print("1 = ROCK, 2 = PAPER and 3 = SCISSORS And 0 = EXIT")
    player = int(input("Chosse between 0 to 3: "))
    if player == 1: print("Player: ROCK")
    elif player == 2: print("Player: PAPER")
    elif player == 3: print("Player: SCISSORS")
    if not player == 0:
      pc = random.randint(1, 3)
      if pc == 1:
        print("PC: ROCK")
        if player == 1: print("Draw")
        elif player == 2: print("Win!!")
        elif player == 3: print("Better luck next time!!!")
      elif pc == 2:
        print("PC: PAPER")
        if player == 1: print("Better luck next time!!!")
        elif player == 2: print("Draw")
        elif player == 3: print("Win!!")
      else:
        print("PC: SCISSORS")
        if player == 1: print("Win!!")
        elif player == 2: print("Better luck next time!!!")
        elif player == 3: print("Draw")
      print()

else:
  print("Game closed!")