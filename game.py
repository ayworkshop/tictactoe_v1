import pygame 
pygame.init()


#set up the screen 
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


#set frame rate 
clock = pygame.time.Clock()
FPS = 60 


#set game variables
ROWS, COLS = 3, 3 
SQUARE_SIZE = SCREEN_WIDTH // COLS 
BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
RED = (255, 127, 127) 

#load image of the marks 
CROSS_IMG = pygame.image.load("cross.png")
CROSS_IMG = pygame.transform.scale(CROSS_IMG, (SQUARE_SIZE, SQUARE_SIZE))
CIRCLE_IMG = pygame.image.load("circle.png")
CIRCLE_IMG = pygame.transform.scale(CIRCLE_IMG, (SQUARE_SIZE, SQUARE_SIZE))
COMPLETE_IMG = pygame.image.load("complete.png")
COMPLETE_IMG = pygame.transform.scale(COMPLETE_IMG, (SQUARE_SIZE, SQUARE_SIZE))

#load font
MAIN_FONT = pygame.font.SysFont("comicsans", 20) 


class Board:
    def __init__(self): 
        self.board = [] 
        self.create_board() 
        self.turn = "circle"
        self.step = 0        

    def create_board(self):
        for row in range (ROWS):
            self.board.append([])
            for col in range (COLS):
                self.board[row].append(0)

        #print(self.board)

    def draw_squares(self, win): 
        win.fill(BLUE)
        for row in range (ROWS):
            for col in range (row % 2, COLS, 2): 
                pygame.draw.rect(win, WHITE, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) 

    def draw(self, win):
        self.draw_squares(win)
        self.check_condition()
        for row in range (ROWS):
            for col in range (COLS):
                mark = self.board[row][col]
                if mark != 0: 
                    mark.draw(win) 

        self.message_text = MAIN_FONT.render(f"This is {self.turn} turn!", 1, RED) 
        win.blit(self.message_text, (10, 10))
        

    def place(self, row, col):
        if self.board[row][col] == 0: 
            if self.turn =="circle":
                self.board[row][col] = Mark(row, col, "circle")
            elif self.turn == "cross":
                self.board[row][col] = Mark(row, col, "cross")
            self.change_turn() 

    def change_turn(self):
        if self.turn == "circle":
            self.turn = "cross"
            self.step += 1 
        elif self.turn == "cross":
            self.turn = "circle"
            self.step += 1 

    def check_condition(self): 
        mark_1 = self.board[0][0]
        mark_2 = self.board[0][1]
        mark_3 = self.board[0][2]
        mark_4 = self.board[1][0]
        mark_5 = self.board[1][1]
        mark_6 = self.board[1][2]
        mark_7 = self.board[2][0]
        mark_8 = self.board[2][1]
        mark_9 = self.board[2][2]

        if mark_1 != 0 and mark_2 != 0 and mark_3 != 0 : 
            if mark_1.turn == mark_2.turn == mark_3.turn:
                self.board[mark_1.row][mark_1.col] = Mark(mark_1.row, mark_1.col, "complete")
                self.board[mark_2.row][mark_2.col] = Mark(mark_2.row, mark_2.col, "complete")
                self.board[mark_3.row][mark_3.col] = Mark(mark_3.row, mark_3.col, "complete")            
        if mark_1 != 0 and mark_5 != 0 and mark_9 != 0 : 
            if mark_1.turn == mark_5.turn == mark_9.turn:
                self.board[mark_1.row][mark_1.col] = Mark(mark_1.row, mark_1.col, "complete")
                self.board[mark_5.row][mark_5.col] = Mark(mark_5.row, mark_5.col, "complete")
                self.board[mark_9.row][mark_9.col] = Mark(mark_9.row, mark_9.col, "complete")
        if mark_1 != 0 and mark_4 != 0 and mark_7 != 0 : 
            if mark_1.turn == mark_4.turn == mark_7.turn:
                self.board[mark_1.row][mark_1.col] = Mark(mark_1.row, mark_1.col, "complete")
                self.board[mark_4.row][mark_4.col] = Mark(mark_4.row, mark_4.col, "complete")
                self.board[mark_7.row][mark_7.col] = Mark(mark_7.row, mark_7.col, "complete")
        if mark_4 != 0 and mark_5 != 0 and mark_6 != 0 : 
            if mark_4.turn == mark_5.turn == mark_6.turn:
                self.board[mark_4.row][mark_4.col] = Mark(mark_4.row, mark_4.col, "complete")
                self.board[mark_5.row][mark_5.col] = Mark(mark_5.row, mark_5.col, "complete")
                self.board[mark_6.row][mark_6.col] = Mark(mark_6.row, mark_6.col, "complete")
        if mark_2 != 0 and mark_5 != 0 and mark_8 != 0 : 
            if mark_2.turn == mark_5.turn == mark_8.turn:
                self.board[mark_2.row][mark_2.col] = Mark(mark_2.row, mark_2.col, "complete")
                self.board[mark_5.row][mark_5.col] = Mark(mark_5.row, mark_5.col, "complete")
                self.board[mark_8.row][mark_8.col] = Mark(mark_8.row, mark_8.col, "complete")
        if mark_3 != 0 and mark_5 != 0 and mark_7 != 0 : 
            if mark_3.turn == mark_5.turn == mark_7.turn:
                self.board[mark_3.row][mark_3.col] = Mark(mark_3.row, mark_3.col, "complete")
                self.board[mark_5.row][mark_5.col] = Mark(mark_5.row, mark_5.col, "complete")
                self.board[mark_7.row][mark_7.col] = Mark(mark_7.row, mark_7.col, "complete")
        if mark_7 != 0 and mark_8 != 0 and mark_9 != 0 : 
            if mark_7.turn == mark_8.turn == mark_9.turn:
                self.board[mark_7.row][mark_7.col] = Mark(mark_7.row, mark_7.col, "complete")
                self.board[mark_8.row][mark_8.col] = Mark(mark_8.row, mark_8.col, "complete")
                self.board[mark_9.row][mark_9.col] = Mark(mark_9.row, mark_9.col, "complete")
        if mark_3 != 0 and mark_6 != 0 and mark_9 != 0 : 
            if mark_3.turn == mark_6.turn == mark_9.turn:
                self.board[mark_3.row][mark_3.col] = Mark(mark_3.row, mark_3.col, "complete")
                self.board[mark_6.row][mark_6.col] = Mark(mark_6.row, mark_6.col, "complete")
                self.board[mark_9.row][mark_9.col] = Mark(mark_9.row, mark_9.col, "complete")
                


    def check_reset(self):
        for row in range (ROWS):
            for col in range (COLS):
                mark = self.board[row][col]
                if mark != 0 and mark.turn == "complete": 
                    pygame.time.delay(2000)
                    self.board = [] 
                    self.create_board() 
                    self.turn = "circle"
                    self.step = 0 

        if self.step == 9: 
            pygame.time.delay(2000)
            self.board = [] 
            self.create_board() 
            self.turn = "circle" 
            self.step = 0           



class Mark: 
    def __init__(self, row, col, turn): 
        self.row = row
        self.col = col 
        self.turn = turn 
        self.x = 0
        self.y = 0 
        self.calc_pos() 
        if self.turn == "circle": 
            self.img = CIRCLE_IMG
        elif self.turn == "cross":
            self.img = CROSS_IMG 
        elif self.turn == "complete":
            self.img = COMPLETE_IMG 

    def calc_pos(self):
        self.x = self.col*SQUARE_SIZE
        self.y = self.row*SQUARE_SIZE

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))



#game loop 
run = True 
gameboard = Board()
#gameboard.board[0][0] = Mark(0, 0, "circle")

while run: 

    clock.tick(FPS) 

    gameboard.draw(screen)
    pygame.display.update() 
    gameboard.check_reset()

    for event in pygame.event.get(): 

        if event.type == pygame.QUIT: 
            run = False 

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x, y = pos 
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE
            gameboard.place (row, col) 



pygame.quit() 




#Copyright © 2025 by futuristickids (Instagram), Futuristic Kids(Facebook), ay.parentingworkshop@yahoo.com
#All rights reserved
