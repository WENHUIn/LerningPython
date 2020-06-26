## Display 13 original states in alphabetical order.
infile = open("States.txt", 'r')
states = [line.rstrip() for line in infile]
infile.close()
originalStates = states[:13]
originalStates.sort()
for state in originalStates:
    print(state)
          
