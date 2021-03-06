var w;
var count = 21;
var speed = 1;

function setup() {
  createCanvas(640, 360);
  // Make a Walker object
  w = new Walker();
}

function draw() {
  background(201);
  // Update and display object
  w.update();
  w.display();

  count += speed;

  if(count >= 620 || count <= 20){
   speed *= -1;
  }
  
   print(count);
  
  rect(count,mouseY,60,60);
  rectMode(CENTER);
}

function Walker() {

  // Start Walker in center
  this.pos = createVector(width / 2, height / 2);

  this.update = function() {
    // Move Walker randomly
    var vel = createVector(random(-3, 3), random(-3, 3));
    this.pos.add(vel);
  }

  this.display = function() {
    // Draw Walker as circle
    fill(mouseX,125,125);
    ellipse(this.pos.x, this.pos.y, 50, 50);
  }
}