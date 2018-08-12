// Select the submit button
var submit = d3.select("#submit");

submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#example-form-input");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);

  // Set the span tag in the h1 element to the text
  // that was entered in the form
  d3.select("h1>span").text(inputValue);
});
