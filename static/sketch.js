
// var results = document.getElementsById('results').innerHTML;
var results = decodeHtml(window.results);

function setup() {
  var canvas = createCanvas(500, 500);
  canvas.parent('p5container');
  colorMode(HSB, 100);
  //noLoop();
}

function draw() {
  background(60, 30, 100);
  fill(0);
  stroke(0,0,100);
  ellipse(50,50,50,50);
  //text(results, 25, 100);
}

function drawCar(car) {
  let x = 50;
  let y = 50;
  let r = 10;
  push();
  stroke(0);
  strokeWeight(1);
  fill(35, 100, 100);
  ellipse(x, y, r, r);
  pop();
}

function decodeHtml(html) {
  var txt = document.createElement("textarea");
  txt.innerHTML = html;
  return txt.value;
}
