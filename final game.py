# IMPORT LIBRARIES
import pygame
import math
import random
import sys

def main():

	# DEFINE VARIABLES
	BLACK = [0, 0, 0]
	WHITE = [255, 255, 255]
	RED = [255, 0, 0]
	GREEN = [0, 255, 0]
	BLUE = [0, 0, 255]

	size = [700,500]
	running = True

	x = 0
	y = 0
	x_speed = 0
	y_speed = 0

	# DEFINE FUNCTIONS
	def object(screen, x, y, color):
		pygame.draw.circle(screen, color, [x,y], 10, 0)
		pygame.draw.circle(screen, color, [x,y], 5, 0)

	# SETUP PYGAME
	pygame.init()
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("the soccer game")
	clock = pygame.time.Clock()
	pygame.mouse.set_visible(False)

	# MAIN PROGRAM LOOP
	while running:

		# Event loop to check for user input
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_speed = -10
				elif event.key == pygame.K_RIGHT:
					x_speed = 10
				if event.key == pygame.K_UP:
					y_speed = -10
				elif event.key == pygame.K_DOWN:
					y_speed = 10

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_speed = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_speed = 0

		# Update variables
		x += x_speed
		y += y_speed

		pos = pygame.mouse.get_pos()
		x_cursor = pos[0]
		y_cursor = pos[1]

		# Draw background (wipe the screen)
		screen.fill(WHITE)

		# Draw objects
		object(screen, x, y, RED)
		object(screen, x_cursor, y_cursor, BLACK)

		# Display drawings
		pygame.display.flip()

		# Set frame rate to 60 frames per second
		clock.tick(60)

	# Close the window and quit.
	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	main()
