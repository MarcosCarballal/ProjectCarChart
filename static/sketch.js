
console.log(decodeHtml(window.results));
var results = JSON.parse(decodeHtml(window.results));
var cars = results.cars;
var xLabel = results.xLabel;
var yLabel = results.yLabel;

var xMin, xMax, yMin, yMax;
var w, h;
var o = 25;

function setup() {
  var canvas = createCanvas(500, 500);
  canvas.parent('p5container');
  colorMode(HSB, 100);
  noLoop();
  w = width;
  h = height;
  console.log(results.cars.length);
  console.log(xLabel);
  console.log(yLabel);
  //createCarTest();
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
  text("y axis", w/2.3, 3);
  pop();
}

function plotCars() {
  for (index in cars) {
    drawCar(cars[index]);
  }
}

// test data
function createCarTest() {
  cars = [];
  for (i = 0; i < 30; i++) {
    cars.push({
      'bodyType': 'cabriolet',
      'emissionsCO2': random(25, 200),
      'seatingCapacity': random(2, 8),
      'price': random(1000, 50000),
      'manufacturer': 'Abarth',
      'model': 'Abarth 124 Spider',
      'year': random(2000, 2020),
      'enginePower': random(0, 200)
    });
  }
}

function setupCars() {
  cars.sort((a, b) => b.price - a.price);
  xMin = cars[0].price;
  xMax = cars[cars.length-1].price;

  cars.sort((a, b) => b.enginePower - a.enginePower);
  yMin = cars[0].enginePower;
  yMax = cars[cars.length-1].enginePower;

  for (index in cars) {
    let car = cars[index];
    let vx = parseFloat(car.price);
    let vy = parseFloat(car.enginePower);
    let vg = parseFloat(car.emissionsCO2);
    car.x = map(vx, xMin, xMax, o, w);
    car.y = map(vy, yMin, yMax, h-o, 0);
    car.g = map(vg, 125, 155, 0, 100);
    car.r = 30;
  }
}

function drawCar(car) {
  push();
  stroke(0);
  strokeWeight(1);
  fill(35, car.g, 100);
  ellipse(car.x, car.y, car.r, car.r);
  pop();
}

function drawCarInfo(car) {
  push();
  translate(car.x, car.y);
  rectMode(CENTER);
  fill(35, car.g, 100, 80);
  stroke(0);
  strokeWeight(1);
  rect(0, 0, 160, 100, 5);
  fill(0);
  textSize(12);
  text(car.model + " " + Math.floor(car.year), -65, -30);
  pop();
}

function mousePressed() {
  redraw();
  for (index in cars) {
    let car = cars[index];
    log()
    let dist = Math.pow((car.x - mouseX), 2) + Math.pow((car.y - mouseY), 2);
    if (dist < Math.pow(car.r/2, 2)) {
      drawCarInfo(car);
      return;
    }
  }
}

function keyPressed() {
  if (keyCode == 27) {
    redraw();
  }
}

function decodeHtml(html) {
  var txt = document.createElement("textarea");
  txt.innerHTML = html;
  return txt.value;
}
