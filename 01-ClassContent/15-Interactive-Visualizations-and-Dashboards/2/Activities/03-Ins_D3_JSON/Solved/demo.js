/* const url = "https://api.spacexdata.com/v2/launchpads";

// Fetch the JSON data and console log it
d3.json(url).then(function(data) {
  console.log(data);
});

// Promise Pending
const dataPromise = d3.json(url);
console.log("Data Promise: ", dataPromise);*/



/** Class demo below */

const url = "https://api/spacexdata.com/v2/launchpads";

d3.json(url).then(function(data){

    console.log(data);
});

// the data is Promised: that means the data is fetched and held

const dataPromise = d3.json(url);
console.log("The Data Promised is :", dataPromise);
