import pygame
import random
import numpy as np
pygame.init()


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0,0,255)
x1_change = 0       
y1_change = 0

clock = pygame.time.Clock()
snakelst = []


class game:
    def __init__(self):
        dis_width = 300
        dis_height = 200
        dis=pygame.display.set_mode((dis_width,dis_height))
        pygame.display.update()
        pygame.display.set_caption('Snake game')
        self.board = dis
        snakelst = []
        self.snakelst = snakelst
        x = random.randint(0,dis_width / 10 - 1) * 10
        y = random.randint(0,dis_height / 10 - 1) * 10
        self.addsnake((x,y), blue)
        self.game_over = False
        self.cp = (0,0)
        self.play()
    def moveright(self):
        print('right')

    def addsnake(self,p, color):
        s = snake(p, color)
        self.snakelst.append(s)

    def createfood(self):
        x1f = random.randint(0,self.board.get_width() / 10 - 1) * 10
        y1f = random.randint(0,self.board.get_height() / 10 - 1) * 10
        food = (x1f,y1f)
        while self.board.get_at(food) != white:
            x1f = random.randint(0,self.board.get_width() / 10 - 1) * 10
            y1f = random.randint(0,self.board.get_height() / 10 - 1) * 10
            food = (x1f,y1f)
        return food

    def drawsnake(self):
        for i in self.snakelst:
            pygame.draw.rect(self.board, i.color, [i.p[0],i.p[1], 10, 10])

    def movesnake(self, x1, y1, pchange,isfood, food):
        x1 += pchange[0]
        y1 += pchange[1]
        p = (x1, y1)
        self.board.fill(white)
        if food == None:
            food = self.createfood()
            isfood = True
        pygame.draw.rect(self.board, red, [food[0],food[1], 10, 10])
        if p == food:
            food = None
            plast = self.snakelst[-1].p
            for i in range(len(self.snakelst)):
                if i == 0:
                    plast = self.snakelst[i].p
                    self.snakelst[i].p = p
                else:
                    currentp = self.snakelst[i].p
                    self.snakelst[i].p = plast
                    plast = currentp
            self.addsnake(plast, black)
        else:
            for i in range(len(self.snakelst)):
                if i == 0:
                    plast = self.snakelst[i].p
                    self.snakelst[i].p = p
                else:
                    currentp = self.snakelst[i].p
                    self.snakelst[i].p = plast
                    plast = currentp

        return x1, y1,isfood,food


    def play(self):
        game_over=self.game_over
        isfood = False
        food = None
        cp = (0,0)
        x1_change = 0
        y1_change = 0
        x1 = random.randint(0,self.board.get_width() / 10 - 1) * 10
        y1 = random.randint(0,self.board.get_height() / 10 - 1) * 10
        snakelst = self.snakelst
        
            
        played = False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('LEFT')
                    if cp[0] == 0:
                        x1_change = -10
                        y1_change = 0
                        cp = (x1_change,y1_change)
                        x1, y1, isfood,food = self.movesnake(x1,y1,cp,isfood,food)
                        self.drawsnake(self.snakelst)
                        played = True
                        for i in range(1,len(self.snakelst)):
                            if self.snakelst[0].p == self.snakelst[i].p:
                                self.game_over = True
                        if x1 >= self.board.get_width() or x1 < 0 or y1 >= self.board.get_height() or y1 < 0:
                            self.game_over = True
                elif event.key == pygame.K_RIGHT:
                    print('RIGHT')
                    if x1_change == 0:
                        x1_change = 10
                        y1_change = 0
                        cp = (x1_change,y1_change)
                        x1, y1, isfood,food, self.snakelst = self.movesnake(x1,y1,snakelst,cp,isfood,food)
                        self.drawsnake(self.snakelst)
                        played = True
                        for i in range(1,len(self.snakelst)):
                            if self.snakelst[0].p == self.snakelst[i].p:
                                self.game_over = True
                        if x1 >= self.board.get_width() or x1 < 0 or y1 >= self.board.get_height() or y1 < 0:
                            self.game_over = True
                elif event.key == pygame.K_UP:
                    print('UP')
                    if y1_change == 0:
                        y1_change = -10
                        x1_change = 0
                        cp = (x1_change,y1_change)
                        x1, y1, isfood,food, snakelst = self.movesnake(x1,y1,snakelst,cp,isfood,food)
                        self.drawsnake(self.snakelst)
                        played = True
                        for i in range(1,len(self.snakelst)):
                            if self.snakelst[0].p == self.snakelst[i].p:
                                self.game_over = True
                        if x1 >= self.board.get_width() or x1 < 0 or y1 >= self.board.get_height() or y1 < 0:
                            self.game_over = True
                elif event.key == pygame.K_DOWN:
                    print('DOWN')
                    if y1_change == 0:
                        y1_change = 10
                        x1_change = 0
                        cp = (x1_change,y1_change)
                        x1, y1, isfood,food, snakelst = self.movesnake(x1,y1,snakelst,cp,isfood,food)
                        self.drawsnake(self.snakelst)
                        played = True
                        for i in range(1,len(self.snakelst)):
                            if self.snakelst[0].p == self.snakelst[i].p:
                                self.game_over = True
                        if x1 >= self.board.get_width() or x1 < 0 or y1 >= self.board.get_height() or y1 < 0:
                            self.game_over = True
                            
        if not played:
            x1, y1, isfood,food,snakelst = self.movesnake(x1,y1,snakelst,cp,isfood,food)
        

        self.drawsnake(snakelst)
        for i in range(1,len(snakelst)):
            if snakelst[0].p == snakelst[i].p:
                self.game_over = True
        if x1 >= self.board.get_width() or x1 < 0 or y1 >= self.board.get_height() or y1 < 0:
            self.game_over = True

        pygame.display.update()
        board = pygame.surfarray.pixels3d(self.board)
        clock.tick(15)
        print(board[0])
        score = len(snakelst) - 1
        return score
        


class snake:
    def __init__(self, p, color):
        self.p = p
        self.color = color

a = game()
pygame.quit()

quit()
