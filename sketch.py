#Making game like flappy bird
#Fixed collision
#Any potential additions?


#This is a remake of Flappy Bird.
#Controls: Space bar to make the bird fly
#Objective: Avoid hitting pipes and try to get the highest score

import time
import random

global score
global ongoing
ongoing = True
score = 0

class Character(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xspeed = 0
        self.yspeed = 1
        self.gravity = 0.1

    def render(self):
        global ongoing

        noStroke()  #builds player character
        fill(245, 226, 56)
        ellipse(self.x, self.y, 50, 45)
        fill(231, 247, 106)
        ellipse(self.x - 16, self.y - 5, 30, 20)
        fill(252, 179, 8)
        ellipse(self.x + 8, self.y + 9, 35, 20)
        fill(255)
        ellipse(self.x + 14, self.y - 7, 15, 17)
        fill(0)
        ellipse(self.x + 17, self.y - 7, 5, 7)



        if keyPressed and key == " ": #"jump" button
            self.yspeed = -3
            self.gravity = 0.1

        self.yspeed = self.yspeed + self.gravity #player movement
        self.y = self.y + self.yspeed
        self.x = self.x + self.xspeed

        if self.y >= 650 or self.y <= -50: #hitting the bottom or top of the screen (out of bounds)
            ongoing = False

class PipeBottom(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hit = False

    def display(self):
        noStroke() #build pipe
        fill(0)
        rectMode(CENTER)
        stroke(0)
        fill(0,255,0)
        rect(self.x, self.y + 180, self.width, self.height)
        rect(self.x, self.y - 50, 50, 40)
        fill(200)
        ellipse(self.x - 15, self.y - 40,5, 5)
        ellipse(self.x + 15, self.y - 40,5, 5)

    def simulate(self):
        global score
        self.x -= 2    #pipe moves to the left by 2

        if self.x == 350:    #when pipe passes x = 350, create new pipes after it
            newYLoc = random.randint(200, 600)
            pipes.append(PipeTop(590, newYLoc, 50, 500))  #rand(100, 400)
            pipes.append(PipeBottom(590, newYLoc, 50, 500))
        if self.x == 320: #when player passes through pipe, add to score
            score += 1


    def collidePipePlayer(self, playerX, playerY):
        shiftedY = self.y - 40 #adjusted collision box since it would not detect correctly at the top of the pipe
        testX = playerX
        testY = playerY

        if playerX < self.x:   #test all sides of the pipe for collision
            testX = self.x
        elif playerX > self.x + self.width:
            testX = self.x + self.width
        if playerY < shiftedY:
            testY = shiftedY
        elif playerY > shiftedY + self.height:
            testY = shiftedY + self.height

        distance = dist(playerX, playerY, testX, testY) #find distance between pipe and player

        if distance <= 22.5: #if the distance is less than the radius of the player, it will collide
            return True
        
        return False

    def collide(self, player):
        global ongoing
        self.hit = self.collidePipePlayer(player.x + 25, player.y + 25)

        
        if self.hit: #if "hit" is true, the game ends
            time.sleep(0.1)
            ongoing = False
        

        return self.hit

class PipeTop(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y - 500 #adjust y-location of top pipe
        self.width = width
        self.height = height
        self.hit = False

    def display(self):
        stroke(0)
        fill(0)
        rectMode(CENTER)
        fill(0,255,0)
        rect(self.x, self.y, self.width, self.height)
        rect(self.x, self.y + 230, 50, 40)
        fill(200)
        ellipse(self.x - 15, self.y + 220,5, 5)
        ellipse(self.x + 15, self.y + 220,5, 5)
        

    def simulate(self):
        self.x -= 2

    def collidePipePlayer(self, playerX, playerY):
        shiftedY = self.y - 227
        testX = playerX
        testY = playerY

        if playerX < self.x:
            testX = self.x
        elif playerX > self.x + self.width:
            testX = self.x + self.width

        if playerY < shiftedY:
            testY = shiftedY
        elif playerY > shiftedY + self.height:
            testY = shiftedY + self.height

        distance = dist(playerX, playerY, testX, testY)
        
        if distance <= 22.5:
            return True
        
        return False
        
    def collide(self, player):
        global ongoing
        self.hit = self.collidePipePlayer(player.x + 25, player.y + 25) #player location + width/height so it collides at touch

        
        if self.hit:
            time.sleep(0.1)
            ongoing = False
        

        return self.hit


bird = Character(300, 300) #variable for player character
pipes = []
PipeYLoc = random.randint(200, 600) #creates first set of pipes with random y-location
firstPipeTop = PipeTop(590, PipeYLoc, 50, 500)
firstPipeBottom = PipeBottom(590, PipeYLoc, 50, 500)
pipes.append(firstPipeTop)
pipes.append(firstPipeBottom)


def setup():
    size(600,600)
    
def draw():
    global ongoing
    background(79, 202, 240)
    noStroke()

    fill(250) #add clouds
    ellipse(80, 340, 250, 200)
    ellipse(170, 340, 200, 200)
    ellipse(240, 350, 190, 200)
    ellipse(300, 380, 190, 200)

    ellipse(400, 380, 190, 200)
    ellipse(490, 350, 190, 200)
    ellipse(560, 340, 200, 200)
    ellipse(620, 340, 250, 200)

    fill(38, 199, 89) #add green circles in back
    stroke(38, 199, 89)
    ellipse(30, 350, 80, 80)
    ellipse(100, 360, 80, 80)
    ellipse(170, 370, 80, 80)
    ellipse(220, 370, 80, 80)
    ellipse(290, 355, 80, 80)
    ellipse(350, 360, 80, 80)
    ellipse(400, 365, 80, 80)
    ellipse(470, 355, 80, 80)
    ellipse(530, 370, 80, 80)
    ellipse(590, 370, 80, 80)
    rectMode(CENTER)
    fill(91, 224, 88)
    stroke(91, 224, 88)
    rect(300, 550, 600, 400) #add background grass
    fill(237, 213, 159)
    stroke(237, 213, 159)
    rect(300, 580, 600, 400) #add background dirt

    if ongoing == True: #while the game is "onging" (the variable is True)
        bird.render()
        for pipe in pipes:
            if pipe.x < -25:
                pipes.remove(pipe)
            pipe.display()
            pipe.simulate()
            pipe.collide(bird)
        fill(0)
        textSize(30)
        text(str(score), 25, 50)
    else:                        #when the game is over ("ongoing" variable is False)
        rectMode(CENTER)
        stroke(0)
        fill(255)
        rect(300, 300, 450, 300)
        fill(0)
        textSize(70)
        text("GAME", 200, 270)
        text("OVER", 205, 370)
        textSize(30)
        text(str(score), 25, 50)