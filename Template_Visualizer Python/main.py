import pygame
import math
from queue import PriorityQueue
from colors import *
from Node import Node

DIMENSION = 800 

WINDOW = pygame.display.set_mode((DIMENSION,DIMENSION))
pygame.display.set_caption("A* Path Finding Visualization")

DEFAULT = WHITE

def h(p1,p2):
	x1,y1 = p1
	x2,y2 = p2
	return abs(x2-x1)+abs(y2-y1)

def make_grid(rows,width):
	grid = []
	gap = width//rows

	for i in range(rows):
		grid.append(list())
		for j in range(rows):
			node = Node(i,j,gap,rows)
			grid[i].append(node)

	return grid

def draw_grid(window,rows,width):
	gap = width//rows
	for i in  range(rows):
		pygame.draw.line(window,GREY,(0,i*gap),(width,i*gap))
		for j in  range(rows):
			pygame.draw.line(window,GREY,(j*gap,0),(j*gap,width))

def draw(window,grid,rows,width):
	window.fill(DEFAULT)

	for row in grid:
		for node in row:
			node.draw(window)

	draw_grid(window,rows,width)
	pygame.display.update()

def generate_path(parent,start,current,draw):
	if current == start:
		return
	current = parent[current]
	if current != start:
		current.make_path()
	draw()
	generate_path(parent,start,current,draw)

def algorithm(draw,grid,start,end):
	pass
def get_click_pos(pos,rows,width):
	gap = width//rows
	y,x = pos

	row = y//gap
	col = x//gap

	return row,col

def main(window,width):
	ROWS = 50
	grid = make_grid(ROWS,width)

	start,end = None,None

	run = True
	started = False

	while run:
		draw(window,grid,ROWS,width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if started:
				continue

			#left click
			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				row,col = get_click_pos(pos,ROWS,width)
				node = grid[row][col]
				if not start:
					start = node
					start.make_start()
				
				elif not end and node != start:
					end = node
					end.make_end()
				
				elif node != end and node != start:
					node.make_barrier()

			#mouse wheel click
			elif pygame.key.get_pressed()[114] or pygame.mouse.get_pressed()[1]:
				for row in grid:
					for node in row:
						node.reset()
				start = None
				end = None

			#right click
			elif pygame.mouse.get_pressed()[2]:
				pos = pygame.mouse.get_pos()
				row,col = get_click_pos(pos,ROWS,width)
				node = grid[row][col]
				if node.is_start():
					node.reset()
					start = None
				
				elif node.is_end():
					node.reset()
					end = None
				
				elif node.is_barrier():
					node.reset()
			if pygame.key.get_pressed()[32] and not started:
				for row in grid:
					for node in row:
						node.update_neighbors(grid)
				algorithm(lambda:draw(window,grid,ROWS,width),grid,start,end)


	pygame.quit()

main(WINDOW,DIMENSION)
