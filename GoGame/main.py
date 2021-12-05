import pygame
import Board
import sys



BACKGROUND = 'images/ramin.jpg'
BOARD_SIZE = (820, 820)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Stone(Board.Stone):
    def __init__(self, board, point, color):
        """Create, initialize and draw a stone."""
        super(Stone, self).__init__(board, point, color)
        self.coords = (5 + self.point[0] * 40, 5 + self.point[1] * 40)
        self.draw()

    def draw(self):
        """Draw the stone as a circle."""
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

def main():
    board = Board()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and board.outline.collidepoint(event.pos):
                    x = int(round(((event.pos[0] - 5) / 40.0), 0))
                    y = int(round(((event.pos[1] - 5) / 40.0), 0))
                    stone = board.search(point=(x, y))
                    print(x,y)
                    if stone:
                        stone.remove()
                    else:
                        added_stone = Stone(board, (x, y), board.turn())
                   # board.update_liberties(added_stone)
def menu():  #  the menu
    font = pygame.font.Font("freesansbold.ttf", 20) #font type to text
    while True:
        pygame.display.set_caption('menu')
        screen.blit(background, (0, 0))
        pygame.time.wait(250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            mx, my = pygame.mouse.get_pos()
            button1 = pygame.Rect(350,300,150,50)
            button2 = pygame.Rect(350,400,150,50)

            pygame.draw.rect(screen ,(255,250,250),button1)
            pygame.draw.rect(screen, (255, 0, 0, 0), button2)

            # draw text into buttons
            easy = font.render('Easy', True, (0,0,0))
            hard = font.render('Hard', True, (0, 0, 0))

            screen.blit(easy, (350+50 , 300+12))
            screen.blit(hard, (350 + 50, 400 + 12))

            pygame.display.update()

            # if press one of the buttons go to main (start game)
            if button1.collidepoint((mx,my)) or button2.collidepoint((mx,my)):
                if pygame.mouse.get_pressed()[0]:
                    main()




if __name__ == '__main__':
  pygame.init()
  screen = pygame.display.set_mode(BOARD_SIZE, 0, 32)
  background = pygame.image.load(BACKGROUND).convert()



  menu()
  #main()
