
import pygame
import random

#for initializing pygame(compulsary line)
pygame.init()

#defining colours in terms of RGB values
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
orange = (255, 128, 0)
pink = (255, 0, 255)
lblue = (0, 255, 255)
black = (0, 0, 0)


#frames per second
FPS = 10

#width and height of the pygame window
displayWidth = 1000
displayHeight = 700

#the maximum and minimum speed of each turtle
speedmax = 5
speedmin = 2

#creating the pygame window
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('TURTLE RACE BY ASUTOSH')

#creating a clock object of the class Clock
clock = pygame.time.Clock()

#loading the turtle images who race
t1 = pygame.image.load('t1.png')
t2 = pygame.image.load('t2.png')
t3 = pygame.image.load('t3.png')
t4 = pygame.image.load('t4.png')
t5 = pygame.image.load('t5.png')
t6 = pygame.image.load('t6.png')
t7 = pygame.image.load('t7.png')
t8 = pygame.image.load('t8.png')

#loading the turtle images for the rankboard
st1 = pygame.image.load('st1.png')
st2 = pygame.image.load('st2.png')
st3 = pygame.image.load('st3.png')
st4 = pygame.image.load('st4.png')
st5 = pygame.image.load('st5.png')
st6 = pygame.image.load('st6.png')
st7 = pygame.image.load('st7.png')
st8 = pygame.image.load('st8.png')

#loading images for the play button
offplay = pygame.image.load('offplay75.png')
onplay = pygame.image.load('onplay75.png')

#loading images for the reset button
offreset = pygame.image.load('offreset75.png')
onreset = pygame.image.load('onreset75.png')

#loading the startline image
startline = pygame.image.load('startline.png')

#loading the finishline image
finishline = pygame.image.load('finishlinef.png')

#here we have defined lists so that we can easily access them in for loops by changing the index and lengthy if elif statements can be avoided
#making a list of the turtle images 
t = [t1, t2, t3, t4, t5, t6, t7, t8]

#list of initial x and y position of all turtles at the starting line
x = [200, 300, 400, 500, 600, 700, 800, 900]
y = [625, 625, 625, 625, 625, 625, 625, 625]

#list of tutle images for rankboard
trank = [st1, st2, st3, st4, st5, st6, st7, st8]

#list of colours
colour = [red, blue, green, yellow, orange, pink, lblue, black]

#filling the background with white
gameDisplay.fill(white)

#necessary statement after every change made to the display surface so that it gets updated
pygame.display.update()


'''this func displays a button at a particular pos and checks for the cursor pos if the cursor pos
happens to be within the area of the button then it makes the button lighter(displays another image
at the same x-y pos), it also checks for mouse clicks within the area of the button and if found
performs a particular action as given in the parameter'''
def button(bx, by, bwidth, bheight, offimg, onimg, action = None):
    #cur is a var that stores the mouse cursor pos as a tupple of x-y coords
    cur = pygame.mouse.get_pos()
    '''click is a var that stores the mouse button pressed status in the form
    of a tupple of 3 elements where all 3 values are 0 if no button is pressed
    first tuple elements is for left mouse button, 2nd for wheel and 3rd for
    right mouse button'''
    click = pygame.mouse.get_pressed()
    if bx + 10 < cur[0] < bx + bwidth - 10 and by + 10 < cur[1] < by + bheight - 10:
        gameDisplay.blit(onimg, (bx, by))
    else:
        gameDisplay.blit(offimg, (bx, by))


    if bx + 10 < cur[0] < bx + bwidth - 10 and by + 10 < cur[1] < by + bheight - 10:    
        if click[0] == 1 and action != None:    
            if action == 'play':
                gameLoop()
  
            elif action == 'reset':
                gameIntro()



'''displays text on the screen'''
def message_to_screen(msg, color, textX, textY, textSize):

    #creating a Font obj
    font = pygame.font.Font("LOOPY_IT.TTF", textSize)
    #rendering makes the text tangible to the pixels on the display screen
    screen_text = font.render(msg, True, color)
    #blit adds the text to yhe screen
    gameDisplay.blit(screen_text, [textX, textY])



'''the intro screen consists of only the turtles at startins line, rank text, finish line
and the play button. If the play button is clicked then ctrl passes to the gameLoop() func
where the play button is no more required and so is replaced by the reset button'''
def gameIntro():

    gintro = True
    

    while gintro:
        

        #for the top right red cross to be able to quit the game when clicked
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen('RANK', black, 22, 5, 50)
        message_to_screen('RANK', yellow, 24, 7, 50)
        
        
        gameDisplay.blit(startline, (175, 605))
        gameDisplay.blit(finishline, (175, 10))
        
        for x4 in range(8):
            gameDisplay.blit(t[x4], (x[x4], y[x4]))

        button(50, 550, 75, 75, offplay, onplay, 'play')
        
        pygame.display.update()
        clock.tick(15)



'''ychange is a list of ints that are all 0 initially but are given a random value
at y=625 i.e. the initial position of the turtles(we don't directly change change
the y coordinate instead we change ychange and add it to y to change y) depending
on how low is the y coordinate value the rankboard is displayed, the turtles leave
a mark of the same colour as their's as they move'''
def gameLoop():
    

##    lead_y1 = 500
##    lead_y1_change = 0
##    lead_y2 = 500
##    lead_y2_change = 0
##    lead_y3 = 500
##    lead_y3_change = 0
##    lead_y4 = 500
##    lead_y4_change = 0
##    lead_y5 = 500
##    lead_y5_change = 0
##    lead_y6 = 500
##    lead_y6_change = 0
##    lead_y7 = 500
##    lead_y7_change = 0
##    lead_y8 = 500
##    lead_y8_change = 0
    x = [200, 300, 400, 500, 600, 700, 800, 900]
    y = [625, 625, 625, 625, 625, 625, 625, 625]
    ychange = [0, 0, 0, 0, 0, 0, 0, 0]
    #y pos of all the turtles to be displayed on the rank board
    yrank = [70, 110, 150, 190, 230, 270, 310, 350]


    gameExit = True
    while gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

                
##            if event.type == pygame.KEYDOWN:
##
##                if event.key == pygame.K_p:
##                    lead_y1_change = random.randrange(1, 10)
##                    lead_y2_change = random.randrange(1, 10)
##                    lead_y3_change = random.randrange(1, 10)
##                    lead_y4_change = random.randrange(1, 10)
##                    lead_y5_change = random.randrange(1, 10)
##                    lead_y6_change = random.randrange(1, 10)
##                    lead_y7_change = random.randrange(1, 10)
##                    lead_y8_change = random.randrange(1, 10)
##                    for x2 in range(8):
##                        yc[x2] = random.randrange(smin, smax)
##        lead_y1 -= lead_y1_change
##        lead_y2 -= lead_y2_change
##        lead_y3 -= lead_y3_change
##        lead_y4 -= lead_y4_change
##        lead_y5 -= lead_y5_change
##        lead_y6 -= lead_y6_change
##        lead_y7 -= lead_y7_change
##        lead_y8 -= lead_y8_change

        gameDisplay.fill(white)
        
        gameDisplay.blit(startline, (175, 605))
        gameDisplay.blit(finishline, (175, 10))
        message_to_screen('RANK', black, 22, 5, 50)
        message_to_screen('RANK', yellow, 24, 7, 50)


        button(50, 450, 75, 75, offreset, onreset, 'reset')

        #to chnage ychange and hence speeds at different y levels           
        for x5 in range(8):
            '''only range of 10 pixels bcoz if we mention a large range then ychange
            varies 15 times per sec bcoz of FPS and hence the motion of the turtles
            will be quite sluggish'''
            if y[x5] <= 600 and y[x5] >= 590:
                ychange[x5] = random.randrange(speedmin, speedmax)
            elif y[x5] <= 500 and y[x5] >= 490:
                ychange[x5] = random.randrange(speedmin, speedmax)
            elif y[x5] <= 400 and y[x5] >= 390:
                ychange[x5] = random.randrange(speedmin, speedmax)
            elif y[x5] <= 200 and y[x5] >= 190:
                ychange[x5] = random.randrange(speedmin, speedmax)
            elif y[x5] <= 100:
                ychange[x5] = 7
            elif y[x5] == 625:
                ychange[x5] = random.randrange(speedmin, speedmax)

   
        for x3 in range(8):
            y[x3] -= ychange[x3]
            
       
        
        yCopy = [0, 0, 0, 0, 0, 0, 0, 0]
        trankCopy = [0, 0, 0, 0, 0, 0, 0, 0]

        #copying the y and trank lists
        for x9 in range(8):
            yCopy[x9] = y[x9]
            trankCopy[x9] = trank[x9]
            
        #sorting the yCopy list(and trankCopy accordingly) so that the rank board can be displayed and updated accordingly
        for x7 in range(8):
            for x8 in range(x7+1, 8):
                if yCopy[x7] > yCopy[x8]:
                    z = trankCopy[x7]
                    trankCopy[x7] = trankCopy[x8]
                    trankCopy[x8] = z
                    z1 = yCopy[x7]
                    yCopy[x7] = yCopy[x8]
                    yCopy[x8] = z1
             
        
        for x6 in range(8):
            if y[x6] <= 615:
                pygame.draw.rect(gameDisplay, colour[x6], (x[x6]+24, y[x6]+48, 2, 563-y[x6]))
##        pygame.draw.rect(gameDisplay, black, (250, 10, 300, 10))
##        pygame.draw.rect(gameDisplay, black, (250, 200, 300, 10))
##        pygame.draw.rect(gameDisplay, red, (290, lead_y1, blockSize, blockSize))
##        pygame.draw.rect(gameDisplay, red, (320, lead_y2, blockSize, blockSize))
##        pygame.draw.rect(gameDisplay, red, (350, lead_y3, blockSize, blockSize))
##        pygame.draw.rect(gameDisplay, red, (380, lead_y4, blockSize, blockSize))
##        pygame.draw.rect(gameDisplay, red, (410, lead_y5, blockSize, blockSize))
##        pygame.draw.rect(gameDisplay, red, (440, lead_y6, blockSize, blockSize))
##        pygame.draw.rect(gameDisplay, red, (470, lead_y7, blockSize, blockSize))
##        pygame.draw.rect(gameDisplay, red, (500, lead_y8, blockSize, blockSize))

        #displaying the turtles
        for x4 in range(8):
            gameDisplay.blit(t[x4], (x[x4], y[x4]))

        #displaying the rank board
        for x6 in range(8):
            gameDisplay.blit(trankCopy[x6], (50, yrank[x6]))
              
            
        pygame.display.update()
        
        #runs the while loop FPS times per sec
        clock.tick(FPS)
gameIntro()
gameLoop()

