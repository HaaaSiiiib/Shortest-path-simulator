import pygame
from colors import *

DEFAULT = WHITE

BARRIER_COLOR = BLACK

START_COLOR = CORAL

END_COLOR = BLUE

OPEN_COLOR = GREEN

CLOSED_COLOR = RED

PATH_COLOR = PURPLE

class Node:
	def __init__(self,row,col,width,total_rows):
		self.row = row
		self.col = col
		self.x = row*width
		self.y = col*width
		self.color = DEFAULT
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows
	
	def get_coord(self):
		return self.row,self.col

	def is_closed(self):
		return self.color == CLOSED_COLOR

	def is_open(self):
		return self.color == OPEN_COLOR

	def is_barrier(self):
		return self.color == BARRIER_COLOR

	def is_start(self):
		return self.color == START_COLOR

	def is_end(self):
		return self.color == END_COLOR

	def reset(self):
		self.color = DEFAULT

	def make_open(self):
		self.color = OPEN_COLOR

	def make_closed(self):
		self.color = CLOSED_COLOR

	def make_start(self):
		self.color = START_COLOR

	def make_end(self):
		self.color = END_COLOR

	def make_barrier(self):
		self.color = BARRIER_COLOR

	def make_path(self):
		self.color = PATH_COLOR

	def draw(self,window):
		pygame.draw.rect(window,self.color,(self.x,self.y,self.width,self.width))

	def update_neighbors(self,grid):
		self.neighbors = []

		#down
		if self.row < self.total_rows-1 and not grid[self.row+1][self.col].is_barrier():
			self.neighbors.append(grid[self.row+1][self.col])
		
		#up
		if self.row > 0 and not grid[self.row-1][self.col].is_barrier():
			self.neighbors.append(grid[self.row-1][self.col])
		
		#right
		if self.col < self.total_rows-1 and not grid[self.row][self.col+1].is_barrier():
			self.neighbors.append(grid[self.row][self.col+1])

		#left
		if self.col > 0 and not grid[self.row][self.col-1].is_barrier():
			self.neighbors.append(grid[self.row][self.col-1])



	def __lt__(self,other):
		return False
