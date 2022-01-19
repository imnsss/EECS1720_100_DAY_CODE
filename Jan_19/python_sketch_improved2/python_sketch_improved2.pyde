

def setup():
    size(800, 400)
            
    # photo = loadImage("1.JPG")
    # photo.resize(50,50)


def draw():
    if  mousePressed and mouseButton == RIGHT:
        fill(0)
        ellipse(mouseX, mouseY, 50, 50)
    if  mousePressed and mouseButton == LEFT:
        fill(255)
        ellipse(mouseX, mouseY, 60, 60)
    
    if keyPressed and key == ' ':
        background(125)
            
    if mouseX > 400:
        cursor(CROSS)
    else:
        cursor(HAND)


    
    for i in range(0, 400, 50):
        line(30, 20+i, 85, 20+i)
        stroke(126)
        line(85, 20+i, 85, 75+i)
        stroke(255)
        line(85, 75+i, 30, 75+i)
        
    for i in range(0,200,50):
        rect(300+i, 50, 50, 50)
        
    rect(200, 50, 50, 50)
        
                      
                      
    # image(photo,random(100,700),random(50,350))
    # imageMode = CENTER
