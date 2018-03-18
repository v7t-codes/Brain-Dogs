import pygame
import time
import csv

pygame.init()

display_width = 1300
display_height = 900


black = (0,0,0)
white = (255,255,255)

def init():
	name=raw_input("Enter name ")
	m= input("Enter pattern no.: ")
	return (name,m)

(name,m)=init()

gameDisplay = pygame.display.set_mode((display_width,display_height)) 
pygame.display.set_caption('Take a leep of faith')
clock = pygame.time.Clock()


box1 = pygame.image.load('images/box.png')
rball1 = pygame.image.load('images/rball.png')
bball1 = pygame.image.load('images/bball.png')
rlight = pygame.image.load('images/rlight.png')
ylight = pygame.image.load('images/ylight.png')
glight = pygame.image.load('images/glight.png')
bbr1 = pygame.image.load('images/rball.png')
bbb1 = pygame.image.load('images/bball.png')
box1 = pygame.transform.scale(box1, (170, 170))
ylight = pygame.transform.scale(ylight, (140, 140))
rlight = pygame.transform.scale(rlight, (140, 140))
glight = pygame.transform.scale(glight, (140, 140))
rball = pygame.transform.scale(rball1, (100, 100))
rball_s = pygame.transform.scale(rball1, (120, 120))
bball = pygame.transform.scale(bball1, (100, 100))
bball_s = pygame.transform.scale(bball1, (120, 120))
bbr = pygame.transform.scale(bbr1, (100, 100))
bbb = pygame.transform.scale(bbb1, (100, 100))


xb = (display_width * 0.05)-50
yb = (display_height * 0.6)-50
xl = xb+1000+50
yl = yb-330-100

aball = rball1
gameDisplay.blit(ylight,(xl,yl))

def text_objects(text,font):
	textSurface = font.render(text,True,white)
	return textSurface, textSurface.get_rect()
def message_display():
	text = "Task Complete"
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf,TextRect = text_objects(text,largeText)
	TextRect.center = ((display_width/2),(display_height/2)-100)
	gameDisplay.blit(TextSurf,TextRect)

	pygame.display.update()
	time.sleep(2)


def fb(m,b,i):
	if m == 1: 	 #odd = red, even = blue
		if (i%2 != 0 and b == 1) or (i%2 == 0 and b == 2):
			return 1
		else:
			return 2
	elif m == 2:	#odd = blue, even = red
		if(i%2 != 0 and b == 2) or (i%2 == 0 and b == 1):
			return 1
		else:
			return 2
	elif m == 3:	#prime = red
		if ((i == 2 or i == 3 or i == 5 or i == 7) and (b == 1)) or ((i == 1 or i == 4 or i == 6) and (b == 2)):
			return 1
		else:
			return 2
	elif m == 4:	# prime = blue
		if ((i == 2 or i == 3 or i == 5 or i == 7) and (b == 2)) or ((i == 1 or i == 4 or i == 6) and (b == 1)):
			return 1
		else:
			return 2
	elif m == 5:	#all red
		if(b ==1):
			return 1
		else:
			return 2
	elif m == 6:	#all blue
		if(b == 2):
			return 1
		else:
			return 2
	else:
		pygame.quit()
				
		


def last(name,steps,tt):
	print "Second Task Completed by ",name," in"
	print steps," steps and ",tt," Seconds"
	with open('task2_data.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow([name, steps,tt])
		f.close()

	

def task_complete(b1,b2,b3,b4,b5,b6,b7,m): 
	if m == 1:
		if (b1,b2,b3,b4,b5,b6,b7) == (1,2,1,2,1,2,1):
			return 1
		else:
			return 2
	elif m == 2:
		if (b1,b2,b3,b4,b5,b6,b7) == (2,1,2,1,2,1,2):
			return 1
		else:
			return 2
	elif m == 3:
		if (b1,b2,b3,b4,b5,b6,b7) == (2,1,1,2,1,2,1):
			return 1
		else:
			return 2
	elif m == 4:
		if (b1,b2,b3,b4,b5,b6,b7) == (1,2,2,1,2,1,2):
			return 1
		else:
			return 2
	elif m == 5:
		if (b1,b2,b3,b4,b5,b6,b7) == (1,1,1,1,1,1,1):
			return 1
		else:
			return 2
	elif m == 6:
		if (b1,b2,b3,b4,b5,b6,b7) == (2,2,2,2,2,2,2):
			return 1
		else:
			return 2

	

	

def box(feedback,b1,b2,b3,b4,b5,b6,b7):
	gameDisplay.blit(box1,(xb-10,yb+20))
	gameDisplay.blit(box1,(xb+200-30,yb+20))
	gameDisplay.blit(box1,(xb+400-50,yb+20))
	gameDisplay.blit(box1,(xb+600-60,yb+20))
	gameDisplay.blit(box1,(xb+800-70,yb+20))
	gameDisplay.blit(box1,(xb+1000-80,yb+20))	
	gameDisplay.blit(box1,(xb+1200-90,yb+20))	
	
	if feedback == 2: 
		gameDisplay.blit(rlight,(xl,yl))
		#pygame.mixer.music.load("electric.mp3")
		#pygame.mixer.music.play()
		#time.sleep(2)
	elif feedback == 1:
		gameDisplay.blit(glight,(xl,yl))
	else:
		gameDisplay.blit(ylight,(xl,yl))

	if b1 == 1:
		gameDisplay.blit(bbr,(xb+50-20,yb))
	elif b1 == 2:
		gameDisplay.blit(bbb,(xb+50-20,yb))
	if b2 == 1:
		gameDisplay.blit(bbr,(xb+250-40,yb))
	elif b2 == 2:
		gameDisplay.blit(bbb,(xb+250-40,yb))
	if b3 == 1:	
		gameDisplay.blit(bbr,(xb+450-60,yb))
	elif b3 ==2:
		gameDisplay.blit(bbb,(xb+450-60,yb))
	if b4 == 1:	
		gameDisplay.blit(bbr,(xb+650-70,yb))
	elif b4 ==2:
		gameDisplay.blit(bbb,(xb+650-70,yb))
	if b5 == 1:	
		gameDisplay.blit(bbr,(xb+850-80,yb))
	elif b5 ==2:
		gameDisplay.blit(bbb,(xb+850-80,yb))
	if b6 == 1:	
		gameDisplay.blit(bbr,(xb+1050-90,yb))
	elif b6 ==2:
		gameDisplay.blit(bbb,(xb+1050-90,yb))
	if b7 == 1:	
		gameDisplay.blit(bbr,(xb+1250-100,yb))
	elif b7 ==2:
		gameDisplay.blit(bbb,(xb+1250-100,yb))




def balls(r,b,s):
	xr1 = (display_width * 0.05)
	xr2 = xr1 + 100
	xr3 = xr2 + 100
	xr4 = xr3 + 100
	xr5 = xr4 + 100
	xr6 = xr5 + 100
	xr7 = xr6 + 100

	yr1 = (display_height * 0.1)
	yr2 = yr1
	yr3 = yr1
	yr4 = yr1
	yr5 = yr1
	yr6 = yr1
	yr7 = yr1

	xb1 = xr1
	xb2 = xr2
	xb3 = xr3
	xb4 = xr4
	xb5 = xr5
	xb6 = xr6
	xb7 = xr7

	yb1 = yr1 +100
	yb2 = yb1
	yb3 = yb1
	yb4 = yb1
	yb5 = yb1
	yb6 = yb1
	yb7 = yb1


	if(r <> 7):
		if(s == 1):
			gameDisplay.blit(rball_s,(xr1,yr1))
		else:
			gameDisplay.blit(rball,(xr1,yr1))
		if(r <> 6):
			gameDisplay.blit(rball,(xr2,yr2))
			if(r <> 5):
				gameDisplay.blit(rball,(xr3,yr3))
				if(r <> 4):
					gameDisplay.blit(rball,(xr4,yr4))
					if(r <> 3):
						gameDisplay.blit(rball,(xr5,yr5))
						if(r <> 2):
							gameDisplay.blit(rball,(xr6,yr6))
							if(r <> 1):
								gameDisplay.blit(rball,(xr7,yr7))

	
	if(b <> 7):
		if(s == 2):
			gameDisplay.blit(bball_s,(xb1,yb1))
		else:
			gameDisplay.blit(bball,(xb1,yb1))
		if(b <> 6):
			gameDisplay.blit(bball,(xb2,yb2))
			if(b <> 5):
				gameDisplay.blit(bball,(xb3,yb3))
				if(b <> 4):
					gameDisplay.blit(bball,(xb4,yb4))
					if(b <> 3):
						gameDisplay.blit(bball,(xb5,yb5))
						if(b <> 2):
							gameDisplay.blit(bball,(xb6,yb6))
							if(b <> 1):
								gameDisplay.blit(bball,(xb7,yb7))

def game_loop(m):
	gameExit = False
	feedback = 0
	pf=0
	r=0
	b=0
	b1=0
	b2=0
	b3=0
	b4=0
	b5=0
	b6=0
	b7=0
	s=0
	
	sball = 0
	steps = 0
	now = time.localtime(time.time())
	start_mins = now[4]
	start_secs = now[5]

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					aball = rball1
					sball = 1
					s=1
				elif event.key == pygame.K_a:
					aball = bball1
					sball = 2
					s=2
				elif event.key==pygame.K_1:
					steps+=1
					if sball == 1:
						if b1 == 1:
							r-=1
						elif b1 == 2:
							b-=1
						b1 = 1	
						sball = 0
						rball2 = rball1
						rball3 = rball2
						rball4 = rball3
						rball5 = rball4
						rball6 = rball5
						rball7 = rball6
						r+=1
					else: 
						if b1 == 1:
							r-=1
						elif b1 == 2:
							b-=1
						b1 = 2	
						sball = 0
						bball2 = bball1
						bball3 = bball2
						bball4 = bball3
						bball5 = bball4 	
						bball6 = bball5
						bball7 = bball6	
						b+=1
					feedback = fb(m,b1,1)
					s=0

				elif event.key==pygame.K_2:
					steps+=1
					if sball == 2:
						if b2 == 1:
							r-=1
						elif b2 == 2:
							b-=1
						b2 = 2	
						sball = 0
						bball2 = bball1
						bball3 = bball2
						bball4 = bball3
						bball5 = bball4	
						bball6 = bball5
						bball7 = bball6	
						b+=1
					else: 
						if b2 == 1:
							r-=1
						elif b2 == 2:
							b-=1
						b2 = 1		 
						sball = 0
						rball2 = rball1
						rball3 = rball2
						rball4 = rball3
						rball5 = rball4
						rball6 = rball5
						rball7 = rball6
						r+=1
					feedback = fb(m,b2,2)
					s=0

				elif event.key==pygame.K_3:
					steps+=1
					if sball == 1:
						if b3 == 1:
							r-=1
						elif b3 == 2:
							b-=1
						b3 = 1	
						sball = 0
						rball2 = rball1
						rball3 = rball2
						rball4 = rball3
						rball5 = rball4
						rball6 = rball5
						rball7 = rball6
						r+=1
					else: 
						if b3 == 1:
							r-=1
						elif b3 == 2:
							b-=1
						b3 = 2	
						sball = 0
						bball2 = bball1
						bball3 = bball2
						bball4 = bball3
						bball5 = bball4		
						bball6 = bball5
						bball7 = bball6				
						b+=1
					feedback = fb(m,b3,3)
					s=0

				elif event.key==pygame.K_4:
					steps+=1
					if sball == 2:
						if b4 == 1:
							r-=1
						elif b4 == 2:
							b-=1
						b4 = 2	
						sball = 0
						bball2 = bball1
						bball3 = bball2
						bball4 = bball3
						bball5 = bball4	
						bball6 = bball5
						bball7 = bball6	
						b+=1
					else: 
						if b4 == 1:
							r-=1
						elif b4 == 2:
							b-=1
						b4 = 1		 
						sball = 0
						rball2 = rball1
						rball3 = rball2
						rball4 = rball3
						rball5 = rball4
						rball6 = rball5
						rball7 = rball6
						r+=1
					feedback = fb(m,b4,4)
					s=0
					

				
				elif event.key==pygame.K_5:
					steps+=1
					if sball == 1:
						if b5 == 1:
							r-=1
						elif b5 == 2:
							b-=1
						b5 = 1	
						sball = 0
						rball2 = rball1
						rball3 = rball2
						rball4 = rball3
						rball5 = rball4
						rball6 = rball5
						rball7 = rball6
						r+=1
					else: 
						if b5 == 1:
							r-=1
						elif b5 == 2:
							b-=1
						b5 = 2	
						sball = 0
						bball2 = bball1
						bball3 = bball2
						bball4 = bball3
						bball5 = bball4	
						bball6 = bball5
						bball7 = bball6					
						b+=1
					feedback = fb(m,b5,5)
					s=0

				elif event.key==pygame.K_6:
					steps+=1
					if sball == 1:
						if b6 == 1:
							r-=1
						elif b6 == 2:
							b-=1
						b6 = 1	
						sball = 0
						rball2 = rball1
						rball3 = rball2
						rball4 = rball3
						rball5 = rball4
						rball6 = rball5
						rball7 = rball6
						r+=1
					else: 
						if b6 == 1:
							r-=1
						elif b6 == 2:
							b-=1
						b6 = 2	
						sball = 0
						bball2 = bball1
						bball3 = bball2
						bball4 = bball3
						bball5 = bball4		
						bball6 = bball5
						bball7 = bball6				
						b+=1
					feedback = fb(m,b6,6)
					s=0

				elif event.key==pygame.K_7:
					steps+=1
					if sball == 1:
						if b7 == 1:
							r-=1
						elif b7 == 2:
							b-=1
						b7 = 1	
						sball = 0
						rball2 = rball1
						rball3 = rball2
						rball4 = rball3
						rball5 = rball4
						rball6 = rball5
						rball7 = rball6
						r+=1
					else: 
						if b7 == 1:
							r-=1
						elif b7 == 2:
							b-=1
						b7 = 2	
						sball = 0
						bball2 = bball1
						bball3 = bball2
						bball4 = bball3
						bball5 = bball4	
						bball6 = bball5
						bball7 = bball6			
						b+=1
					feedback = fb(m,b7,7)
				

				
		gameDisplay.fill(black)
		box(feedback,b1,b2,b3,b4,b5,b6,b7)
		balls(r,b,s)
		ffb=task_complete(b1,b2,b3,b4,b5,b6,b7,m)
		pygame.display.update()
		clock.tick(60)
		if(ffb==1):
			message_display()
			break
	now = time.localtime(time.time())
	stop_mins = now[4]
	stop_secs = now[5]
	tt = (stop_mins-start_mins)*60+(stop_secs-start_secs)
	return (steps,tt)
	


(steps,tt)=game_loop(m)
pygame.quit()
last(name,steps,tt)
quit()



