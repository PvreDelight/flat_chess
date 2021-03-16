import pygame

import time

import sys

board = [['  ' for i in range(23)] for i in range(16)]

## Creates a chess piece class that shows what team a piece is on, what type of piece it is and whether or not it can be killed by another selected piece.
class Piece:
    def __init__(self, team, type, image,dynamite, killable=False):
        self.team = team
        self.type = type
        self.killable = killable
        self.image = image
        self.dynamite = dynamite



## Creates instances of chess pieces, so far we got: pawn, king, rook and bishop
## The first parameter defines what team its on and the second, what type of piece it is
bp = Piece('b', 'p', 'b_pawn.png',False)
wp = Piece('w', 'p', 'w_pawn.png',False)
wpB = Piece('w','p','w_pawnDynamite.png',False)
bpB = Piece('b','p','b_pawnDynamite.png',False)
bk = Piece('b', 'k', 'b_king.png',False)
wk = Piece('w', 'k', 'w_king.png',False)
br = Piece('b', 'r', 'b_rook.png',False)
wr = Piece('w', 'r', 'w_rook.png',False)
bb = Piece('b', 'b', 'b_bishop.png',False)
wb = Piece('w', 'b', 'w_bishop.png',False)
bq = Piece('b', 'q', 'b_queen.png',False)
wq = Piece('w', 'q', 'w_queen.png',False)
bkn = Piece('b', 'kn', 'b_knight.png',False)
wkn = Piece('w', 'kn', 'w_knight.png',False)
rp = Piece('r', 'p', 'r_pawn.png',False)
rpB = Piece('r', 'p', 'r_pawnDynamite.png',False)
rk = Piece('r', 'k', 'r_king.png',False)
rr = Piece('r', 'r', 'r_rook.png',False)
rb = Piece('r', 'b', 'r_bishop.png',False)
rq = Piece('r', 'q', 'r_queen.png',False)
rkn = Piece('r', 'kn', 'r_knight.png',False)

up = Piece('u', 'p', 'u_pawn.png',False)
upB = Piece('u', 'p', 'u_pawnDynamite.png',False )
uk = Piece('u', 'kn', 'u_king.png',False)
ur = Piece('u', 'r', 'u_rook.png',False)
ub = Piece('u', 'b', 'u_bishop.png',False)
uq = Piece('u', 'q', 'u_queen.png',False)
ukn = Piece('u', 'kn', 'u_knight.png',False)

yp = Piece('y', 'p', 'y_pawn.png',False)
ypB = Piece('y', 'p', 'y_pawnDynamite.png',False)
yk = Piece('y', 'kn', 'y_king.png',False)
yr = Piece('y', 'r', 'y_rook.png',False)
yb = Piece('y', 'b', 'y_bishop.png',False)
yq = Piece('y', 'q', 'y_queen.png',False)
ykn = Piece('y', 'kn', 'y_knight.png',False)

gp = Piece('g', 'p', 'g_pawn.png',False)
gk = Piece('g', 'kn', 'g_king.png',False)
gr = Piece('g', 'r', 'g_rook.png',False)
gb = Piece('g', 'b', 'g_bishop.png',False)
gq = Piece('g', 'q', 'g_queen.png',False)
gkn = Piece('g', 'kn', 'g_knight.png',False)
gpB = Piece('g', 'p', 'g_pawnDynamite.png',False)

starting_order = {(0,0): pygame.transform.scale(pygame.image.load(yr.image),(30,30)),(0,1): pygame.transform.scale(pygame.image.load(yb.image),(30,30)),(0,2): pygame.transform.scale(pygame.image.load(yq.image),(30,30)),(0,3): pygame.transform.scale(pygame.image.load(yk.image),(30,30)),(0,4): pygame.transform.scale(pygame.image.load(yb.image),(30,30)),(0,5): pygame.transform.scale(pygame.image.load(yr.image),(30,30)),
(0,6): None,(0,7): None,(0,8): None,(0,9): None,(0,10): None,(0,11): None,(0,12): None,(0,13): None,
(0,14): pygame.transform.scale(pygame.image.load(bp.image),(30,30)),(0,15): pygame.transform.scale(pygame.image.load(br.image),(30,30)),(1,0): pygame.transform.scale(pygame.image.load(yp.image),(30,30)),(1,1): pygame.transform.scale(pygame.image.load(yp.image),(30,30)),(1,2): pygame.transform.scale(pygame.image.load(yp.image),(30,30)),(1,3): pygame.transform.scale(pygame.image.load(ypB.image),(30,30)),(1,4): pygame.transform.scale(pygame.image.load(ykn.image),(30,30)),(1,5): pygame.transform.scale(pygame.image.load(ykn.image),(30,30)),
(1,6): None,(1,7): None,(1,8): None,(1,9): None,(1,10): None,(1,11): None,(1,12): None,(1,13): None,
(1,14): pygame.transform.scale(pygame.image.load(bp.image),(30,30)),(1,15): pygame.transform.scale(pygame.image.load(bb.image),(30,30)),
(2,0): None,(2,1): None,(2,2): None,(2,3): None,(2,4): None,(2,5): None,(2,6): None,(2,7): None,(2,8): None,(2,9): None,(2,10): None,(2,11): None,(2,12): None,(2,13): None,
(2,14): pygame.transform.scale(pygame.image.load(bp.image),(30,30)),(2,15): pygame.transform.scale(pygame.image.load(bq.image),(30,30)),
(3,0): None,(3,1): None,(3,2): None,(3,3): None,(3,4): None,(3,5): None,(3,6): None,(3,7): None,(3,8): None,(3,9): None,(3,10): None,(3,11): None,(3,12): None,(3,13): None,
(3,14): pygame.transform.scale(pygame.image.load(bpB.image),(30,30)),(3,15): pygame.transform.scale(pygame.image.load(bk.image),(30,30)),
(4,0): None,(4,1): None,(4,2): None,(4,3): None,(4,4): None,(4,5): None,(4,6): None,(4,7): None,(4,8): None,(4,9): None,(4,10): None,(4,11): None,(4,12): None,(4,13): None,
(4,14):pygame.transform.scale(pygame.image.load(bkn.image),(30,30)),(4,15): pygame.transform.scale(pygame.image.load(bb.image),(30,30)),
(5,0): None,(5,1): None,(5,2): None,(5,3): None,(5,4): None,(5,5): None,(5,6): None,(5,7): None,(5,8): None,(5,9): None,(5,10): None,(5,11): None,(5,12): None,(5,13): None,
(5,14):pygame.transform.scale(pygame.image.load(bkn.image),(30,30)),(5,15): pygame.transform.scale(pygame.image.load(br.image),(30,30)),
(6,0): None,(6,1): None,(6,2): None,(6,3): None,(6,4): None,(6,5): None,(6,6): None,(6,7): None,(6,8): None,(6,9): None,(6,10): None,(6,11): None,(6,12): None,(6,13): None,(6,14): None,(6,15): None,(7,0): None,(7,1): None,(7,2): None,(7,3): None,(7,4): None,(7,5): None,(7,6): None,(7,7): None,(7,8): None,(7,9): None,(7,10): None,(7,11): None,(7,12): None,(7,13): None,
(7,14): pygame.transform.scale(pygame.image.load(wkn.image),(30,30)),(7,15): pygame.transform.scale(pygame.image.load(wr.image),(30,30)),
(8,0): None,(8,1): None,(8,2): None,(8,3): None,(8,4): None,(8,5): None,(8,6): None,(8,7): None,(8,8): None,(8,9): None,(8,10): None,(8,11): None,(8,12): None,(8,13): None,
(8,14):  pygame.transform.scale(pygame.image.load(wkn.image),(30,30)),(8,15): pygame.transform.scale(pygame.image.load(wb.image),(30,30)),
(9,0): None,(9,1): None,(9,2): None,(9,3): None,(9,4): None,(9,5): None,(9,6): None,(9,7): None,(9,8): None,(9,9): None,(9,10): None,(9,11): None,(9,12): None,(9,13): None,
(9,14):  pygame.transform.scale(pygame.image.load(wpB.image),(30,30)),(9,15): pygame.transform.scale(pygame.image.load(wk.image),(30,30)),
(10,0): None,(10,1): None,(10,2): None,(10,3): None,(10,4): None,(10,5): None,(10,6): None,(10,7): None,(10,8): None,(10,9): None,(10,10): None,(10,11): None,(10,12): None,(10,13): None,
(10,14):  pygame.transform.scale(pygame.image.load(wp.image),(30,30)),(10,15): pygame.transform.scale(pygame.image.load(wq.image),(30,30)),
(11,0): None,(11,1): None,(11,2): None,(11,3): None,(11,4): None,(11,5): None,(11,6): None,(11,7): None,(11,8): None,(11,9): None,(11,10): None,(11,11): None,(11,12): None,(11,13): None,
(11,14):  pygame.transform.scale(pygame.image.load(wp.image),(30,30)),(11,15): pygame.transform.scale(pygame.image.load(wb.image),(30,30)),
(12,0): None,(12,1): None,(12,2): None,(12,3): None,(12,4): None,(12,5): None,(12,6): None,(12,7): None,(12,8): None,(12,9): None,(12,10): None,(12,11): None,(12,12): None,(12,13): None,
(12,14):  pygame.transform.scale(pygame.image.load(wp.image),(30,30)),(12,15): pygame.transform.scale(pygame.image.load(wr.image),(30,30)),
(13,0): None,(13,1): None,(13,2): None,(13,3): None,(13,4): None,(13,5): None,(13,6): None,(13,7): None,(13,8): None,(13,9): None,(13,10): None,(13,11): None,(13,12): None,(13,13): None,(13,14): None,(13,15): None,(14,0): None,(14,1): None,(14,2): None,(14,3): None,(14,4): None,(14,5): None,(14,6): None,(14,7): None,(14,8): None,(14,9): None,(14,10): None,(14,11): None,(14,12): None,
(14,13): pygame.transform.scale(pygame.image.load(rpB.image),(30,30)),(14,14): pygame.transform.scale(pygame.image.load(rr.image),(30,30)),(14,15): pygame.transform.scale(pygame.image.load(rb.image),(30,30)),
(15,0): None,(15,1): None,(15,2): None,(15,3): None,(15,4): None,(15,5): None,(15,6): None,(15,7): None,(15,8): None,(15,9): None,(15,10): None,(15,11): None,(15,12): None,
(15,13): pygame.transform.scale(pygame.image.load(rp.image),(30,30)),(15,14): pygame.transform.scale(pygame.image.load(rkn.image),(30,30)),(15,15): pygame.transform.scale(pygame.image.load(rk.image),(30,30)),
(16,0): None,(16,1): None,(16,2): None,(16,3): None,(16,4): None,(16,5): None,(16,6): None,(16,7): None,(16,8): None,(16,9): None,(16,10): None,(16,11): None,(16,12): None,
(16,13): pygame.transform.scale(pygame.image.load(rp.image),(30,30)),(16,14): pygame.transform.scale(pygame.image.load(rkn.image),(30,30)),(16,15): pygame.transform.scale(pygame.image.load(rq.image),(30,30)),
(17,0): None,(17,1): None,(17,2): None,(17,3): None,(17,4): None,(17,5): None,(17,6): None,(17,7): None,(17,8): None,(17,9): None,(17,10): None,(17,11): None,(17,12): None,
(17,13): pygame.transform.scale(pygame.image.load(rp.image),(30,30)),(17,14): pygame.transform.scale(pygame.image.load(rr.image),(30,30)),(17,15): pygame.transform.scale(pygame.image.load(rb.image),(30,30)),
(18,0): None,(18,1): None,(18,2): None,(18,3): None,(18,4): None,(18,5): None,(18,6): None,(18,7): None,(18,8): None,(18,9): None,(18,10): None,(18,11): None,(18,12): None,(18,13): None,(18,14): None,(18,15): None,(19,0): None,(19,1): None,(19,2): None,(19,3): None,(19,4): None,(19,5): None,(19,6): None,(19,7): None,(19,8): None,(19,9): None,(19,10): None,(19,11): None,(19,12): None,
(19,13): pygame.transform.scale(pygame.image.load(upB.image),(30,30)),(19,14):  pygame.transform.scale(pygame.image.load(ur.image),(30,30)),(19,15):  pygame.transform.scale(pygame.image.load(ub.image),(30,30)),
(20,0): None,(20,1): None,(20,2): None,(20,3): None,(20,4): None,(20,5): None,(20,6): None,(20,7): None,(20,8): None,(20,9): None,(20,10): None,(20,11): None,(20,12): None,
(20,13):  pygame.transform.scale(pygame.image.load(up.image),(30,30)),(20,14):  pygame.transform.scale(pygame.image.load(ukn.image),(30,30)),(20,15):  pygame.transform.scale(pygame.image.load(uk.image),(30,30)),
(21,0):  pygame.transform.scale(pygame.image.load(gp.image),(30,30)),(21,1): pygame.transform.scale(pygame.image.load(gp.image),(30,30)),(21,2):pygame.transform.scale(pygame.image.load(gp.image),(30,30)),
(21,3): pygame.transform.scale(pygame.image.load(gpB.image),(30,30)),(21,4): pygame.transform.scale(pygame.image.load(gkn.image),(30,30)),(21,5): pygame.transform.scale(pygame.image.load(gkn.image),(30,30)),
(21,6): None,(21,7): None,(21,8): None,(21,9): None,(21,10): None,(21,11): None,(21,12): None,
(21,13):  pygame.transform.scale(pygame.image.load(up.image),(30,30)),(21,14):  pygame.transform.scale(pygame.image.load(ukn.image),(30,30)),(21,15):  pygame.transform.scale(pygame.image.load(uq.image),(30,30)),
(22,0):  pygame.transform.scale(pygame.image.load(gr.image),(30,30)),(22,1):  pygame.transform.scale(pygame.image.load(gb.image),(30,30)),(22,2):  pygame.transform.scale(pygame.image.load(gq.image),(30,30)),
(22,3):  pygame.transform.scale(pygame.image.load(gk.image),(30,30)),(22,4):  pygame.transform.scale(pygame.image.load(gb.image),(30,30)),(22,5):  pygame.transform.scale(pygame.image.load(gr.image),(30,30)),
(22,6): None,(22,7): None,(22,8): None,(22,9): None,(22,10): None,(22,11): None,(22,12): None,
(22,13):  pygame.transform.scale(pygame.image.load(up.image),(30,30)),(22,14):  pygame.transform.scale(pygame.image.load(ur.image),(30,30)),(22,15):  pygame.transform.scale(pygame.image.load(ub.image),(30,30)),}


def create_board(board):
    board[0][0] = Piece('y', 'r', 'y_rook.png',False)
    board[1][0] = Piece('y', 'b', 'y_bishop.png',False)
    board[2][0] = Piece('y', 'q', 'y_king.png',False)
    board[3][0] = Piece('y', 'k', 'y_queen.png',False)
    board[4][0] = Piece('y', 'b', 'y_bishop.png',False)
    board[5][0] = Piece('y', 'r', 'y_rook.png',False)

    board[0][1] = Piece('y', 'p', 'y_pawn.png',False)
    board[1][1] = Piece('y', 'p', 'y_pawn.png',False)
    board[2][1] = Piece('y', 'p', 'y_pawn.png',False)
    board[3][1] = Piece('y', 'p', 'y_pawn.png',True)
    board[4][1] = Piece('y', 'kn', 'y_knight.png',False)
    board[5][1] = Piece('y', 'kn', 'y_knight.png',False)

    board[0][21] = Piece('g', 'p', 'g_pawn.png',False)
    board[1][21] = Piece('g', 'p', 'g_pawn.png',False)
    board[2][21] = Piece('g', 'p', 'g_pawn.png',False)
    board[3][21] = Piece('g', 'p', 'g_pawn.png',True)
    board[4][21] = Piece('g', 'kn', 'g_knight.png',False)
    board[5][21] = Piece('g', 'kn', 'g_knight.png',False)

    board[0][22] = Piece('g', 'r', 'g_rook.png',False)
    board[1][22] = Piece('g', 'b', 'g_bishop.png',False)
    board[2][22] = Piece('g', 'q', 'g_queen.png',False)
    board[3][22] = Piece('g', 'k', 'g_king.png',False)
    board[4][22] = Piece('g', 'b', 'g_bishop.png',False)
    board[5][22] = Piece('g', 'r', 'g_rook.png',False)

    board[14][7] = Piece('w', 'kn', 'w_knight.png',False)
    board[14][8] = Piece('w', 'kn', 'w_knight.png',False)
    board[14][9] = Piece('w', 'p', 'w_pawnDynamite.png',True)
    board[14][10] = Piece('w', 'p', 'w_pawn.png',False)
    board[14][11] = Piece('w', 'p', 'w_pawn.png',False)
    board[14][12] = Piece('w', 'p', 'w_pawn.png',False)
    board[14][4] = Piece('b', 'kn', 'b_knight.png',False)
    board[14][5] = Piece('b', 'kn', 'b_knight.png',False)

    board[15][7] = Piece('w', 'r', 'w_rook.png',False)
    board[15][8] = Piece('w', 'b', 'w_bishop.png',False)
    board[15][9] = Piece('w', 'k', 'w_king.png',False)
    board[15][10] = Piece('w', 'q', 'w_queen.png',False)
    board[15][11] = Piece('w', 'b', 'w_bishop.png',False)
    board[15][12] = Piece('w', 'r', 'w_rook.png',False)

    board[14][4] = Piece('b', 'kn', 'b_knight.png',False)
    board[14][5] = Piece('b', 'kn', 'b_knight.png',False)


    board[14][0] = Piece('b', 'p', 'b_pawn.png',False)
    board[14][1] = Piece('b', 'p', 'b_pawn.png',False)
    board[14][2] = Piece('b', 'p', 'b_pawn.png',False)
    board[14][3] = Piece('b', 'p', 'b_pawnDynamite.png',True)


    board[15][4] = Piece('b', 'b', 'b_bishop.png',False)
    board[15][5] = Piece('b', 'r', 'b_rook.png',False)
    board[15][0] = Piece('b', 'r', 'b_rook.png',False)
    board[15][1] = Piece('b', 'b', 'b_bishop.png',False)
    board[15][2] = Piece('b', 'q', 'b_queen.png',False)
    board[15][3] = Piece('b', 'k', 'b_king.png',False)




    board[13][14] = Piece('r', 'p', 'r_pawnDynamite.png',True)
    board[13][15] = Piece('r', 'p', 'r_pawn.png',False)
    board[13][16] = Piece('r', 'p', 'r_pawn.png',False)
    board[13][17] = Piece('r', 'p', 'r_pawn.png',False)


    board[14][14] = Piece('r', 'r', 'r_rook.png',False)
    board[14][15] = Piece('r', 'kn', 'r_knight.png',False)
    board[14][16] = Piece('r', 'kn', 'r_knight.png',False)
    board[14][17] = Piece('r', 'r', 'r_rook.png',False)
    board[15][14] = Piece('r', 'b', 'r_bishop.png',False)
    board[15][15] = Piece('r', 'k', 'r_king.png',False)
    board[15][16] = Piece('r', 'q', 'r_queen.png',False)
    board[15][17] = Piece('r', 'b', 'r_bishop.png',False)

    board[13][19] = Piece('u', 'p', 'u_pawn.png',True)
    board[13][20] = Piece('u', 'p', 'u_pawn.png',False)
    board[13][21] = Piece('u', 'p', 'u_pawn.png',False)
    board[13][22] = Piece('u', 'p', 'u_pawn.png',False)


    board[14][19] = Piece('u', 'r', 'u_rook.png',False)
    board[14][20] = Piece('u', 'kn', 'u_knight.png',False)
    board[14][21] = Piece('u', 'kn', 'u_knight.png',False)
    board[14][22] = Piece('u', 'r', 'u_rook.png',False)
    board[15][19] = Piece('u', 'b', 'u_bishop.png',False)
    board[15][20] = Piece('u', 'k', 'u_king.png',False)
    board[15][21] = Piece('u', 'q', 'u_queen.png',False)
    board[15][22] = Piece('u', 'b', 'u_bishop.png',False)
    return board


## returns the input if the input is within the boundaries of the board
def on_board(position):
    if position[0] > -1 and position[1] > -1 and position[0] < 16 and position[1] < 23:
        return True
walls = [[6,0],[6,1],[6,2],[6,3],[7,3],[8,3],[9,3], [0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],[0,11],[1,11],[2,11],[3,11],[4,11],[0,12],[1,12],[2,12],[3,12],[4,12],[0,13],[1,13],
[2,13],[3,13],[4,13],[0,14],[1,14],[2,14],[3,14],[4,14],[0,15],[1,15],[2,15],[3,15],[4,15],[4,9],[5,9],[6,9],[4,10],[5,10],[6,10],[5,11],[6,11],[5,14],[6,14],[5,15],[6,15], [6,18],[6,19],[6,20],[6,21],[6,22],[9,6],[10,6],[11,6],[12,6],[13,6],[14,6],[15,6],[9,9],[9,10],[9,11],[9,12],[9,13],[10,13],[11,13],[12,13],[13,13],[14,13],[15,13],[9,16],[9,17],[9,18],[9,19],[9,20],[10,18],[11,18],[12,18],[13,18],[14,18],[15,18]]
def check_wall(position):

    if [position[0],position[1]] not in walls:
        return True

## returns a string that places the rows and columns of the board in a readable manner
def convert_to_readable(board):
    output = ''

    for i in board:
        for j in i:
            try:
                output += j.team + j.type + ', '
            except:
                output += j + ', '
        output += '\n'
    return output


## resets "x's" and killable pieces
def deselect():
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 'x ':
                board[row][column] = '  '
            else:
                try:
                    board[row][column].killable = False
                except:
                    pass
    return convert_to_readable(board)


## Takes in board as argument then returns 2d array containing positions of valid moves
def highlight(board):
    highlighted = []
    for i in range(len(board) ):
        for j in range(len(board[0])):
            if board[i][j] == 'x ':
                highlighted.append((i, j))
            else:
                try:
                    if board[i][j].killable:
                        highlighted.append((i, j))
                except:
                    pass
    return highlighted

def check_team(moves, index):
    row, col = index
    print(moves)

    if moves%6 == 0:
        if board[row][col].team == 'w':
                return True
    elif moves%6 == 1:
        if board[row][col].team == 'b':
            return True
    elif moves%6 == 2:
        if board[row][col].team == 'y':
            return True
    elif moves%6 == 3:
        if board[row][col].team == 'g':
                 return True
    elif moves%6 == 4:
        if board[row][col].team == 'u':
            return True
    elif moves%6 == 5:
        if board[row][col].team == 'r':
            return True

## This takes in a piece object and its index then runs then checks where that piece can move using separately defined functions for each type of piece.
def select_moves(piece, index, moves):
    if check_team(moves, index):

        if piece.type == 'p':
            if piece.team == 'b':
                return highlight(pawn_moves_b(index))
            else:
                return highlight(pawn_moves_w(index))

        if piece.type == 'k':
            return highlight(king_moves(index))

        if piece.type == 'r':
            return highlight(rook_moves(index))

        if piece.type == 'b':
            return highlight(bishop_moves(index))

        if piece.type == 'q':
            return highlight(queen_moves(index))

        if piece.type == 'kn':
            return highlight(knight_moves(index))


## Basically, check black and white pawns separately and checks the square above them. If its free that space gets an "x" and if it is occupied by a piece of the opposite team then that piece becomes killable.
def pawn_moves_b(index):


    bottom3 = [[(index[0]+1),(index[1] +1)],[(index[0]+1),(index[1] -1)],[(index[0]-1),(index[1] +1)],[(index[0]-1),(index[1] -1)],[(index[0]+1),(index[1])],[(index[0]),(index[1] +1)],[(index[0]-1),index[1]],[index[0],index[1]-1]]

    for positions in bottom3:
        if on_board(positions) and check_wall(positions):
            if board[positions[0]][positions[1]] == '  ':
                board[positions[0]][positions[1]] = 'x '
            elif (board[positions[0]][positions[1]].team != board[index[0]][index[1]].team):
                board[positions[0]][positions[1]].killable = True
    return board

def pawn_moves_w(index):

    top3 = [[(index[0]+1),(index[1] +1)],[(index[0]+1),(index[1] -1)],[(index[0]-1),(index[1] +1)],[(index[0]-1),(index[1] -1)],[(index[0]+1),(index[1])],[(index[0]),(index[1] +1)],[(index[0]-1),index[1]],[index[0],index[1]-1]]

    for positions in top3:
        if on_board(positions):
            if board[index[0]][index[1]].dynamite:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                elif (board[positions[0]][positions[1]].team != board[index[0]][index[1]].team):
                    board[positions[0]][positions[1]].killable = True
            elif(check_wall(positions)):
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                elif (board[positions[0]][positions[1]].team != board[index[0]][index[1]].team):
                    board[positions[0]][positions[1]].killable = True


    return board



## This just checks a 3x3 tile surrounding the king. Empty spots get an "x" and pieces of the opposite team become killable.
def king_moves(index):
    for y in range(3):
        for x in range(3):
            if on_board((index[0] - 1 + y, index[1] - 1 + x)) and check_wall((index[0] - 1 + y, index[1] - 1 + x)):
                if board[index[0] - 1 + y][index[1] - 1 + x] == '  ':
                    board[index[0] - 1 + y][index[1] - 1 + x] = 'x '
                else:
                    if board[index[0] - 1 + y][index[1] - 1 + x].team != board[index[0]][index[1]].team:
                        board[index[0] - 1 + y][index[1] - 1 + x].killable = True
    return board


## This creates 4 lists for up, down, left and right and checks all those spaces for pieces of the opposite team. The list comprehension is pretty long so if you don't get it just msg me.
def rook_moves(index):
    cross = [[[index[0] + i, index[1]] for i in range(1, 17)],
             [[index[0] - i, index[1]] for i in range(1,17)],
             [[index[0], index[1] + i] for i in range(1, 24)],
             [[index[0], index[1] - i] for i in range(1, 24)]]

    for direction in cross:
        for positions in direction:
            if on_board(positions) and board[index[0]][index[1]].dynamite:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                else:
                    if board[positions[0]][positions[1]].team != board[index[0]][index[1]].team:
                        board[positions[0]][positions[1]].killable = True
                    break
            elif(check_wall(positions) and on_board(positions)):
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                else:
                    if (board[positions[0]][positions[1]].team != board[index[0]][index[1]].team):
                        board[positions[0]][positions[1]].killable = True
                    break
            else:
                break
    return board


## Same as the rook but this time it creates 4 lists for the diagonal directions and so the list comprehension is a little bit trickier.
def bishop_moves(index):
    diagonals = [[[index[0] - i,index[1] + i] for i in range(1,23)],
                [[index[0] - i,index[1] - i] for i in range(1,23)],
                [[index[0] + i,index[1] + i] for i in range(1,23)],
                [[index[0] + i,index[1] - i] for i in range(1,23)]]

    for dia in diagonals:
        for positions in dia:

            if on_board(positions) and board[index[0]][index[1]].dynamite:

                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '

                else:
                    if (board[positions[0]][positions[1]].team != board[index[0]][index[1]].team):
                        board[positions[0]][positions[1]].killable = True
                    break
            elif (on_board(positions) and check_wall(positions)):
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '

                else:
                    if (board[positions[0]][positions[1]].team != board[index[0]][index[1]].team):
                        board[positions[0]][positions[1]].killable = True
                    break
            else:
                break

    return board


## applies the rook moves to the board then the bishop moves because a queen is basically a rook and bishop in the same position.
def queen_moves(index):
    board = rook_moves(index)
    board = bishop_moves(index)
    return board



## Checks a 5x5 grid around the piece and uses pythagoras to see if if a move is valid. Valid moves will be a distance of sqrt(5) from centre
def knight_moves(index):

    knight_moves = [[(index[0]-2),(index[1] +1)], [(index[0]-2),(index[1]-1)],[(index[0]-1), (index[1] + 2)],[(index[0]-1), (index[1] - 2)],[(index[0] + 1),(index[1] - 2)], [(index[0]+2),(index[1]-1)], [(index[0]+1),(index[1]+2)],[(index[0]+2),(index[1]+1)]]
    for move in knight_moves:
        if on_board(move) and check_wall(move) :

            if board[move[0]][move[1]] == '  ':
                board[move[0]][move[1]] = 'x '

            elif (board[move[0]][move[1]].team != board[index[0]][index[1]].team):
                board[move[0]][move[1]].killable = True


    return board


WIDTH = 800

WIN = pygame.display.set_mode((780, 560))

""" This is creating the window that we are playing on, it takes a tuple argument which is the dimensions of the window so in this case 800 x 800px
"""

pygame.display.set_caption("Chess")
WHITE = (236, 222, 183)
GREY = (137, 115, 91)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)


class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(row * width)
        self.y = int(col * width)
        self.colour = WHITE
        self.occupied = None


    def draw(self, WIN):
        pygame.draw.rect(WIN, self.colour, (self.x, self.y, WIDTH / 23, WIDTH / 23))

    def drawWall(self, WIN):
        pygame.draw.rect(WIN, BLACK, (self.x, self.y, WIDTH / 23, WIDTH / 23))
    def setup(self, WIN):
        if starting_order[(self.row, self.col)]:
            if starting_order[(self.row, self.col)] == None:
                pass
            else:
                WIN.blit(starting_order[(self.row, self.col)], (self.x, self.y))

        """
        For now it is drawing a rectangle but eventually we are going to need it
        to use blit to draw the chess pieces instead
        """


def make_grid(rows, width):
    grid = []
    gap = WIDTH // rows


    for i in range(16):
        grid.append([])
        for j in range(rows):
            node = Node(j, i, gap)
            grid[i].append(node)
            if [i,j] not in walls:
                if (i+j)%2 ==1:
                    grid[i][j].colour = GREY
            else:
                grid[i][j].colour = BLACK
    return grid
"""
This is creating the nodes thats are on the board(so the chess tiles)
I've put them into a 2d array which is identical to the dimesions of the chessboard
"""


def draw_grid(win, rows, width):
    gap = width // 23
    for i in range(16):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))

    """
    The nodes are all white so this we need to draw the grey lines that separate all the chess tiles
    from each other and that is what this function does"""


def update_display(win, grid, rows, width):

    for row in grid:
        for spot in row:
            if([spot.col, spot.row] not in walls):
                spot.draw(win)
                spot.setup(win)
            else:
                spot.drawWall(win)
                spot.setup(win)
    draw_grid(win, rows, width)


    pygame.display.update()


def Find_Node(pos, WIDTH):
    interval = 790 // 23
    y, x = pos
    rows = y // (560 // 16)
    columns = x // interval

    return int(rows), int(columns)


def display_potential_moves(positions, grid):
    for i in positions:
        x, y = i
        grid[x][y].colour = BLUE
        """
        Displays all the potential moves
        """


def Do_Move(OriginalPos, FinalPosition, WIN):
    starting_order[FinalPosition] = starting_order[OriginalPos]
    starting_order[OriginalPos] = None


def remove_highlight(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i+j)%2 == 0:
                grid[i][j].colour = WHITE
            else:
                grid[i][j].colour = GREY
    return grid
"""this takes in 2 co-ordinate parameters which you can get as the position of the piece and then the position of the node it is moving to
you can get those co-ordinates using my old function for swap"""

create_board(board)


def main(WIN, WIDTH):
    moves = 0
    selected = False
    piece_to_move=[]
    grid = make_grid(23, WIDTH)
    while True:
        pygame.time.delay(50) ##stops cpu dying
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            """This quits the program if the player closes the window"""

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                y, x = Find_Node(pos, WIDTH)

                if selected == False:
                    try:

                        possible = select_moves((board[x][y]), (x,y), moves)

                        for positions in possible:
                            row, col = positions

                            grid[row][col].colour = BLUE
                        piece_to_move = x,y
                        selected = True
                    except:
                        piece_to_move = []
                        print('Can\'t select')
                    #print(piece_to_move)

                else:
                    try:
                        if board[x][y].killable == True:
                            row, col = piece_to_move ## coords of original piece
                            board[x][y] = board[row][col]
                            board[row][col] = '  '
                            deselect()
                            remove_highlight(grid)
                            Do_Move((col, row), (y, x), WIN)
                            if (board[x][y].type == 'p' and ((x == 5 and y==12 ) or (x == 5 and y==13 ))):
                                board[x][y] =  Piece(board[x][y].team, 'q', board[x][y].team + '_queen.png',board[x][y].dynamite)
                            moves += 1
                            print(convert_to_readable(board))
                        else:
                            deselect()
                            remove_highlight(grid)
                            selected = False
                            print("Deselected")
                    except:
                        if board[x][y] == 'x ':
                            row, col = piece_to_move
                            board[x][y] = board[row][col]
                            board[row][col] = '  '
                            deselect()
                            remove_highlight(grid)
                            if (board[x][y].type == 'p' and ((x == 5 and y==12 ) or (x == 5 and y==13 ))):
                                board[x][y] =  Piece(board[x][y].team, 'q', board[x][y].team + '_queen.png',board[x][y].dynamite)
                                pygame.display.update()
                            if not (check_wall([x,y])) and board[x][y].dynamite:
                                walls.remove([x,y])
                                board[x][y].dynamite = False

                            Do_Move((col, row), (y, x), WIN)

                            moves += 1
                            print(convert_to_readable(board))

                        else:
                            deselect()
                            remove_highlight(grid)
                            selected = False
                            print("Invalid move")
                    selected = False

            update_display(WIN, grid, 23, WIDTH)


main(WIN, WIDTH)
