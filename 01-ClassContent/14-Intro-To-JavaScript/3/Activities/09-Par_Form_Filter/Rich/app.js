// Assign the data from `data.js` to a descriptive variable
var people = data;

// Select the submit button
var submit = d3.select("#submit");

// Complete the click handler for the form
submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#patient-form-input");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);

  // Use the form input to filter the data by blood type
  var filteredData = people.filter(person => person.bloodType == inputVal);
  console.log(filteredData);
  // BONUS: Calculate summary statistics for the age field of the filtered data

  // First, create an array with just the age values
var ages = filteredData.map(person => person.age);
//var names = filteredData.map(person => person.fullName);
//console.log(names);
  var mean = math.mean(ages)
  var median = math.mean(ages)
  // Next, use math.js to calculate the mean, median, mode, var, and std of the ages

  // Finally, add the summary stats to the `ul` tag
d3.select(".summary")
.append("li").text(`mean:${mean}`)// here we do not end with the semicolo as it will be referenced separately
.append("li").text(`mean:${median}`);

});
