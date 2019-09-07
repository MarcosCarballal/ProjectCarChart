var circles = [];
var sliders;

var pressed = false;

var graph = {
  width: 450,
  height: 450,
  axisOffset: 50,  
  xAxis: {
    label: "X-AXIS",
    min: 0,
    max: 10,
  },
  yAxis: {
    label: "Y-AXIS",
    min: 0,
    max: 10,
  },
  data: [],
  draw: (x, y) => {
  
    let w = graph.width;
    let h = graph.height;
    let off = graph.axisOffset;
    let xLabel = graph.xAxis.label;
    let yLabel = graph.yAxis.label;
    let t = 30;
    
    // graph outline & axes
    push();
    
    translate(x, y);
    
    noFill();
    stroke(0);
    strokeWeight(3);
    rect(0, 0, w, h);
    line(-off, 0, -off, h);
    line(0, h + off, w, h + off);
    
    // labels
    noStroke();
    fill(0);
    textSize(t);
    
    push();
    translate(0, h);
    rotate(-PI / 2);
    text(yLabel, 0, -off-10);
    pop();
    
    push();
    translate(0, h);
    text(xLabel, 0, off+t);
    pop();
    
    pop();
  }
};

function setup() {
  var canvas = createCanvas(500, 500);
  canvas.parent('p5container');
  colorMode(HSB, 100);
  noLoop();
}

function draw() {
  background(0, 0, 100);
  graph.draw(325, 25);
  if (pressed) { drawEllipseAtMouse(); }
}

function mousePressed() {
  pressed = true;
}

function mouseReleased() {
  pressed = false;
}

function drawEllipseAtMouse() {
  push();
  translate(mouseX, mouseY);
  noStroke();
  fill(0);
  ellipse(0, 0, 30, 30);
  pop();
}

function keyPressed() {
  if (keyCode == 32) {
    redraw();
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
