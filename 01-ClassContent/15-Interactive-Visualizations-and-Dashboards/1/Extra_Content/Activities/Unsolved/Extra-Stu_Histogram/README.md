# Speed of Light

In this activity, you will re-create the histogram for a famous experiment to estimate the speed of light.

Abstract: Simon Newcomb measured the time required for light to travel from his laboratory on the Potomac River to a mirror at the base of the Washington Monument and back, a total distance of about 7400 meters. These measurements were used to estimate the speed of light.
A histogram or dotplot of this data shows a normal distribution except for two outliers. Newcomb ultimately dropped the lowest outlier, -44, from his analysis. The average measurement may be used to estimate the speed of light.

## Files

* [plots.js](./plots.js)

* [data.js](./data.js)

* [index.html](./index.html)

## Instructions

* Create a histogram to display the speed of light measurements.

* Adjust the bargap to add seperation between the bins.

## Bonus

* Use the `filterOutliers` function provided to remove outliers from the data array.

* Calculate the `min` and `max` values of the filtered data array and use that for the `start` and `stop` value for the xbins attribute.

* Adjust the number of bins so that the bin with the largest amplitude contains the actual measurement corresponding the the speed of light.

  * Note: measurements were take at a distance of 7400 meters, so `7400/299792458 = 24.68e-6`.
