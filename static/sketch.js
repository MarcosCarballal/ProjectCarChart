
var results = JSON.parse(decodeHtml(window.results));

if (!results) {
  results = {
    cars: [],
    xLabel: "price",
    yLabel: "enginePower"
  }
}


var cars = results.cars;
console.log(cars[0]);
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
  console.log(cars.length);
  console.log(xLabel);
  console.log(yLabel);
  setupCars();
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
  text(xLabel, w/2.3, 5);
  rotate(-PI / 2);
  text(yLabel, w/2.3, 3);
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

// function setupCars() {
//   cars.sort((a, b) => b[xLabel] - a[xLabel]);
//   xMin = cars[0][xLabel];
//   xMax = cars[cars.length-1][xLabel];
//
//   cars.sort((a, b) => b[yLabel] - a[yLabel]);
//   yMin = cars[0][yLabel];
//   yMax = cars[cars.length-1][yLabel];
//
//   for (index in cars) {
//     let car = cars[index];
//     let vx = parseFloat(car[xLabel]);
//     let vy = parseFloat(car[yLabel]);
//     let vg = parseFloat(car.emissionsCO2);
//     car.x = map(vx, xMin, xMax, o, w);
//     car.y = map(vy, yMin, yMax, h-o, 0);
//     car.g = map(vg, 125, 155, 0, 100);
//     car.r = 5;
//   }
// }

function setupCars() {
  if (!cars) {
    cars = [];
    return;
  }

  cars.sort((a, b) => a.price - b.price);
  xMin = cars[0].price;
  xMax = cars[cars.length-1].price;

  cars.sort((a, b) => a.enginePower - b.enginePower);
  yMin = cars[0].enginePower;
  yMax = cars[cars.length-1].enginePower;

  while (cars[0].enginePower == 0) {
    cars.shift();
  }

  cars.sort((a, b) => a.emissionsCO2 - b.emissionsCO2);
  eMin = cars[0].emissionsCO2;
  eMax = cars[cars.length-1].emissionsCO2;
  console.log(eMin);
  console.log(eMax);

  for (index in cars) {
    let car = cars[index];
    let vx = parseFloat(car.price);
    let vy = parseFloat(car.enginePower);
    let vg = parseFloat(car.emissionsCO2);
    car.x = map(vx, xMin, xMax, o, w-o);
    car.y = map(vy, yMin, yMax, h-o, o);
    car.g = map(vg, 50, 350, 0, 100);
    car.r = 15;
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
  let iw = 160;
  let ih = 100;
  let tx = car.x;
  let ty = car.y;
  let o = 10;
  if (tx < iw/2 + o) { tx = iw/2 + o; }
  if (tx > w - iw/2 - o) { tx = w - iw/2 - o; }
  if (ty < ih/2 + o) { ty = ih/2 + o; }
  if (ty > h - ih/2 - o) { ty = h - ih/2 - o; }
  push();
  translate(tx, ty);
  rectMode(CENTER);
  fill(35, car.g, 100, 80);
  stroke(0);
  strokeWeight(1);

  rect(0, 0, 160, 100, 5);

  fill(0);
  textSize(12);
  text(car.model + " " + Math.floor(car.year), -65, -30);
  text(car.price + " (euros)", -65, -15);
  text(car.enginePower + " kwH", -65, 0);
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
