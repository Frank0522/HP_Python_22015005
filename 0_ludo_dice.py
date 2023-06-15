while True:
      command = input ("enter 'toss' to roll the dice or'quit'to end the game:")
      if command == 'toss':
         dice_roll = random.randint (1,6)
         print("you rolled a",dice roll)
      elif command == 'quit':
           print ("Thank for playing!")
           break 
      else: 
          print ("invaild input please enter 'toss' or 'quit'.")
