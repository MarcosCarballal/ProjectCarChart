
var results = decodeHtml(window.results);
var cars = results.cars;
var xLabel = results.xLabel;
var yLabel = results.yLabel;

var w, h;
var o = 25;

function setup() {
  var canvas = createCanvas(500, 500);
  canvas.parent('p5container');
  colorMode(HSB, 100);
  noLoop();
  w = width;
  h = height;
}

function draw() {
  background(60, 30, 100);
  drawGraph();
}

function drawGraph() {
  drawAxes();
  drawLabels();
  plotCars();
}

function drawAxes() {
  push();
  stroke(0);
  strokeWeight(1);
  line(o, h-o, o, o);
  line(o, h-o, w-o, h-o);
  pop();
}

function drawLabels() {
  push();
  translate(o/2, h-o/2);
  textSize(14);
  text("x axis", w/2.3, 5);
  rotate(-PI / 2);
  text("y axis", w/2.3, 5);
  pop();
}

function plotCars() {
  push();
  pop();
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
