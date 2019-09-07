/*class Graph() {
  constructor() {
    this.width: 600,
    this.height: 600,
    this.axisOffset: 50,  
    this.xAxis: {
      label: "X-AXIS",
      min: 0,
      max: 10,
    },
    this.yAxis: {
      label: "Y-AXIS",
      min: 0,
      max: 10,
    },
  }
}*/

var graph = {
  
  width: 600,
  height: 600,
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
    let txtSize = 50;
    
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
    textSize(50);
    
    push();
    translate(0, h);
    rotate(-PI / 2);
    text(yLabel, 0, -off-10);
    pop();
    
    push();
    translate(0, h);
    text(xLabel, 0, off+txtSize);
    pop();
    
    pop();
  }
};

