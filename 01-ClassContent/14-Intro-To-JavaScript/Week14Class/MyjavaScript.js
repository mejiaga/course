// it is a good practice to end a statements by semicolon

var firstArray = ["a","b","c","d","e"];

//aLetter will be d
var aLetter = firstArray[3];

// array length
var lenArray = length(firstArray);

// to add
firstArray.push("e");   // palm to get or pull

var firstThree = firstArray.slice(0,2);

var fStr = "This is the first string.";
var sStr = "This is the second string";

// split and join
var splitFstr = fStr.split(" ");

var joinFstr = fStr.join(sStr);
// or we can use + to concatinate

//////////////////////////////////
for (var i=0;i<10;i++)
{
    console.log("Iteration # ", i)

}

var students = ["John", "Tyler"];
{
    for (var j=0; j<students.length;j++)
    console.log(students[j]);
}



