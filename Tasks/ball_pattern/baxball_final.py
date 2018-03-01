import pygame
import time

pygame.init()

display_width = 1300
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
box4 = pygame.image.load('images/box.png')
box5 = pygame.image.load('images/box.png')
rball1 = pygame.image.load('images/rball.png')
bball1 = pygame.image.load('images/bball.png')
rball2 = pygame.image.load('images/rball.png')
bball2 = pygame.image.load('images/bball.png')
rball3 = pygame.image.load('images/rball.png')
bball3 = pygame.image.load('images/bball.png')
rball4 = pygame.image.load('images/rball.png')
bball4 = pygame.image.load('images/bball.png')
rball5 = pygame.image.load('images/rball.png')
bball5 = pygame.image.load('images/bball.png')
rlight = pygame.image.load('images/rlight.png')
ylight = pygame.image.load('images/ylight.png')
glight = pygame.image.load('images/glight.png')
bbr1 = pygame.image.load('images/rball.png')
bbr2 = pygame.image.load('images/rball.png')
bbr3 = pygame.image.load('images/rball.png')
bbr4 = pygame.image.load('images/rball.png')
bbr5 = pygame.image.load('images/rball.png')
bbb1 = pygame.image.load('images/bball.png')
bbb2 = pygame.image.load('images/bball.png')
bbb3 = pygame.image.load('images/bball.png')
bbb4 = pygame.image.load('images/bball.png')
bbb5 = pygame.image.load('images/bball.png')

box1 = pygame.transform.scale(box1, (200, 200))
box2 = pygame.transform.scale(box2, (200, 200))
box3 = pygame.transform.scale(box3, (200, 200))
box4 = pygame.transform.scale(box4, (200, 200))
box5 = pygame.transform.scale(box5, (200, 200))
ylight = pygame.transform.scale(ylight, (140, 140))
rlight = pygame.transform.scale(rlight, (140, 140))
glight = pygame.transform.scale(glight, (140, 140))
rball1 = pygame.transform.scale(rball1, (100, 100))
rball2 = pygame.transform.scale(rball2, (100, 100))
rball3 = pygame.transform.scale(rball3, (100, 100))
rball4 = pygame.transform.scale(rball4, (100, 100))
rball5 = pygame.transform.scale(rball5, (100, 100))
bball1 = pygame.transform.scale(bball1, (100, 100))
bball2 = pygame.transform.scale(bball2, (100, 100))
bball3 = pygame.transform.scale(bball3, (100, 100))
bball4 = pygame.transform.scale(bball4, (100, 100))
bball5 = pygame.transform.scale(bball5, (100, 100))
bbr1 = pygame.transform.scale(bbr1, (100, 100))
bbr2 = pygame.transform.scale(bbr2, (100, 100))
bbr3 = pygame.transform.scale(bbr3, (100, 100))
bbr4 = pygame.transform.scale(bbr4, (100, 100))
bbr5 = pygame.transform.scale(bbr5, (100, 100))
bbb1 = pygame.transform.scale(bbb1, (100, 100))
bbb2 = pygame.transform.scale(bbb2, (100, 100))
bbb3 = pygame.transform.scale(bbb3, (100, 100))
bbb4 = pygame.transform.scale(bbb4, (100, 100))
bbb5 = pygame.transform.scale(bbb5, (100, 100))

#reset function game loop can be used instead of restart and initialisation can be done inn the begening
#sleep for 5 sec
xb = (display_width * 0.05)+50
yb = (display_height * 0.6)+50
xl = xb+1000
yl = yb-330
xr1 = (display_width * 0.05)
xr2 = xr1 + 100
xr3 = xr2 + 100
xr4 = xr3 + 100
xr5 = xr4 + 100

yr1 = (display_height * 0.1)
yr2 = yr1
yr3 = yr1
yr4 = yr1
yr5 = yr1

xb1 = xr1
xb2 = xr2
xb3 = xr3
xb4 = xr4
xb5 = xr5

yb1 = yr1 +100
yb2 = yb1
yb3 = yb1
yb4 = yb1
yb5 = yb1


aball = rball1
gameDisplay.blit(ylight,(xl,yl))

#def text_objects(text,font):
#	textSurface = font.render(text,True,white)
#	return textSurface, textSurface.get_rect()
	
	

def task_complete(b1,b2,b3,b4,b5,m): 
	if (b1,b2,b3,b4,b5,m) == (1,2,1,2,1,1):
		feedback = 1
	elif (b1,b2,b3,b4,b5,m) == (2,1,2,1,2,2):
		feedback = 1
	else:
		feedback = 2
		
#	largeText = pygame.font.Font('freesansbold.ttf',115)
#	TextSurf, TectRect = text_objects(text,largeText)
#	TextRect.centre = (display_width/2 , display_height/2)
#	gameDisplay.blit(TextSurface,TextRect)
#	time.sleep(5)
#	game_loop()
	

def box(feedback,b1,b2,b3,b4,b5):
	gameDisplay.blit(box1,(xb,yb))
	gameDisplay.blit(box1,(xb+200,yb))
	gameDisplay.blit(box1,(xb+400,yb))
	gameDisplay.blit(box1,(xb+600,yb))
	gameDisplay.blit(box1,(xb+800,yb))
	
	if feedback == 2: 
		gameDisplay.blit(rlight,(xl,yl))
	elif feedback == 1:
		gameDisplay.blit(glight,(xl,yl))
	else:
		gameDisplay.blit(ylight,(xl,yl))

	if b1 == 1:
		gameDisplay.blit(bbr1,(xb+50,yb))
	elif b1 == 2:
		gameDisplay.blit(bbb1,(xb+50,yb))
	if b2 == 1:
		gameDisplay.blit(bbr2,(xb+250,yb))
	elif b2 == 2:
		gameDisplay.blit(bbb2,(xb+250,yb))
	if b3 == 1:	
		gameDisplay.blit(bbr3,(xb+450,yb))
	elif b3 ==2:
		gameDisplay.blit(bbb3,(xb+450,yb))
	if b4 == 1:	
		gameDisplay.blit(bbr4,(xb+650,yb))
	elif b4 ==2:
		gameDisplay.blit(bbb4,(xb+650,yb))
	if b5 == 1:	
		gameDisplay.blit(bbr5,(xb+850,yb))
	elif b5 ==2:
		gameDisplay.blit(bbb5,(xb+850,yb))




def balls(r,b):
	xr1 = (display_width * 0.05)
	xr2 = xr1 + 100
	xr3 = xr2 + 100
	xr4 = xr3 + 100
	xr5 = xr4 + 100

	yr1 = (display_height * 0.1)
	yr2 = yr1
	yr3 = yr1
	yr4 = yr1
	yr5 = yr1

	xb1 = xr1
	xb2 = xr2
	xb3 = xr3
	xb4 = xr4
	xb5 = xr5

	yb1 = yr1 +100
	yb2 = yb1
	yb3 = yb1
	yb4 = yb1
	yb5 = yb1

	if(r <> 5):
		gameDisplay.blit(rball1,(xr1,yr1))
		if(r <> 4):
			gameDisplay.blit(rball2,(xr2,yr2))
			if(r <> 3):
				gameDisplay.blit(rball3,(xr3,yr3))
				if(r <> 2):
					gameDisplay.blit(rball3,(xr4,yr4))
					if(r <> 1):
						gameDisplay.blit(rball3,(xr5,yr5))

	
	if(b <> 5):
		gameDisplay.blit(bball1,(xb1,yb1))
		if(b <> 4):
			gameDisplay.blit(bball1,(xb2,yb2))
			if(b <> 3):
				gameDisplay.blit(bball1,(xb3,yb3))
				if(b <> 2):
					gameDisplay.blit(bball1,(xb4,yb4))
					if(b <> 1):
						gameDisplay.blit(bball1,(xb5,yb5))

def game_loop():
	gameExit = False
	feedback = 0
	r=0
	b=0
	b1=0
	b2=0
	b3=0
	b4=0
	b5=0
	m=1
	
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
						rball4 = rball3
						rball5 = rball4
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
						bball4 = bball3
						bball5 = bball4 
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
						bball4 = bball3
						bball5 = bball4
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
						rball4 = rball3
						rball5 = rball4
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
						rball4 = rball3
						rball5 = rball4
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
						bball4 = bball3
						bball5 = bball4				
						b+=1
				elif event.key==pygame.K_4:
					steps+=1
					if sball == 2:
						if b4 == 1:
							r-=1
						elif b4 == 2:
							b-=1
						b4 = 2
						feedback = 1
						sball = 0
						bball2 = bball1
						bball3 = bball2
						bball4 = bball3
						bball5 = bball4
						b+=1
					else: 
						if b4 == 1:
							r-=1
						elif b4 == 2:
							b-=1
						feedback = 2
						b4 = 1	 
						sball = 0
						rball2 = rball1
						rball3 = rball2
						rball4 = rball3
						rball5 = rball4
						r+=1
					

				
				elif event.key==pygame.K_5:
					steps+=1
					if sball == 1:
						if b5 == 1:
							r-=1
						elif b5 == 2:
							b-=1
						b5 = 1
						feedback = 1
						sball = 0
						rball2 = rball1
						rball3 = rball2
						rball4 = rball3
						rball5 = rball4
						r+=1
					else: 
						if b5 == 1:
							r-=1
						elif b5 == 2:
							b-=1
						feedback = 2
						b5 = 2	
						sball = 0
						bball2 = bball1
						bball3 = bball2
						bball4 = bball3
						bball5 = bball4				
						b+=1
				

				

		gameDisplay.fill(black)
		box(feedback,b1,b2,b3,b4,b5)
		balls(r,b)
		print(feedback)
		task_complete(b1,b2,b3,b4,b5,m)
		pygame.display.update()
		clock.tick(60)
	



game_loop()
pygame.quit()
quit()



