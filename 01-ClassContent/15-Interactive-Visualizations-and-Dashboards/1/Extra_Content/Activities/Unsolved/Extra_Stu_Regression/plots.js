/**
 * Use the SimpleStats `ss` linearRegression functions to
 * calculate the regression model for the high jump data
 * https://simplestatistics.org/docs/#linearregressionline
 */
function calculateRegressionLine() {
  // the regression model needs data in the format of
  // [[x1, y1], [x2, y2],...,[xn, yn]]
  // loop through the data to create an array of arrays
  // for each x and y values
  // @TODO: YOUR CODE HERE

  // Create a regression object in slope intercept form
  // @TODO: YOUR CODE HERE

  // Create a linear regression function,
  // which provides a y coordinate for any given x coordinate
  // @TODO: YOUR CODE HERE
}

// Calculate the Min and Max values to plot the regression line
var min = Math.min.apply(null, data.year);
var max = Math.max.apply(null, data.year);

// Create a reference to the regressionFunction and use it to calculate
// the y values given the min and max year
var regressionFunction = calculateRegressionLine();
console.log(min, max, regressionFunction(min), regressionFunction(max));

// Create the regression line plot using mode "lines"
// Use the min and max year for the x values and the calculated
// y values from the regression function `regressionFunction(min)`
// @TODO: YOUR CODE HERE
var trace1 = {};


// Create the data trace for the high jump
// @TODO: YOUR CODE HERE
var trace2 = {};

// Create the data array for the plot using both the data trace
// and the linear regression trace
var data = [trace1, trace2];

// Define the plot layout
var layout = {
  title: "Olympic high jump over the years with regression line",
  xaxis: { title: "Year" },
  yaxis: { title: "Olympic High Jump" }
};

// Plot the chart to a div tag with id "plot"
Plotly.newPlot("plot", data, layout);
