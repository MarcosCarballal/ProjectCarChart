var h = 100;
var hDelta = 0.1;

var circles = [];

var sliders;

var graph = {
  xAxis: {
    label: "",
    min: 0,
    max: 10,
  },
  yAxis: {
    label: "",
    min: 0,
    max: 10,
  },
  data: [],
  draw: (x, y) => {
    push();
    translate(x, y);
    noFill();
    stroke(0);
    strokeWeight(3);

    rect(0, 0, 300, 600);
    line(-50, 0, -50, 600)

    pop();
  }
};

function setup() {
  //var canvas = createCanvas(500, 300);
  var canvas = createCanvas(windowWidth, windowHeight);
  //var x = (windowWidth - width) / 2;
  //var y = (windowHeight - height) / 2;
  //canvas.parent('p5container');
  //canvas.position(x, y);
  colorMode(RGB, 255);
}

function draw() {
  background(193, 255, 190, 90);
  stroke(200, 50, 50);
  strokeWeight(2);

  circles.push({
    x: random(0, width),
    y: random(0, height),
    r: random(20, 50),
  });

  graph.draw(100, 100);

  circles.forEach((c) => ellipse(c.x, c.y, c.r, c.r));
  if (circles.length > 30) { circles.shift(); }
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}

function createSlider() {
  return {
    // todo
  }
}

/*{
  "bodyType": "cabriolet",
  "emmissionCO2": "148",
  "seatingCapacity": "2",
  "maxspeed": "232",
  "fuelcapacity": "45",
  "price": "46760",
  "fuelconsumption": "6.4",
  "manufacturer": "Abarth",
  "model": "Abarth 124 Spider"
  "enginePower": "125"
}*/
