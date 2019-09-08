
function setup() {
  var canvas = createCanvas(500, 500);
  canvas.parent('p5container');
  colorMode(HSB, 100);
  noLoop();
}

function draw() {
  background(60, 30, 100);
  fill(0);
  ellipse(50,50,50,50);
  var input = "";
  textSize(50);
  text(input, 50, 50);
}
