
x = 300
y = 300
movingUp = False
movingDown = False
movingLeft = False
movingRight = False


def setup():
    size(1000, 800)
    
def draw():
    global x, y
    
    background(255)
    rectMode(CENTER)
    fill(0)
    rect(x, y, 100, 100)
    moveSonic()

def moveSonic():
    global x, y, movingUp, movingDown, movingLeft, movingRight
    if movingUp:
        y = y - 5
    elif movingDown:
        y = y + 5
    elif movingLeft:
        x -= 5   #shortcut. Means same thing as x = x - 5
    elif movingRight:
        x += 5   #same as x = x + 5

def keyPressed():
    global movingUp, movingDown, movingLeft, movingRight
    #this function will be called automatically every time a key on the keyboard is pressed
    if key == "w":
        movingUp = True
    elif key == "s":
        movingDown = True
    elif key == "a":
        movingLeft = True
    elif key == "d":
        movingRight = True
        
def keyReleased():
    global movingUp, movingDown, movingLeft, movingRight
    if key == "w":
        movingUp = False
    elif key == "s":
        movingDown = False
    elif key == "a":
        movingLeft = False
    elif key == "d":
        movingRight = False