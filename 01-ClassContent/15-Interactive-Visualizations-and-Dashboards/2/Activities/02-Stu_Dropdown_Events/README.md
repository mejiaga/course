# Dynamic Pie Chart with Dropdown

In this activity, you will use a dropdown selector to choose from one of three datasets to update the pie chart.

## Instructions

* Review the drop down select element in the `index.html` file to see what options will be sent to the `getData` function.

* Complete the `getData` function to choose a new data array depending on which dataset was selected. You can choose the new data values. Write a switch statement to choose between the datasets based on the value selected from the html dropdown select element.

* Complete the `updatePlotly` function to use `Plotly.restyle` to update the chart data with a new data array.

## Hints

* Remember that `Plotly.restyle` requires an extra set of square brackets around the data arrays.
