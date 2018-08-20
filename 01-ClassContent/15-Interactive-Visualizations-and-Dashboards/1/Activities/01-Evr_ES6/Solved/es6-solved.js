/*
ES6 CONST/LET EXAMPLES
*/

// 1. Scope and `let` keyword

// using var
function logger() {
  // returns "undefined", but code still runs.
  console.log(x);
  var x = "hi";
}
logger();

// using let
function logger2() {
  // ReferenceError: y is not defined. Code will stop execution.
  console.log(y);
  let y = "hello";
}
// logger2();


// 2. Example of const for constant value

// this value is constant, and will refuse attempts at re-assignment.
const myPets = ["dog", "cat", "rabbit", "some endangered species of sea turtle"];

// myPets = "ferret"; //This will not work - stops execution

// myPets = ["wolf", "giraffe", "parrot"]; //This will not work either

// HOWEVER, we can still manipulate Objects and Arrays!
console.log("before: ", myPets);
myPets.pop();
console.log("after: ", myPets);
