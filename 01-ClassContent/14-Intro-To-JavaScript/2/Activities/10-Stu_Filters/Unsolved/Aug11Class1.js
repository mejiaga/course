var classText = d3.select(".text1").text(); // . is used to call a class
console.log(classText);

var idText = d3.select("#text2").text();// # is used when we call a id
console.log(idText);

// d3 select
d3.select(".text1").text("Aha, now I can change");

// capture the html link
var aLink = d3.select(".my-link".html)();
console.log("I got a Link for html",aLink);

// get a child element / anchor / href attribute
var aLinkAnch = d3.select(".my-link>a");
console.log("This is the anch: ",aLinkAnch);
var aLinkAnchAttr = aLinkAnch.attr("href");
console.log("This is only the link", aLinkAnchAttr);

// change the attribute
aLinkAnch.attr("href","https://python.org");

// use join method
d3.select(".my-link").attr("href","https://nytimes.org").text("This points to NY Times now")

// select ALL list items and then change the font color
d3.selectAll.("li").style("color",red)