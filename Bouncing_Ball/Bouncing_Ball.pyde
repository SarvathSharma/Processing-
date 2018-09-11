# Bouncing Ball

ballX = 300
ballY = 300
ballRadius = 60
xSpeed = random(3, 8)  #built-in random function returns a float
ySpeed = random(3, 8)

def setup():
    global trump
    size(600, 600)
    trump = loadImage("Trump.png")
    
def draw():
    background(0)
    moveBall()
    displayBall()

def moveBall():
    global ballX, ballY, xSpeed, ySpeed, ballRadius  #to change global variables, need to access the global scope 
    ballX += xSpeed
    ballY += ySpeed
    
    #bounce if required
    if (ballX > width - ballRadius or ballX < 0 + ballRadius):
        xSpeed = xSpeed * -1
    if (ballY + ballRadius > height or ballY < 0 + ballRadius):
        ySpeed = ySpeed * -1
        
def mousePressed():
    global ballX, ballY, xSpeed, ySpeed, ballRadius
    distanceFromBall = dist(mouseX, mouseY, ballX, ballY)
    if distanceFromBall < ballRadius:
        ySpeed = ySpeed * -1
        xSpeed = xSpeed * -1             
        
def displayBall():
    fill(255)
    ellipse(ballX, ballY, ballRadius*2, ballRadius*2)
    imageMode(CENTER)
    image(trump, ballX, ballY, ballRadius*3.5, ballRadius*3.5)