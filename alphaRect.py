import pygame
import math
import random

def drawRectangle(screen, cStart, wid, heig, mX, mY):
	xOffset = 200 - int(wid/2)
	yOffset = 150 - int(heig/2)

	for i in range(xOffset, wid+xOffset):
		for j in range(yOffset, heig+yOffset):
			aSq = abs(i - mX) ** 2
			bSq = abs(j - mY) ** 2
			cSq = math.sqrt(aSq + bSq)
			#print("CSQUARED:", cSq)
			
			r = cStart[0] - (cSq)
			g = cStart[1] - (cSq)
			b = cStart[2] - (cSq)
			
			if r < 0:
				r = 0
			if g < 0:
				g = 0
			if b < 0:
				b = 0
			screen.set_at((i,j), (int(r), int(g), int(b)))

pygame.display.init()

screen = pygame.display.set_mode((400,300))

done = False
mX = 0
mY = 0
cStart = [random.randrange(1,254),random.randrange(1,254),random.randrange(1,254)]
while not done:
	events = pygame.event.get()
	for e in events:
		if e.type == pygame.QUIT:
			done = True
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_SPACE:
				del cStart[:]
				cStart = [random.randrange(1,254),random.randrange(1,254),random.randrange(1,254)]
			if e.key == pygame.K_ESCAPE:
				done = True
		if e.type == pygame.MOUSEMOTION:
			#print(e.pos)
			mX = e.pos[0]
			mY = e.pos[1]
		
	screen.fill((0,0,0))
	drawRectangle(screen, cStart, 100, 50, mX, mY)
	pygame.display.flip()

pygame.display.quit()
