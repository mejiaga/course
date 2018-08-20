var trace = {
  x: speedOfLight,
  type: "histogram"
};

var data = [trace];

var layout = {
  bargap: 0.05
};

Plotly.newPlot("plot", data, layout);
