function setup() {
  createCanvas(800, 800);
  fill(0);
  textSize(100);

}

var value = 0;


function draw() {
  background(0);
  text(key, 200, 200);
  text(key, 100, 100);
  text(key, 150, 150);
  text(key, 600, 600);
  text(key, 650, 650);
  text(key, 700, 700);
  rect(200, 200, 400, 400);
  
}

function keyPressed() {
  if (keyCode === 65) {
    fill(102, 51, 153);
}
  if (keyCode === 66) {
    fill(82, 179, 217);
}
  if (keyCode === 67) {
    fill(58, 83, 155);
}

  if (keyCode === 68) {
    fill(0, 230, 64);
}

  //} else {
   // fill(255);
 // }
}