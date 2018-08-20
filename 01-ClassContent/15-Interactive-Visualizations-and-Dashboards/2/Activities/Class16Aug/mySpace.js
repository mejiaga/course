const url = "https://api/spacexdata.com/v2/launchpads";

var api = ""
var url = ""



function unpack(data,index){
    return data.map(function(row){
return row[index];

    });

    

}

d3.json(url).then(function(data){

    console.log(data);
});

// the data is Promised: that means the data is fetched and held

const dataPromise = d3.json(url);
console.log("The Data Promised is :", dataPromise);
