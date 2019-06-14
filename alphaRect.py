import pygame
import math
import random

def redraw(attenuationFactor):
	#val = random.randrange(attenuationFactor,254)
	val = attenuationFactor
	return [val,val,val]

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
attenuationFactor = 100
cStart = redraw(attenuationFactor)
while not done:
	events = pygame.event.get()
	for e in events:
		if e.type == pygame.QUIT:
			done = True
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_SPACE:
				cStart = redraw(attenuationFactor)
			if e.key == pygame.K_ESCAPE:
				done = True
		if e.type == pygame.MOUSEBUTTONDOWN:
			#print("UP",e)
			if e.button == 4:
				attenuationFactor += 1
				if attenuationFactor > 255:
					attenuationFactor = 255
			else:
				attenuationFactor -= 1
				if attenuationFactor < 0:
					attenuationFactor = 0
			print("ATTEN:",attenuationFactor)
			cStart = redraw(attenuationFactor)
		if e.type == pygame.MOUSEMOTION:
			mX = e.pos[0]
			mY = e.pos[1]
		
	screen.fill((0,0,0))
	drawRectangle(screen, cStart, 100, 50, mX, mY)
	pygame.display.flip()

pygame.display.quit()
