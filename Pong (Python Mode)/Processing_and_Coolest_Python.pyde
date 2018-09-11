# Sarvath Sharma
# May 30, 2017
# Pong game - Coolest Python Assignment Version
# Computer Science 20 // Mr. Schellenberg // Pd. 4
# Credits: Mr. Schellenberg, Alex, Golden and Reference for Processing

xPlayer = 0
heightPlayer = 150
xCPU = 0
heightCPU = 150
cpuY = 0
ballRadius = 35 
xBall = random(150, 201)
yBall = random(150, 201)
xSpeed = random(7, 15)  
ySpeed = random(7, 15)
ySpeedCPU = random(8, 20)
r = int(0)
g = int(0)
b = int(0)
rBall = int(0)
gBall = int(0)
bBall = int(0)
practiceScore = 0
playerScore = 0
cpuScore = 0
numberOfHits = 0
restart = False
practiceMode = True
CPUMode = True
frontScreenMessage = "Pong Game (By: Sarvath Sharma)"
CPUgame = "CPU vs Human (Press s)" 

def setup():
    ''' A core function made for processing that makes the size of the screen used and changes a few global varibles ''' 
    global xPlayer, cpuY
        
    fullScreen()
    xPlayer = width - 50
    cpuY = height/2

def draw():
    ''' A core function made for Processing. This function runs all the codes and will refresh for effiecient work '''
    global frontScreenMessage, practiceMode, CPUgame, practiceMode, xCPU, heightCPU, r, g, b, practiceScore
    
    background(0)
    fill(255)
    textSize(42)
    textAlign(CENTER)
    text(frontScreenMessage, width/2, height/2 - 60)
    text("Practice Mode (Press a)", width/2, height/2 )
    text(CPUgame, width/2, height/2 + 60)
    
    if practiceMode == False:    
        background(r, g, b)
        fill(255)
        practiceBar = rect(0, 0, 50, height)
        playersBar = rect(xPlayer, mouseY - heightPlayer/2, 30, heightPlayer)
        fill(rBall,gBall,bBall)
        ball = ellipse(xBall, yBall, ballRadius*2, ballRadius*2)
        ballBouncePractice()
        ballHitLose()
        increaseSpeed()
        scoreKeep = "Score: " + str(practiceScore)
        fill(255)
        textSize(42)
        textAlign(LEFT)
        text(scoreKeep, TOP, LEFT)
        
    if CPUMode == False:
        background(0)
        fill(random(0,256),random(0,256),random(0,256))
        line(width/2, 0, width/2, height)
        fill(255)
        CPUBar = rect(xCPU + 20, cpuY, 30, heightCPU)
        playersBar = rect(xPlayer, mouseY - heightPlayer/2, 30, heightPlayer)
        fill(rBall,gBall,bBall)
        ball = ellipse(xBall, yBall, ballRadius*2, ballRadius*2)
        ballBounceCPU()
        lostBallCPU()
        whoWins()
        aiBar()
        increaseSpeed()
        fill(255)
        textSize(42)
        textAlign(CENTER)
        cpuPoints = str(cpuScore)
        playerPoints = str(playerScore)
        text(cpuPoints, width/2 - 50, 50)
        text(playerPoints, width/2 + 50, 50) 

def aiBar():
    ''' This function is to make the CPU bar move and play against the player '''
    global cpuY, ySpeedCPU, yBall
    
    if (yBall > cpuY and xBall < displayWidth/2):
        cpuY += ySpeedCPU #Only ySpeedCPU is used is because the bar will only move up and down
    elif (yBall < cpuY + heightCPU and xBall < displayWidth/2):
        cpuY -= ySpeedCPU 
        
def ballBouncePractice():
    ''' This function is made to make the ball bounce of the Practice bar and the player's bar '''
    global yPlayer, yBall, xBall, xSpeed, ySpeed, ballRadius, practiceScore, rBall, gBall, bBall, numberOfHits #to change global variables, need to access the global scope 
    xBall += xSpeed
    yBall += ySpeed
    
    for colours in range(0, 256):
        #This loop was created to have the ball change colours randomly and quickly to confuse the player while playing and give a retro disco theme
        rBall = random(0,256)
        gBall = random(0,256)
        bBall = random(0,256)
    
    #Bounce if required
    if (xBall + ballRadius > width - 50 and xBall + ballRadius < width - 20 and yBall < mouseY + heightPlayer/2 and yBall + ballRadius > mouseY - heightPlayer/2):
        xSpeed = xSpeed * -1
        xBall += xSpeed
        #Whenever the ball hits the bar an ellipse of colour goes off for a very small time
        fill(random(0,256),random(0,256),random(0,256))
        ballHitsBar = random(75,150)
        ellipse(xBall , yBall, ballHitsBar, ballHitsBar)
        practiceScore += 10
        numberOfHits += 1
    elif (xBall - ballRadius < 50):
        xSpeed = xSpeed * -1
        xBall += xSpeed
        fill(random(0,256),random(0,256),random(0,256))
        ballHitsBar = random(75,150)
        ellipse(xBall , yBall, ballHitsBar, ballHitsBar)
    elif (yBall + ballRadius > height or yBall < ballRadius):
        ySpeed = ySpeed * -1

def ballBounceCPU():
    ''' This function is made for the ball and the CPU bar to move and have the player play a game against an AI '''
    global yPlayer, yBall, xBall, xSpeed, ySpeed, ballRadius, score, rBall, gBall, bBall, numberOfHits #to change global variables, need to access the global scope 
    xBall += xSpeed
    yBall += ySpeed
    
    for colours in range(0, 256):
        rBall = random(0,256)
        gBall = random(0,256)
        bBall = random(0,256)
   
    #Bounce if required
    if (xBall + ballRadius > width - 50 and xBall + ballRadius < width - 20 and yBall < mouseY + heightPlayer/2 and yBall + ballRadius > mouseY - heightPlayer/2):
        xSpeed = xSpeed * -1
        xBall += xSpeed
        #Whenever the ball hits the bar an ellipse of colour goes off for a very small time
        fill(rBall, gBall, bBall)
        ellipseDiameter = random(75,150)
        ellipse(xBall , yBall, ellipseDiameter, ellipseDiameter)
        numberOfHits += 1
    elif (xBall - ballRadius < 50 and xBall - ballRadius > 20 and yBall + ballRadius > cpuY and yBall - ballRadius < cpuY + heightCPU):
        xSpeed = xSpeed * -1
        xBall += xSpeed
        fill(random(0,256),random(0,256),random(0,256))
        ellipseDiameter = random(75,150)
        ellipse(xBall , yBall, ellipseDiameter, ellipseDiameter)
    elif (yBall + ballRadius > height or yBall < ballRadius):
        ySpeed = ySpeed * -1
                                             
def ballHitLose():
    ''' If the player loses during the practice the ball respawn is position to restart (loses all points) and the background colour changes (PRACTICE MODE) '''
    global xBall, yBall, xSpeed, ySpeed, practiceScore, r, g ,b, numberOfHits
    
    if (xBall > width):
        #If the player misses the ball, the game restarts
        gameStart = False
        xBall = random(150, 201)
        yBall = random(150, 201)
        xSpeed = random(6, 16)
        ySpeed = random(6, 16)
        r = random(0, 256)
        g = random(0, 256)
        b = random(0, 256)
        practiceScore = 0
        numberOfHits = 0
        
def lostBallCPU():
    ''' If the player loses during the practice the ball respawns to a random position to restart (CPU MODE) '''
    global xBall, yBall, xSpeed, ySpeed, playerScore, cpuScore, numberOfHits
    
    if (xBall > width):
        #If the player misses the ball, the game restarts
        restart = False
        xBall = random(150, 201)
        yBall = random(150, 201)
        xSpeed = random(6, 16)
        ySpeed = random(6, 16)
        cpuScore += 1
        numberOfHits = 0
    if (xBall < 0):
        #If the CPU misses the ball, the game restarts
        restart = False
        xBall = random(150, 201)
        yBall = random(150, 201)
        xSpeed = random(6, 16)
        ySpeed = random(6, 16)
        playerScore += 1
        numberOfHits = 0

def whoWins():
    ''' This code will run to check who reaches 10 points first and play a message '''
    global cpuScore, playerScore

    if cpuScore == 5:
        clear
        background(0)
        fill(random(0,256),random(0,256),random(0,256))
        loser = "Oh well! Good try click on the screen, then press Esc for your surprise."
        textSize(32)
        textAlign(CENTER)
        text(loser, width/2, height/2)
    elif playerScore == 5:
        clear
        background(0)
        fill(random(0,256),random(0,256),random(0,256))
        winner = "Congratulations!!!! Click on the screen, then press Esc for your surprise."
        textSize(32)
        textAlign(CENTER)
        text(winner, width/2, height/2) 
            
def increaseSpeed():
    ''' This function takes note of all the hits made by the player, and increases the speed slowly/highly '''
    global xBall, yBall, xSpeed, ySpeed, numberOfHits
    
    if numberOfHits > 4:
        xBall += xSpeed + 1
        yBall += ySpeed + 1
    if  numberOfHits > 6:
        xBall += xSpeed + 3
        yBall += ySpeed + 3
        
def keyPressed():
    ''' This function was made to help the player use the keyboard during the game ''' 
    global practiceMode, CPUMode
    
    if key == "a":
        practiceMode = True
    if key == "s":
        CPUMode = True

def keyReleased():
    ''' This function was made to help the player use the keyboard during the game '''
    global practiceMode, CPUMode
    
    if key == "a":
        practiceMode = False
    if key == "s":
        CPUMode = False
    