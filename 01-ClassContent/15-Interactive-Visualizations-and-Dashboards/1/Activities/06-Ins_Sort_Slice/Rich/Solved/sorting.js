// Sorts descending
[3, 2, -120].sort(function compareFunction(firstNum, secondNum) {
   // resulting order is (3, 2, -120)
  return secondNum - firstNum;
});


// Sorts ascending
[3, 2, -120].sort(function compareFunction(firstNum, secondNum) {
  // resulting order is (-120, 2, 3)
  return firstNum - secondNum;
});

// Arrow Function
[3, 2, -120].sort((first, second) => first - second);

