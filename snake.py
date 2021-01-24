import pygame
import random
import numpy as np
from PIL import Image
import tensorflow as tf

pygame.init()


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0,0,255)
x1_change = 0       
y1_change = 0

clock = pygame.time.Clock()


class game:
	def __init__(self, w=300,h=200):
		self.dis_width = w
		self.dis_height = h
		dis=pygame.display.set_mode((self.dis_width,self.dis_height))
		pygame.display.update()
		pygame.display.set_caption('Snake game')
		self.board = dis
		self.isfood = False
		self.food = None
		self.cp = (0,0)
		self.x1_change = 0
		self.y1_change = 0
		self.counter = 0
		self.x1 = random.randint(0,self.board.get_width() / 10 - 1) * 10
		self.y1 = random.randint(0,self.board.get_height() / 10 - 1) * 10
		
		self.model = set_model(w, h)

		self.played = False
		self.snakelst = []
		x_srart = random.randint(0,self.dis_width / 10 - 1) * 10
		y_start = random.randint(0,self.dis_height / 10 - 1) * 10
		
		self.addsnake((x_srart,y_start), blue)
		self.game_over = False
		self.cp = (0,0)
		while not self.game_over:
			self.play() 
		print(self.counter)

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

	def movesnake(self):
		self.x1 += self.cp[0]
		self.y1 += self.cp[1]
		p = (self.x1, self.y1)
		self.board.fill(white)
		if self.food == None:
			self.food = self.createfood()
			self.isfood = True
		pygame.draw.rect(self.board, red, [self.food[0],self.food[1], 10, 10])
		if p == self.food:
			self.food = None
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
			self.counter += 1
		else:
			for i in range(len(self.snakelst)):
				if i == 0:
					plast = self.snakelst[i].p
					self.snakelst[i].p = p
				else:
					currentp = self.snakelst[i].p
					self.snakelst[i].p = plast
					plast = currentp



	def play(self):
		self.played = False
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				self.game_over=True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					print('LEFT')
					if self.cp[0] == 0:
						self.x1_change = -10
						self.y1_change = 0
						self.cp = (self.x1_change,self.y1_change)
				elif event.key == pygame.K_RIGHT:
					print('RIGHT')
					if self.cp[0] == 0:
						self.x1_change = 10
						self.y1_change = 0
						self.cp = (self.x1_change,self.y1_change)
						self.movesnake()
						self.drawsnake()
				elif event.key == pygame.K_UP:
					print('UP')
					if self.cp[1] == 0:
						self.x1_change = 0
						self.y1_change = -10
						self.cp = (self.x1_change,self.y1_change)
						self.movesnake()
						self.drawsnake()
				elif event.key == pygame.K_DOWN:
					print('DOWN')
					if self.cp[1] == 0:
						self.x1_change = 0
						self.y1_change = 10
						self.cp = (self.x1_change,self.y1_change)
						self.movesnake()
						self.drawsnake()
				#? captures gamestate as w * h imagwe after every turn
				pygame.image.save(self.board, 'cp.png')
				ia = Image.open('cp.png')
				ia = pass_to_model(ia)
				print(ia.shape)
				print(self.model(ia))

				self.played = True
				for i in range(1,len(self.snakelst)):
					if self.snakelst[0].p == self.snakelst[i].p:
						self.game_over = True
				if self.x1 >= self.board.get_width() or self.x1 < 0 or self.y1 >= self.board.get_height() or self.y1 < 0:
					self.game_over = True

		if not self.played:
			self.movesnake()
		

		self.drawsnake()
		for i in range(1,len(self.snakelst)):
			if self.snakelst[0].p == self.snakelst[i].p:
				self.game_over = True
		if self.x1 >= self.board.get_width() or self.x1 < 0 or self.y1 >= self.board.get_height() or self.y1 < 0:
			self.game_over = True

		pygame.display.update()
		board = pygame.surfarray.pixels3d(self.board)
		clock.tick(15)
		


class snake:
	def __init__(self, p, color, model=None):
		self.p = p
		self.color = color
		self.model = model

def pass_to_model(img):
	img_arr = np.asarray(img)
	img_arr = np.expand_dims(img_arr, axis=0)

	return img_arr

def set_model(w, h):
	model = tf.keras.models.Sequential([
		tf.keras.layers.Conv2D(1, (3,3), activation='relu', input_shape=(200, 300, 3)),
		tf.keras.layers.MaxPooling2D(2,2),
		tf.keras.layers.Conv2D(1, (3,3), activation='relu'),
		tf.keras.layers.MaxPooling2D(2,2),
		tf.keras.layers.Conv2D(1, (3,3), activation='relu'),
		tf.keras.layers.MaxPooling2D(2,2),
		tf.keras.layers.Flatten(),
		tf.keras.layers.Dense(128, activation='relu'),
		tf.keras.layers.Dropout(0.2),
		tf.keras.layers.Dense(4)
		])
	
	model.compile(optimizer='adam',
			metrics=['accuracy'])
	probability_model = tf.keras.Sequential([
		model,
		tf.keras.layers.Softmax()
		])
	return probability_model

a = game()
pygame.quit()

quit()
