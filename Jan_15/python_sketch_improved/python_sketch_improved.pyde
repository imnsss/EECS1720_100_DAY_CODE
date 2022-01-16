
# PImage img;

def setup():
    size(800, 400)
    photo = loadImage("cursor.png")
    photo.resize(50,50)
    image(photo,200,200)
    imageMode = CENTER

def draw():
    if  mousePressed and mouseButton == RIGHT:
        fill(0)
        ellipse(mouseX, mouseY, 50, 50)
    if  mousePressed and mouseButton == LEFT:
        fill(255)
        ellipse(mouseX, mouseY, 60, 60)
    
    if keyPressed and key == ' ':
        background(255)
            
    if mouseX > 400:
        cursor(CROSS)
    else:
        cursor(HAND)
