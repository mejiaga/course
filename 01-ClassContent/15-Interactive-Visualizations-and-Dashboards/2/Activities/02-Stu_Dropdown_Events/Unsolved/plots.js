function init() {
  var data = [{
    values: [19, 26, 55, 88],
    labels: ["Spotify", "Soundcloud", "Pandora", "Itunes"],
    type: "pie"
    
  }];

  var layout = {
    height: 600,
    width: 800
  };

  Plotly.plot("pie", data, layout);
}

function updatePlotly(newdata) {
  // YOUR CODE HERE
  var mypie = document.getElementById("plot");

  // Note the extra brackets around 'newx' and 'newy'
  Plotly.restyle(mypie, "x", [newx]);
 // Plotly.restyle(mypie, "y", [newy]);
  // Use `Plotly.restyle` to update the pie chart with the newdata array
}

function getData(dataset) {
  // YOUR CODE HERE
  var x = [];
  var y = [];
  // create a select statement to select different data arrays (YOUR CHOICE)
  // whenever the dataset parameter changes. This function will get called
  switch (dataset) {
    case "dataset1":
      data = [1, 2, 3, 4, 5];
      
      break;
      case "dataset2":
      data = [10, 20, 30, 40, 50];
     
      break;
    case "dataset3":
    data = [100, 200, 300, 400, 500];
     
      break;
    default:
      data = [1, 2, 3, 4, 5];
      
      break;
    }
  
    updatePlotly(x, y);
  }
  // from the dropdown event handler.
  updatePlotly(newdata);
}

init();
