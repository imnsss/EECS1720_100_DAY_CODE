# Quiz 2 - Yizhi Zhou

# 1. My variables, and what I need them to do:

generations = 4;

gcposX = 640;
gcposY = 672;

c1posX = 200;

c5posX = 622;

c5posY = 415;

speedX = 4;

# 2. how to setup: setup(), draw() - like always
def setup():
  size(1000,800);
  smooth();

    
def draw():
  # background(251,128,114);
  global gcposX, gcposY, c1posX, speedX, c5posX, c5posY;
  
  img = loadImage("bg.png")
  image(img, 0, 0, width, height)
  
  robotGP = GrandParent(0, [],  'GrandParent',0, 0);
  robotGP.display()
    
  robotP = Parent(0, [],  'Parent',0, 0);
  robotP.display()
  
  robotGP = Child(0, [],  'Child',0, 0);
  robotGP.display()
  
  robotGC = GrandChild(0, [],  'GrandChild',0, 0);
  robotGC.display()
  
  fill(157,157,157)
  textSize(28)
  text("Grand Parent",100, 30)
  fill(100,200,203)
  textSize(28)
  text("Parent",100, 80)
  fill(125,200,100)
  textSize(28)
  text("Child",100, 130)
  fill(242,168,93)
  textSize(28)
  text("Grand Child",100, 180)


  save("live pic of the botfamily.jpg");


# 3. do you want some interactivity?

def mousePressed():
    global gcposX, gcposY;
    gcposX = mouseX
    gcposY = mouseY
    
def keyPressed():
    global gcposX, gcposY;
    gcposX = mouseX
    gcposY = mouseY



# 4. OOP setup for a python class

class GrandParent(object):
        
    def __init__(self, param, params,  name, x, y):
        self.param = param;
        self.params = params;
        self.x = x;
        self.y = y;
    
    def display(self):
        # Grand-Parent (aka oldest robot)
        fill(157,157,157)
        triangle(500, 120, 480, 150, 520, 150)
        circle(500, 183, 65)    
        line(468, 180, 532, 180)
        line(472, 165, 527, 165)
        line(470, 195, 530, 195)
        
class Parent(object):
    
    def __init__(self, param, params,  name, x, y):
        self.param = param;
        self.params = params;
        self.x = x;
        self.y = y;
        
    def display(self):
        fill(100,200,203)
        triangle(140, 250, 120, 280, 160, 280)
        circle(140, 310, 60)   
  
        fill(82,119,247)
        rect(310, 240, 30, 30)
        circle(325, 300, 60) 
  
        fill(100,200,203)
        triangle(390, 240, 370, 270, 410, 270)
        circle(390, 300, 60)  
  
        fill(157,157,157)
        rect(622, 235, 35, 35)
        circle(640, 300, 60) 
  
        fill(100,200,203)
        ellipse(800, 260, 35, 40)  
        circle(800, 310, 60)
        
        fill(196,131,216)
        rect(848, 245, 35, 35)
        circle(865, 310, 60) 
        
class Child(object):
        
    def __init__(self, param, params,  name, x, y):
        self.param = param;
        self.params = params;
        self.x = x;
        self.y = y;
    
    def display(self):
        global gcposX, gcposY, c1posX, speedX, c5posX, c5posY;
        
        #Child
        
        c1posX += speedX;
        if(c1posX > 220):
            speedX *= -1
        if(c1posX < 50):
            speedX *= -1
            
        c5posX += random(-2,2);    
        c5posY += random(-1,1);       
            
        fill(125,200,100)
        rect(c1posX, 420, 30, 30)
        circle(c1posX +15, 480, 60) 
        
        fill(125,200,100)
        rect(300, 420, 30, 30)
        circle(315, 480, 60)
        
        fill(125,200,100)
        triangle(400, 420, 380, 450, 420, 450)
        circle(400, 480, 60)  
        
        fill(125,200,100)
        triangle(490, 420, 470, 450, 510, 450)
        circle(490, 480, 60)  
        
        fill(157,157,157)
        rect(c5posX, c5posY, 35, 35)
        circle(c5posX+17, c5posY+65, 60)  
        
        fill(242, 93, 165)
        ellipse(760, 430, 35, 40)
        circle(760, 480, 60)  
        
        fill(242, 93, 165)
        triangle(890, 420, 870, 450, 910, 450)
        circle(890, 480, 60)  
        
    
class GrandChild(object):
        
    def __init__(self, param, params,  name, x, y):
        self.param = param;
        self.params = params;
        self.x = x;
        self.y = y;
    
    def display(self):
        global generations, gcposX, gcposY, c1posX, speedX;
        
        #Grand Child
        
        fill(242,168,93)
        circle(gcposX, gcposY-42, 30)
        circle(gcposX, gcposY, 55)  
        
        # fill(100,200,203)
        # circle(640, 630, 30)
        # circle(640, 672, 55)  
        
                    
