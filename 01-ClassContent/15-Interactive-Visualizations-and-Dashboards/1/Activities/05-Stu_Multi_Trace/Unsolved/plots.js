console.log(data);
// YOUR CODE HERE

function popularGod(n) {
    var popularGodArray = [];
    for (var i = 0; i < n; i++) {
        popularGodArray.push(Math.floor(Math.random() * 10));
    }
    return popularGodArray;
}

// create trace 1
var trace1 = {
    x: data.map(row => row.pair),
    y: data.map(row => row.greekSearchResults),
    name: "Greek",
    text: data.map(row=>row.greekName),
    type: "bar",
};

var trace2 = {
    x: data.map(row => row.pair),
    y: data.map(row => row.romanSearchResults),
    name: "Roman",
    text: data.map(row => row.romanName),
    type: "bar",
};



var data = [trace1, trace2];

// Apply group for bar graph. It can not be done without layout
var layout = {
    title: "Bar Chart",
    barmode = "group"  // group is a keyword
};

Plotly.newPlot("plot", data, layout);