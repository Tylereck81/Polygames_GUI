import pygame 


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



Xoffset = 200
Yoffset = 50
#Othello 8X8 and Breakthrough 
def drawboard(n):
    if n == 8:
        for x in range(1, n+1):
            for y in range(1, n+1):
                if x % 2 != 0:
                    if y % 2 != 0:
                        pygame.draw.rect(breakthrough.screen, white_square, [squaresize * (x - 1) +Xoffset , squaresize * (y - 1)+Yoffset,
                                                                squaresize, squaresize])
                    else:
                        pygame.draw.rect(breakthrough.screen, black_square, [squaresize * (x - 1)+Xoffset, squaresize * (y - 1)+Yoffset,
                                                                squaresize, squaresize])
                else:
                    if y % 2 != 0:
                        pygame.draw.rect(breakthrough.screen, black_square, [squaresize * (x - 1)+Xoffset, squaresize * (y - 1)+Yoffset,
                                                                squaresize, squaresize])
                    else:
                        pygame.draw.rect(breakthrough.screen, white_square, [squaresize * (x - 1)+Xoffset, squaresize * (y - 1)+Yoffset,
                                                                squaresize, squaresize])


#acually draws image onto the board 
def drawPieces(layout_file):
    global position_list
    position_list=[]
    for i in range(8):
        for j in range(8):
            if layout_file[j][i]=='@':
                breakthrough.screen.blit(player_piece,(i*squaresize+Xoffset,j*squaresize+Yoffset))
                position_list.append((i*squaresize+Xoffset, j*squaresize+Yoffset))
            if layout_file[j][i]=='O':
                breakthrough.screen.blit(enemy_piece,(i*squaresize+Xoffset,j*squaresize+Yoffset))
                position_list.append((i*squaresize+Xoffset, j*squaresize+Yoffset))


#used to translate the mouse position board place values into legal move positions ex a8
def determine_position(position_x, position_y):
    x=''
    y=''
    if position_x>=0+Xoffset and position_x<=60+Xoffset:
        x='a'
    elif position_x>60+Xoffset and position_x<=120+Xoffset:
        x='b'
    elif position_x>120+Xoffset and position_x<=180+Xoffset:
        x='c'
    elif position_x>180+Xoffset and position_x<=240+Xoffset:
        x='d'
    elif position_x>240+Xoffset and position_x<=300+Xoffset:
        x='e'
    elif position_x>300+Xoffset and position_x<=360+Xoffset:
        x='f'
    elif position_x>360+Xoffset and position_x<=420+Xoffset:
        x='g'
    elif position_x>420 +Xoffset and position_x<=480+Xoffset:
        x='h'

    if position_y>=0+Yoffset and position_y<=60+Yoffset:
        y='8'
    elif position_y>60+Yoffset and position_y<=120+Yoffset:
        y='7'
    elif position_y>120+Yoffset and position_y<=180+Yoffset:
        y='6'
    elif position_y>180+Yoffset and position_y<=240+Yoffset:
        y='5'
    elif position_y>240+Yoffset and position_y<=300+Yoffset:
        y='4'
    elif position_y>300+Yoffset and position_y<=360+Yoffset:
        y='3'
    elif position_y>360+Yoffset and position_y<=420+Yoffset:
        y='2'
    elif position_y>420+Yoffset and position_y<=480+Yoffset:
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
        breakthrough.screen.blit(legal_move_indicator, (y*squaresize+Xoffset,x*squaresize+Yoffset))
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

#checks if any player won the game and returns 1 if human won and -1 if computer won and 0 if none 
def check_winner(): 
    layout,r,c=read_file(board_file)
    i_FLAG = 0 
    j_FLAG = 0 
    for i in range(r): 
        for j in range(c): 
            if i == 0: #checks if computer got to our side 
                if layout[i][j] == "O":
                    j_FLAG = -1
                    i_FLAG = 1
                    break 
            
            elif i == 7: #checks if computer got to our side 
                if layout[i][j] == "@":
                    j_FLAG = 1
                    i_FLAG = 1
                    break 
        if i_FLAG == 1:
            break
    
    return j_FLAG 



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

#loading image files of each object in the game 
player_piece=pygame.image.load("black_piece.png") #BLACK piece
enemy_piece=pygame.image.load("white_piece.png") #WHITE piece 
selection=pygame.image.load("selection.png") #red border 
legal_move_indicator=pygame.image.load("move_indicator.png") #red circle 


#loads board file and move list
board_file="board_test3.txt"
move_file="moves_list.txt"


def run_breakthrough():
    layout,r,c=read_file(board_file)
    if check_winner() == 0: #found no winners so we run game loop 
        drawboard(8)
        drawPieces(layout)
        move_list=get_moves(move_file)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return False, False  #if they quit then return false 
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                result, selection_xy=isPiecePresent(x,y)
                position=determine_position(x,y)
                if result==True:
                    determine_position_reverse(position, move_list)
                    input_move=position
                    move=True
                    while move:
                        breakthrough.screen.blit(selection, selection_xy)
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type==pygame.MOUSEBUTTONDOWN:
                                x2,y2=pygame.mouse.get_pos()
                                p2=determine_position(x2,y2)
                                if position==p2:
                                    move=False
                                else:
                                    input_move+=p2
                                    move=False
                                    print(input_move)
                                    output_file=open("../output.txt", "w")
                                    output_file.write(input_move)
                                    output_file.close()
        pygame.display.update() 
        return True, False
    else: 
        drawboard(8)
        drawPieces(layout)
        if check_winner() == 1:
            breakthrough.draw_text("HUMAN WON",20,W/2,H/2)
        elif check_winner() == -1: 
            breakthrough.draw_text("COMPUTER WON",20,W/2,H/2)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return False, False  #if they quit then return false
        pygame.display.update()  
        return True, False 


#keeps checking if the return button was pressed or focussed on in each game. If it is, it exits game loop and switches screens 
def ingame_check_press(curr_screen):
    curr_screen.screenUpdate()
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    return_b = returnButton.focusCheck(mouse_pos,mouse_click)
    returnButton.showButton(curr_screen.returnTitle())
    if return_b: 
        win = menuScreen.makeCurrent() 
        curr_screen.endCurrent() 
        return False 
    
    return True

#checks to see if any of the game loops have been entered and runs it if so 
def game_loop_check(game, game_button,Playing): 
    screen2Button = game_button.focusCheck(mouse_pos,mouse_click)
    game_button.showButton(menuScreen.returnTitle())

    if screen2Button: 
        win = game.makeCurrent()
        menuScreen.endCurrent() 
        flag = 0
        while Playing:
            Playing = ingame_check_press(game)
            Winning = 0 
            if Playing:  #if return button was not pressed then we check if game is done because someone won 
                Playing, Winning = run_game(game)
                if Winning == 1: 
                    print("Human won")
                elif Winning == -1: 
                    print("Computer won")    
        

def run_game(game): 
    if game == breakthrough: 
        return run_breakthrough()
    elif game == othello: 
        return run_othello() 
    elif game == minishogi: 
        return run_minishogi()
    elif game == einstein: 
        return run_einstein() 

def run_othello(): 
    #print("in othello")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            return False, False 
    pygame.display.update() 
    return True, False 
    

def run_minishogi(): 
    #print("in minishogi") 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            return False, False 
    pygame.display.update() 
    return True, False 

def run_einstein(): 
    #print("in einstein")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            return False, False 
    pygame.display.update() 
    return True, False 




colours ={"White": (255,255,255), "Black": (0,0,0), "Red": (255,0,0), "Green":(0,255,0), "Blue":(0,0,255)}

W = 880 
H = 580 
class Screen(): 
    def __init__(self, title, width = W, height = H, fill = colours["White"]): 
        self.title = title
        self.width = width 
        self.height = height 
        self.fill = fill
        self.current = False 

    def  makeCurrent(self): 
        pygame.display.set_caption(self.title)
        self.current = True 
        self.screen = pygame.display.set_mode((self.width, self.height))
    
    def endCurrent(self): 
        self.current = False 
    
    def checkUpdate(self): 
        return self.current 
    
    def screenUpdate(self): 
        if(self.current): 
            self.screen.fill(self.fill)
            background = pygame.image.load("background.jpg")
            self.screen.blit(background,(0,0))
    
    def returnTitle(self): 
        return self.screen 
    
    #used to draw text to any screen 
    def draw_text(self,text, size, x,y): 
        font = pygame.font.SysFont(pygame.font.get_default_font(),size)
        text_surface = font.render(text, True, colours["White"])
        text_rect = text_surface.get_rect() 
        text_rect.center = (x,y)
        #self.screenUpdate()
        self.screen.blit(text_surface,text_rect)



class Button(): 
    def __init__(self,x,y,sx,sy,bcolor,fbcolor,font,fontsize,fcolor,text):
        self.x = x 
        self.y = y 
        self.sx = sx
        self.sy = sy 
        self.bcolor = bcolor
        self.fbcolor = fbcolor 
        self.fontsize = fontsize 
        self.fcolor = fcolor 
        self.text = text 
        self.current = False 
        self.buttonf = pygame.font.SysFont(font,fontsize)
    
    def showButton(self, display): 
        if(self.current): 
            pygame.draw.rect(display, self.fbcolor,(self.x,self.y, self.sx, self.sy)) 

        else: 
            pygame.draw.rect(display,self.bcolor, (self.x,self.y, self.sx, self.sy))

        textsurface = self.buttonf.render(self.text, False, self.fcolor)
        display.blit(textsurface,((self.x + (self.sx/2) - (self.fontsize/2)*(len(self.text)/2) -5, (self.y +(self.sy/2) - (self.fontsize/2)-4))))

    def focusCheck(self, mousepos, mouseClick): 
        if(mousepos[0] >=self.x and mousepos[0]<=self.x +self.sx and mousepos[1] >=self.y and mousepos[1] <= self.y +self.sy):
            self.current = True 
            return mouseClick[0] 
        else:
            self.current = False
            return False   



pygame.init()
pygame.font.init()


#creates the different Screens 
menuScreen = Screen("Polygame: Menu")
breakthrough = Screen("Polygame: Breakthrough")
othello = Screen("Polygame: Othello")
minishogi = Screen("Polygame: MiniShogi") 
einstein = Screen("Polygame: Einstein")

win = menuScreen.makeCurrent()  #set initial screen to MenuScreen 

breakthrough_button = Button(W/2,0,100,50, colours["Black"], colours["Red"],"arial",20,colours["White"],"Breakthrough")
othello_button = Button(W/2,100,100,50, colours["Black"], colours["Red"],"arial",20,colours["White"],"Othello") 
minishogi_button = Button(W/2,200,100,50, colours["Black"], colours["Red"],"arial",20,colours["White"],"Minishogi")
einstein_button = Button(W/2, 300,100,50, colours["Black"], colours["Red"],"arial",20,colours["White"],"Einstein")

returnButton = Button(480,0,100,50, colours["White"], colours["Blue"],"arial",20,colours["Black"],"Return")

#First Go, Menu runs but not playing. When a button for the game is pressed, the game loop is then entered 
Running = True 
while Running: 
    menuScreen.screenUpdate()
    breakthrough.screenUpdate()
    othello.screenUpdate()
    minishogi.screenUpdate()
    einstein.screenUpdate()

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    if menuScreen.checkUpdate(): 
        
        #breakthrough
        game_loop_check(breakthrough,breakthrough_button,True) 
        #Othello 
        game_loop_check(othello,othello_button,True) 
        #Minishogi
        game_loop_check(minishogi,minishogi_button,True)
        #Einstein 
        game_loop_check(einstein,einstein_button,True) 
        
    for event in pygame.event.get(): 
        if(event.type == pygame.QUIT):
            Running = False
    pygame.display.update() 

pygame.quit() 


