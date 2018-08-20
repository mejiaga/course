// @TODO: Complete the following sections

console.log(data);
// Sort the data array using the greekSearchResults value
[3, 2, -120].sort(function compareFunction(a,b) {
    // resulting order is (3, 2, -120)
   return parseFloat(b.greekSearchResults) -parseFloat(b.greekSearchResults) ;
 });

// Slice the first 10 objects for plotting
const dataSlice = data.slice(0, 10);
console.log(left);
// Trace1 for the Greek Data
var trace1 = {
    x: [1, 2, 3, 4, 5],
    y: randomNumbersBetween0and9(5),
    type: "scatter"
  };

  var trace1 = {
    x:dataSlice.map(row => row.greekSearchResults),
    y: dataSlice.map(row => row.greekName),
    text: dataSlice.map(row => row.greekName),
    name:"Greek",
    type: "bar",
    orientation:"h"
  };
// set up the data variable
var data = [trace1];
// set up the layout variable
var layout = {
    title:"Greek Gods",
    margin:{
        l:50,
        r:50,
        t:50,
        b:50

    }
};
// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", data);
