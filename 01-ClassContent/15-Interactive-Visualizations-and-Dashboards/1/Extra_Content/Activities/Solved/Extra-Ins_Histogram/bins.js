// Our "input data"
const numbers = [
  // All in (5, 10)
  8, 9, 7, 6,
  // all in (10, 15)
  11, 15, 12, 14,
  // All in (15, 20)
  18, 19, 17, 17
];

// Boundaries on the thresholds/intervals we care about: 
// (5,10), (10, 15), (15, 20)
const bin1 = [5, 10];
const bin2 = [10, 15];
const bin3 = [15, 20];

// Generate a histogram by hand using these data bins
const histogram = {
  bin1: 3,
  bin2: 3,
  bin3: 3
};
