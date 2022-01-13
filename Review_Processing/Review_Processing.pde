PImage img1;
color bgcolor = color(200,200,200);

void setup(){
  size(800,600,P2D);
  background(bgcolor);
  img1 = loadImage("1.JPG");
  imageMode(CENTER);

}

void draw() {
    
  image(img1, 120,450,120,120); // add Image
  
  rectMode(CORNER);
  rect(50,50,400,300);  // draw a rectangle
  fill(mouseX,mouseY,100);
  
  
  if (mousePressed && (mouseButton == LEFT)){
        line(mouseX,mouseY,pmouseX,pmouseY);
     }
  if (mousePressed && (mouseButton == CENTER)) {
        background(201,201,201);      
    }
}
