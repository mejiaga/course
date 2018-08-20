var x = [];
for (var i = 0; i < 500; i++) {
  x[i] = Math.random();
}

var trace = {
  x: x,
  type: "histogram"
};

var data = [trace];

var layout = {
  title: "Histogram with Autobins",
  bargap: 0.05
};

Plotly.newPlot("plot1", data, layout);

var trace2 = {
  x: x,
  type: "histogram",
  autobinx: false,
  xbins: {
    start: 0,
    end: 1,
    size: 0.01
  }
};

var data2 = [trace2];

var layout2 = {
  title: "Histogram with Bin Size 0.01",
  bargap: 0.05
};

Plotly.newPlot("plot2", data2, layout2);

var trace3 = {
  x: x,
  type: "histogram",
  autobinx: false,
  xbins: {
    start: 0,
    end: 1,
    size: 0.5
  }
};

var data3 = [trace3];

var layout3 = {
  title: "Histogram with Bin Size 0.5",
  bargap: 0.05
};

Plotly.newPlot("plot3", data3, layout3);
