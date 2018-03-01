import pygame
import time

pygame.init()

display_width = 1000
display_height = 600


text = 'Task Complete'
black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height)) 
pygame.display.set_caption('Take a leep of faith')
clock = pygame.time.Clock()

box1 = pygame.image.load('images/box.png')
box2 = pygame.image.load('images/box.png')
box3 = pygame.image.load('images/box.png')
rball1 = pygame.image.load('images/rball.png')
bball1 = pygame.image.load('images/bball.png')
rball2 = pygame.image.load('images/rball.png')
bball2 = pygame.image.load('images/bball.png')
rball3 = pygame.image.load('images/rball.png')
bball3 = pygame.image.load('images/bball.png')
rlight = pygame.image.load('images/rlight.png')
ylight = pygame.image.load('images/ylight.png')
glight = pygame.image.load('images/glight.png')
bbr1 = pygame.image.load('images/rball.png')
bbr2 = pygame.image.load('images/rball.png')
bbr3 = pygame.image.load('images/rball.png')
bbb1 = pygame.image.load('images/bball.png')
bbb2 = pygame.image.load('images/bball.png')
bbb3 = pygame.image.load('images/bball.png')

box1 = pygame.transform.scale(box1, (200, 200))
box2 = pygame.transform.scale(box2, (200, 200))
box3 = pygame.transform.scale(box3, (200, 200))
ylight = pygame.transform.scale(ylight, (140, 140))
rlight = pygame.transform.scale(rlight, (140, 140))
glight = pygame.transform.scale(glight, (140, 140))
rball1 = pygame.transform.scale(rball1, (100, 100))
rball2 = pygame.transform.scale(rball2, (100, 100))
rball3 = pygame.transform.scale(rball3, (100, 100))
bball1 = pygame.transform.scale(bball1, (100, 100))
bball2 = pygame.transform.scale(bball2, (100, 100))
bball3 = pygame.transform.scale(bball3, (100, 100))
bbr1 = pygame.transform.scale(bbr1, (100, 100))
bbr2 = pygame.transform.scale(bbr2, (100, 100))
bbr3 = pygame.transform.scale(bbr3, (100, 100))
bbb1 = pygame.transform.scale(bbb1, (100, 100))
bbb2 = pygame.transform.scale(bbb2, (100, 100))
bbb3 = pygame.transform.scale(bbb3, (100, 100))

#reset function game loop can be used instead of restart and initialisation can be done inn the begening
#sleep for 5 sec
xb = (display_width * 0.1)
yb = (display_height * 0.6)
xl = xb+700
yl = yb-330
xr1 = (display_width * 0.05)
xr2 = xr1 + 100
xr3 = xr2 + 100
yr1 = (display_height * 0.1)
yr2 = yr1
yr3 = yr1
xb1 = xr1
xb2 = xr2
xb3 = xr3
yb1 = yr1 +100
yb2 = yb1
yb3 = yb1

b1=0
b2=0
b3=0
sball = 0
feedback = 0
steps = 0
aball = rball1
gameDisplay.blit(ylight,(xl,yl))

#def text_objects(text,font):
#	textSurface = font.render(text,True,white)
#	return textSurface, textSurface.get_rect()
	
	

def task_complete(b1,b2,b3): 
	if (b1,b2,b3) == (1,2,1):
		feedback = 1
	else:
		feedback = 2
		
#	largeText = pygame.font.Font('freesansbold.ttf',115)
#	TextSurf, TectRect = text_objects(text,largeText)
#	TextRect.centre = (display_width/2 , display_height/2)
#	gameDisplay.blit(TextSurface,TextRect)
#	time.sleep(5)
#	game_loop()
	

def box(feedback,b1,b2,b3):
	gameDisplay.blit(box1,(xb,yb))
	gameDisplay.blit(box1,(xb+300,yb))
	gameDisplay.blit(box1,(xb+600,yb))
	
	if feedback == 2: 
		gameDisplay.blit(rlight,(xl,yl))
	elif feedback == 1:
		gameDisplay.blit(glight,(xl,yl))
	else:
		gameDisplay.blit(ylight,(xl,yl))
	print (b1,b2,b3)

	if b1 == 1:
		gameDisplay.blit(bbr1,(xb+50,yb))
	elif b1 == 2:
		gameDisplay.blit(bbb1,(xb+50,yb))
	if b2 == 1:
		gameDisplay.blit(bbr2,(xb+350,yb))
	elif b2 == 2:
		gameDisplay.blit(bbb2,(xb+350,yb))
	if b3 == 1:	
		gameDisplay.blit(bbr3,(xb+650,yb))
	elif b3 ==2:
		gameDisplay.blit(bbb3,(xb+650,yb))

def balls(r,b):
	xr1 = (display_width * 0.05)
	xr2 = xr1 + 100
	xr3 = xr2 + 100
	yr1 = (display_height * 0.1)
	yr2 = yr1
	yr3 = yr1
	xb1 = xr1
	xb2 = xr2
	xb3 = xr3
	yb1 = yr1 +100
	yb2 = yb1
	yb3 = yb1

	if(r <> 3):
		gameDisplay.blit(rball1,(xr1,yr1))
		if(r <> 2):
			gameDisplay.blit(rball2,(xr2,yr2))
			if(r <> 1):
				gameDisplay.blit(rball3,(xr3,yr3))
	
	if(b <> 3):
		gameDisplay.blit(bball1,(xb1,yb1))
		if(b <> 2):
			gameDisplay.blit(bball1,(xb2,yb2))
			if(b <> 1):
				gameDisplay.blit(bball1,(xb3,yb3))
	

def game_loop():
	gameExit = False
	feedback = 0
	r=0
	b=0
	b1=0
	b2=0
	b3=0
	sball = 0
	steps = 0

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					aball = rball1
					sball = 1
				elif event.key == pygame.K_a:
					aball = bball1
					sball = 2
				elif event.key==pygame.K_1:
					steps+=1
					if sball == 1:
						if b1 == 1:
							r-=1
						elif b1 == 2:
							b-=1
						b1 = 1
						feedback = 1
						sball = 0
						rball2 = rball1
						rball3 = rball2
						r+=1
					else: 
						if b1 == 1:
							r-=1
						elif b1 == 2:
							b-=1
						feedback = 2
						b1 = 2	
						sball = 0
						bball2 = bball1
						bball3 = bball2
						b+=1

				elif event.key==pygame.K_2:
					steps+=1
					if sball == 2:
						if b2 == 1:
							r-=1
						elif b2 == 2:
							b-=1
						b2 = 2
						feedback = 1
						sball = 0
						bball2 = bball1
						bball3 = bball2
						b+=1
					else: 
						if b2 == 1:
							r-=1
						elif b2 == 2:
							b-=1
						feedback = 2
						b2 = 1	 
						sball = 0
						rball2 = rball1
						rball3 = rball2
						r+=1

				elif event.key==pygame.K_3:
					steps+=1
					if sball == 1:
						if b3 == 1:
							r-=1
						elif b3 == 2:
							b-=1
						b3 = 1
						feedback = 1
						sball = 0
						rball2 = rball1
						rball3 = rball2
						r+=1
					else: 
						if b3 == 1:
							r-=1
						elif b3 == 2:
							b-=1
						feedback = 2
						b3 = 2	
						sball = 0
						bball2 = bball1
						bball3 = bball2				
						b+=1
				

		gameDisplay.fill(black)
		box(feedback,b1,b2,b3)
		balls(r,b)
		print(feedback)
		task_complete(b1,b2,b3)
		pygame.display.update()
		clock.tick(60)



game_loop()
pygame.quit()
quit()



