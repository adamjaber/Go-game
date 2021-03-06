

import pygame
import Board
import random
from sys import exit

BACKGROUND = 'images/ramin.jpg'
BOARD_SIZE = (1050, 800)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
Color = (205, 92, 92)
Green = (127, 255, 212)
green = (77, 0, 0)

# text counter
player_score = 0
opponent_score = 0
score_ = 0
black=0
white=0




class Stone(Board.Stone):
    def __init__(self, board, point, color):
        """Create, initialize and draw a stone."""
        super(Stone, self).__init__(board, point, color)
        self.coords = (5 + self.point[0] * 40, 5 + self.point[1] * 40)
        game_font = pygame.font.Font("./FreeSansBold11.ttf", 20)
        pygame.draw.rect(screen, Color, (956, 35, 50, 50) )

        score_text_ = game_font.render(f"{score_}/360", False, (0, 0, 0))
        screen.blit(score_text_, (960, 45))
        self.draw()

    def draw(self):
        """Draw the stone as a circle."""
        if self.color == (205, 92, 92):
           print(self.point)
           self.coords = ( -15+self.point[1] * 40, -15+self.point[0] * 40)
           blit_coords = self.coords
           area_rect = pygame.Rect(blit_coords, (40, 40))
           screen.blit(background, blit_coords, area_rect)

           game_font = pygame.font.Font("./FreeSansBold11.ttf", 20)
           # opponent_text
           text2 = game_font.render('White', True, white)
           textRect2 = text2.get_rect()
           textRect2.center = (940, 450)
           screen.blit(text2, textRect2)
           pygame.draw.rect(screen, WHITE, (830, 420, 213, 300))
           screen.blit(text2, textRect2)
           opponent_text = game_font.render(f"{opponent_score}", False, (0, 0, 0))
           screen.blit(opponent_text, (930, 550))

           text = game_font.render('Black', True, Color, black)
           textRect = text.get_rect()
           textRect.center = (940, 150)
           screen.blit(text, textRect)

           pygame.draw.rect(screen, BLACK, (830, 100, 213, 300))
           screen.blit(text, textRect)
           player_text = game_font.render(f"{player_score}", False, (255, 255, 255))
           screen.blit(player_text, (935, 250))

           pygame.display.update()
        else:
            pygame.draw.circle(screen, self.color, self.coords, 20, 0)
            pygame.display.update()


class Board(Board.Board):
    def __init__(self):
        """Create, initialize and draw an empty board."""
        super(Board, self).__init__()
        self.outline = pygame.Rect(45, 45, 720, 720)
        self.draw()

    def draw(self):
        pygame.draw.rect(background, BLACK, self.outline, 3)
        self.outline.inflate_ip(20, 20)
        for i in range(18):
            for j in range(18):
                rect = pygame.Rect(45 + (40 * i), 45 + (40 * j),40,40)
                pygame.draw.rect(background, BLACK, rect, 1)
        for i in range(3):
            for j in range(3):
                coords = (165 + (240 * i), 165 + (240 * j))
                pygame.draw.circle(background, BLACK, coords, 5, 0)
        screen.blit(background, (0, 0))
        pygame.display.update()

#update the side score board black player
def checkifdeletnow_opponent(board,i,j):
    global player_score, opponent_score, score_
    new_result = board.neighbors(i, j, 1)
    if new_result:
         for i in new_result:
          opponent_score += 1
          board.CapturedBlack +=1
          Stone(board, i, Color)
         for i in new_result:
             board.mat[i[0], i[1]] = -1

#update the side score board whitejoe player
def checkifdeletnow_player(board,i,j):
    global player_score, opponent_score, score_
    new_result = board.neighbors(i, j, 2)
    if new_result:
        for i in new_result:
          player_score += 1
          board.CapturedWite +=1
          Stone(board, i, Color)
        for i in new_result:
           board.mat[i[0], i[1]] = -1


# this function is insert a new point to the array and drow the board
def IndexToList(list1, x, y, board):
       global score_
       score_ +=1
       Stone(board, (x, y), board.turn())
       list1.append((x, y))

def CheckIfWin(Stonecolor,board):
    if Stonecolor == 0:
        board.AddBlack()
    else:
        board.AddWhite()
    print("total rounds is:",board.ToatalRounds)
    if board.ToatalRounds ==360:                          #total round to finish the game
        FinishGame(board)
    return 1

# this function is Checking if the point is exist in the board or not
def if_not_exist_in_list(list1 , x , y):
    for i in list1:
        if i == (x, y):
            return 0    # this happens when we try to add stone on to of another
    return 1

"""Calgorithm for easy mode just finds random numbers"""
def random_number(list1,board):
    i = 1
    while i == 1:
        n = random.randint(1, 19)
        n1 = random.randint(1, 19)
        if (if_not_exist_in_list(list1,n,n1)):
            return (n,n1)

"""algorithm for hardMode"""
def hard_mode(list1,board):
    i=1
    for x in range (2,18):
        for y in range(2,18):
            if board.mat[y][x] == 1:
                if board.mat[y][x+1]== 0 and if_not_exist_in_list(list1,x+1,y):
                    return(x+1,y)
                if board.mat[y][x-1]== 0 and if_not_exist_in_list(list1,x-1,y):
                    return(x-1,y)
                if board.mat[y+1][x]== 0 and if_not_exist_in_list(list1,x,y+1):
                    return(x,y+1)
                if board.mat[y-1][x]== 0 and if_not_exist_in_list(list1,x,y-1):
                    return(x,y-1)  
def  drow_the_board(list1,event ,board ,mode):
    global player_score,opponent_score,score_
    turn = 0
    x = int(round(((event.pos[0] - 5) / 40.0), 0))
    y = int(round(((event.pos[1] - 5) / 40.0), 0))
    if (if_not_exist_in_list(list1, x, y) and turn == 0):
        #side screen that shows score of each player
        pygame.draw.line(screen, (0, 0, 0), (890, 120), (890, 180), 2)
        pygame.draw.line(screen, (0, 0, 0), (985, 120), (985, 180), 2)
        pygame.draw.line(screen, (0, 0, 0), (890, 120), (985, 120), 2)
        pygame.draw.line(screen, (0, 0, 0), (890, 180), (985, 180), 2)

        pygame.draw.line(screen, (0, 0, 0), (890, 425), (890, 485), 2)
        pygame.draw.line(screen, (0, 0, 0), (985, 425), (985, 485), 2)
        pygame.draw.line(screen, (0, 0, 0), (890, 425), (985, 425), 2)
        pygame.draw.line(screen, (0, 0, 0), (890, 485), (985, 485), 2)



        board.AddRound()
        CheckIfWin(turn, board)
        # Setting the inner matrix of the board according to where the stone has been set
        board.setmatrix(y, x)
        for line in board.mat:
          print('  '.join(map(str, line)))
        IndexToList(list1, x, y, board)

        # Running the algorithm what stones are captured
        result=[]
        for i in range(1, 20):
            for j in range(1, 20):
                if (board.mat[i][j] == 2):
                    checkifdeletnow_player(board,i,j)
        turn = 1
    cordinations = []
    if mode == "easyMode":
        cordinations = (random_number(list1,board))
    elif mode == "hardMode":
        cordinations=(hard_mode(list1,board))


    point_x=cordinations[0]
    point_y=cordinations[1]
    for i in range(1, 20):
        for j in range(1, 20):
            if (board.mat[i][j] == 1):
                checkifdeletnow_opponent(board, i, j)

    if (if_not_exist_in_list(list1, point_x, point_y)  and turn == 1):
        #side screen that shows score of each player
        pygame.draw.line(screen, (200,124,111), (890,120),(890,180), 2)
        pygame.draw.line(screen, (200, 124, 111), (985, 120), (985, 180), 2)
        pygame.draw.line(screen, (200, 124, 111), (890, 120), (985, 120), 2)
        pygame.draw.line(screen, (200, 124, 111), (890, 180), (985, 180), 2)

        pygame.draw.line(screen, (255, 255, 255), (890, 425), (890, 485), 2)
        pygame.draw.line(screen, (255, 255, 255), (985, 425), (985, 485), 2)
        pygame.draw.line(screen, (255, 255, 255), (890, 425), (985, 425), 2)
        pygame.draw.line(screen, (255, 255, 255), (890, 485), (985, 485), 2)
        pygame.time.wait(600)
        board.AddRound()
        CheckIfWin(turn, board)
        # Setting the inner matrix of the board according to where the stone has been set
        board.setmatrix(point_y,point_x)
        for line in board.mat:
          print('  '.join(map(str, line)))
        IndexToList(list1, point_x, point_y, board)

        # Running the algorithm what stones are captured
        for i in range(1, 20):
         for j in range(1, 20):
            if (board.mat[i][j] == 1):
                checkifdeletnow_opponent(board, i, j)
    print("------>>",)



def main(mode):
    global score_value
    board = Board()
    list1 = []
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and board.outline.collidepoint(event.pos):
                    drow_the_board(list1, event , board,mode)


# check who is the winner (bigger score)
def FinishGame(board):
    font = pygame.font.Font("./FreeSansBold11.ttf", 20)  # font type to text
    while True:
        pygame.display.set_caption('menu')
        screen.blit(background, (0, 0))
        pygame.time.wait(250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            mx, my = pygame.mouse.get_pos()
            button1 = pygame.Rect(320, 300, 200, 50)

            pygame.draw.rect(screen, (255, 250, 250), button1)

            # draw text into buttons
            player1 = font.render('player 1 win', True, (0, 0, 0))
            player2 = font.render('player 2 win', True, (0, 0, 0))
            draw = font.render('Draw', True, (0, 0, 0))
            if(board.winner()== 1):
                screen.blit(player1, (350 + 50, 300 + 20))
                pygame.display.update()
            if(board.winner()== 2):
                screen.blit(player2, (350 + 50, 300 + 20))
                pygame.display.update()
            if(board.winner()== 0):
                screen.blit(draw, (350 + 50, 300 + 20))
                pygame.display.update()
            # if press one of the buttons go to main (start game)
            if button1.collidepoint((mx, my)):

                if pygame.mouse.get_pressed()[0]:
                    main()

    # the menu
    # create a rectangular object for the
    # text surface object
def menu(): 

    # set the center of the rectangular object.
    font = pygame.font.Font("./FreeSansBold11.ttf", 20)  # font type to text
    # f = open("./FreeSansBold11.ttf", "r")
    # font = pygame.font.Font(f, 20)
    # f.close()
    text = font.render('Black', True, Color, black)
    score = font.render('Stones set: ', True, (0, 0, 0))
    text_Score = score.get_rect()
    text_Score.center = (900, 50 )
    text2 = font.render('White', True, white)
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect.center = (940, 150)
    textRect2.center = (940, 460)


    while True:
        global BOARD_SIZE
        pygame.display.set_caption('menu')
        screen.blit(background, (0, 0))
        screen.blit(background, (780, 0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


            mx, my = pygame.mouse.get_pos()
            button1 = pygame.Rect(350, 300, 150, 50)
            button2 = pygame.Rect(350, 400, 150, 50)
            pygame.draw.rect(screen, (255, 250, 250), button1)
            pygame.draw.rect(screen, (255, 250, 250), button2)

            #The_score
            pygame.draw.rect(screen, WHITE, (830, 420, 213, 300))
            pygame.draw.rect(screen, BLACK, (830, 100, 213, 300))
            screen.blit(text, textRect)
            screen.blit(score, text_Score)
            player_text = font.render(f"{player_score}", False, (255, 255, 255))
            screen.blit(player_text, (935, 250))
            screen.blit(text2, textRect2)
            opponent_text = font.render(f"{opponent_score}", False, (0, 0, 0))
            screen.blit(opponent_text, (935, 550))

            score_text_ = font.render(f"{score_}", False, (255, 255, 255))
            screen.blit(score_text_, (960, 40))

            # draw text into buttons
            easyMode = font.render('Easy', True, (0, 0, 0))
            hardMode = font.render('Hard', True, (0, 0, 0))
            screen.blit(easyMode, (350 + 50, 300 + 12))
            screen.blit(hardMode, (350 + 50, 400 + 12))

            pygame.display.update()

            # if press one of the buttons go to main (start game)
            # if button1.collidepoint((mx, my)) or button2.collidepoint((mx, my)):
            #     if pygame.mouse.get_pressed()[0]:
            #         main()
            if button1.collidepoint((mx, my)) and pygame.mouse.get_pressed()[0]:
                main("easyMode")
            if button2.collidepoint((mx, my)) and pygame.mouse.get_pressed()[0]:
                main("hardMode")    

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(BOARD_SIZE, 0, 32)
    background = pygame.image.load(BACKGROUND).convert()
    menu()
    
