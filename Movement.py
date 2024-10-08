# from RandomPositions import positions

'''
                 [4][1]

   [3][2]        [4][2]          [5][2]
               
                 [4][3]
'''

position = [4,2]
move = input("Which way would you like to move: ")
powerLevel = 3
oppLevel = 2
if move == 'up':
    if powerLevel > oppLevel:
        position[1] -= 1
elif move == 'down':
    if powerLevel > oppLevel:
        position[1] += 1
elif move == 'left':
    if powerLevel > oppLevel:
        position[0] -= 1
elif move == 'right':
    if powerLevel > oppLevel:
        position[0] += 1
else:
    print("Not valid")

print(position)