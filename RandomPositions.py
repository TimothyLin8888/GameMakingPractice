import pygame
import random
pygame.init()
# The pieces which should equal to 16 each for black and red
black_pieces = ["B_king","B_queen1","B_queen2", "B_elephant1", "B_elephant2","B_car1","B_car2","B_horse1","B_horse2", "B_soldier1","B_soldier2","B_soldier3","B_soldier4","B_soldier5","B_cannon1","B_cannon2"]
black_locations = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
red_pieces = ["R_king","R_queen1","R_queen2", "R_elephant1", "R_elephant2","R_car1","R_car2","R_horse1","R_horse2", "R_soldier1","R_soldier2","R_soldier3","R_soldier4","R_soldier5","R_cannon1","R_cannon2"]
board = [['  ' for i in range(8)] for i in range(4)]

for i in range(4):
    for j in range(8):
        random_num = random.randint(1,2)
        if random_num == 1 or len(red_pieces) == 0:
            random_piece = random.choice(black_pieces)
            board[i][j] = random_piece
            black_pieces.remove(random_piece)
        elif random_num == 2 or len(black_pieces) != 0:
            random_piece = random.choice(red_pieces)
            board[i][j] = random_piece
            red_pieces.remove(random_piece)

print(board)
# board = [[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7]]
# for n in board:
#     print(n)