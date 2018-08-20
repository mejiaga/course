// The filterOutliers function below was adapted from
// https://stackoverflow.com/a/20811670
function filterOutliers(someArray) {

  // Copy the values, rather than operating on references to existing values
  var values = someArray.concat();

  // Then sort
  values.sort(function(a, b) {
    return a - b;
  });

  /* Then find a generous IQR. This is generous because if (values.length / 4)
   * is not an int, then really you should average the two elements on either
   * side to find q1.
   */
  var q1 = values[Math.floor((values.length / 4))];
  // Likewise for q3.
  var q3 = values[Math.ceil((values.length * (3 / 4)))];
  var iqr = q3 - q1;

  // Then find min and max values
  var maxValue = q3 + iqr * 1.5;
  var minValue = q1 - iqr * 1.5;

  // Then filter anything beyond or beneath these values.
  var filteredValues = values.filter(function(x) {
    return (x < maxValue) && (x > minValue);
  });

  // Then return
  return filteredValues;
}

// Filter out the outliers

// Calculate the Min and Max values to set the bin boundaries
// console.log(min, max);

// Create the trace using the min and max as the start and stop for the
// xbins. Adjust the size so that the primary bin encompasses the actual
// value related to the speed of light. Note: measurements were take at a
// distance of 7400 meters, so 7400/299792458 = 24.68e-6. The primary bin
// should contain 24.68.

// Create the layout

// Render the plot
