import pygame

#Test Change variable 


# Add undo button 
# Add submit button
#Show chess count 
#Position grid
#Add piece highlight, highlight legal positions andd fade illegal moves 
pygame.init()


#reads the move list file and creates a list of moves (Breakthrough and MiniShogi)
def get_moves(move_list_file):
    with open (move_list_file, 'r') as m:
        moves=m.read().split()
        
    return moves

#othello doesnt have move list file so we go through the board and find which spot where it has ?
def get_moves_othello(board_list, r, c): 
    moves=[]
    for i in range(0,r): 
        n = 0
        for j in range(1,c,2): 
            if(board_list[i][j]=="?"): 
                #want to get location 
                moves.append(position_letter_grid[i][n])
            n+=1
    return moves
    


# reads in a boardfile as a file and returns a 2 dimensional array of the board 
def read_file(boardfile):

    #gets first line number to check what board we are reading 
    with open(boardfile, 'r') as l:
        firstline = l.readline()
    
    if firstline == "1\n": #MiniShogi 
        numlist=123456789
        l=[]
        l2=[]
        r1=0 #holds row count 
        c1=0 #holds col count 
        cflag = 0 
        c=0 #holds temp col count 
        with open(boardfile, 'r') as f:
            board_layout=f.read()
            for j in range(19, 104): #starting and ending values start at 3rd row and end at 7th row  
                if(board_layout[j]!='\n' and board_layout[j] not in str(numlist) and j%17 !=4):
                    l2.append(board_layout[j]) 
                    c+=1
                elif(board_layout[j]=='\n'): #when the end of line is reached we increment the row and append list l2 into main list l
                    if c!=0:
                        l.append(l2)
                        l2=[]
                        r1+=1
                        if cflag == 0:  #holds column count one time before resetting back to 0 
                            cflag = 1 
                            c1 = c
                            c = 0
                        else:
                            c = 0
        return l,r1,c1

    elif firstline == "2\n": #Othello 
        numlist=123456789
        alist = "qwertyuipasdfghjklzxcvnmo" 
        l=[]
        l2=[]
        r1=0 #holds row count 
        c1=0 #holds col count 
        cflag = 0 
        c=0 #holds temp col count 
        with open(boardfile, 'r') as f:
            board_layout=f.read()
            FILE_SIZE = len(board_layout)
            print(FILE_SIZE)
            for j in range(FILE_SIZE):
                if(board_layout[j]!=' ' and board_layout[j]!='\n' and board_layout[j] not in str(numlist) and board_layout[j] not in str(alist) and board_layout[j] not in str(alist).upper()):
                    l2.append(board_layout[j]) 
                    c+=1
                elif(board_layout[j]=='\n'): #when the end of line is reached we increment the row and append list l2 into main list l
                    if c!=0:
                        l.append(l2)
                        l2=[]
                        r1+=1
                        if cflag == 0:  #holds column count one time before resetting back to 0 
                            cflag = 1 
                            c1 = c
                            c = 0
                        else:
                            c = 0
        return l,r1,c1
    elif firstline == "3\n": #Breakthrough 
        numlist=123456789
        alist = "qwertyuipasdfghjklzxcvnmb" #without "O" for breakthrough
        l=[]
        l2=[]
        r1=0 #holds row count 
        c1=0 #holds col count 
        cflag = 0 
        c=0 #holds temp col count 
        with open(boardfile, 'r') as f:
            board_layout=f.read()
            FILE_SIZE = len(board_layout)
            print(FILE_SIZE)
            for j in range(FILE_SIZE):
                if(board_layout[j]!=' ' and board_layout[j]!='\n' and board_layout[j] not in str(numlist) and board_layout[j] not in str(alist) and board_layout[j] not in str(alist).upper()):
                    l2.append(board_layout[j]) 
                    c+=1
                elif(board_layout[j]=='\n'): #when the end of line is reached we increment the row and append list l2 into main list l
                    if c!=0:
                        l.append(l2)
                        l2=[]
                        r1+=1
                        if cflag == 0:  #holds column count one time before resetting back to 0 
                            cflag = 1 
                            c1 = c
                            c = 0
                        else:
                            c = 0
        return l,r1,c1



#pygame shit that is predefined that akeem did not have to think about 
def drawboard(n):
    if n == 8:
        screen.fill(menu_area_color)
        for x in range(1, n+1):
            for y in range(1, n+1):
                if x % 2 != 0:
                    if y % 2 != 0:
                        pygame.draw.rect(screen, white_square, [squaresize * (x - 1), squaresize * (y - 1),
                                                                squaresize, squaresize])
                    else:
                        pygame.draw.rect(screen, black_square, [squaresize * (x - 1), squaresize * (y - 1),
                                                                squaresize, squaresize])
                else:
                    if y % 2 != 0:
                        pygame.draw.rect(screen, black_square, [squaresize * (x - 1), squaresize * (y - 1),
                                                                squaresize, squaresize])
                    else:
                        pygame.draw.rect(screen, white_square, [squaresize * (x - 1), squaresize * (y - 1),
                                                                squaresize, squaresize])

#acually draws image onto the board 
def drawPieces(layout_file):
    global position_list
    position_list=[]
    for i in range(8):
        for j in range(8):
            if layout_file[j][i]=='@':
                screen.blit(player_piece,(i*squaresize,j*squaresize))
                position_list.append((i*squaresize, j*squaresize))
            if layout_file[j][i]=='O':
                screen.blit(enemy_piece,(i*squaresize,j*squaresize))
                position_list.append((i*squaresize, j*squaresize))


#used to translate the mouse position board place values into legal move positions ex a8
def determine_position(position_x, position_y):
    x=''
    y=''
    if position_x>=0 and position_x<=60:
        x='a'
    elif position_x>60 and position_x<=120:
        x='b'
    elif position_x>120 and position_x<=180:
        x='c'
    elif position_x>180 and position_x<=240:
        x='d'
    elif position_x>240 and position_x<=300:
        x='e'
    elif position_x>300 and position_x<=360:
        x='f'
    elif position_x>360 and position_x<=420:
        x='g'
    elif position_x>420 and position_x<=480:
        x='h'

    if position_y>=0 and position_y<=60:
        y='8'
    elif position_y>60 and position_y<=120:
        y='7'
    elif position_y>120 and position_y<=180:
        y='6'
    elif position_y>180 and position_y<=240:
        y='5'
    elif position_y>240 and position_y<=300:
        y='4'
    elif position_y>300 and position_y<=360:
        y='3'
    elif position_y>360 and position_y<=420:
        y='2'
    elif position_y>420 and position_y<=480:
        y='1'

    return x+y


#moves list translated physically into dots on board to indicate where the specified piece can move 
def determine_position_reverse(letter_co, m_list):
    legal_moves=[] 

#goes through legal moves list and looks at first two letters to determine if the place you are at can move and then stores destination location into legal_moves
    for moves in m_list:
        if letter_co==moves[0:2]:
            legal_moves.append(moves[2:])
    
    #prints out those legal_moves onto board 
    for legal_move in legal_moves:
        x=0
        y=0
        for i in range(8):
            for j in range(8):
                if legal_move == position_letter_grid[i][j]:
                    x=i
                    y=j
        screen.blit(legal_move_indicator, (y*squaresize,x*squaresize))
        pygame.display.update()


def isPiecePresent(x,y):
    present=False
    for px,py in position_list:
        if (x>=px and x<=px+60) and (y>=py and y<=py+60):
            present=True
            selection_coordinates=(px,py)
            break
    if present:
        return present, selection_coordinates
    else:
        return present, (0,0)
        
def draw_numbers_area():
    for i in range(1,9):
        pygame.draw.rect()

#variable section
position_list =[]
move_list=[]
squaresize=60

#color for squares
black_square=(193,154,107)
white_square=(242, 222, 199)
menu_area_color=(72, 77, 72)
color_key=(10,10,10)

#matrix to link moves to i,j position values 
position_letter_grid=[
['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
]

#dependent variables
game_width=squaresize*8
game_height=squaresize*8

screen_width=game_width+100
screen_height=game_height+100

#initialization
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Breakthrough")

#loading image files of each object in the game 
player_piece=pygame.image.load(".\\Desktop\\Pygame\\black_piece.png") #BLACK piece
enemy_piece=pygame.image.load(".\\Desktop\\Pygame\\white_piece.png") #WHITE piece 
#selection=pygame.image.load("selection.png") #red border 
#legal_move_indicator=pygame.image.load("rsrc/move_indicator.png") #red circle 

#loads board files
board_file=".\\Desktop\\Pygame\\board_test2.txt"
#move_file="../move_list.txt"

running=True
moves_gotten=False

# output_file=open("../output.txt", "w")
# output_file.write("0")
# output_file.close()

layout,r,c=read_file(board_file) 
print(r,c)
for i in range(r): 
    for j in range(c): 
        print(layout[i][j],end ="")
    print("")

moves = get_moves_othello(layout,r,c) 
print(moves) 

# while running:
#     layout=read_file(board_file)
#     drawboard()
#     drawPieces(layout)
#     move_list=get_moves(move_file)
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             running=False
#         if event.type==pygame.MOUSEBUTTONDOWN:
#             x,y=pygame.mouse.get_pos()
#             result, selection_xy=isPiecePresent(x,y)
#             position=determine_position(x,y)
#             if result==True:
#                 determine_position_reverse(position, move_list)
#                 input_move=position
#                 move=True
#                 while move:
#                     screen.blit(selection, selection_xy)
#                     pygame.display.update()
#                     for event in pygame.event.get():
#                         if event.type==pygame.MOUSEBUTTONDOWN:
#                             x2,y2=pygame.mouse.get_pos()
#                             p2=determine_position(x2,y2)
#                             if position==p2:
#                                 move=False
#                             else:
#                                 input_move+=p2
#                                 move=False
#                                 print(input_move)
#                                 output_file=open("../output.txt", "w")
#                                 output_file.write(input_move)
#                                 output_file.close()

                                
    
#     pygame.display.update()
# #def main_menu()