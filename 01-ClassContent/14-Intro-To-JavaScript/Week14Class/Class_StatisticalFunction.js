// Array of movie ratings
var movieScores = [
  4.4,
  3.3,
  5.9,
  8.8,
  1.2,
  5.2,
  7.4,
  7.5,
  7.2,
  9.7,
  4.2,
  6.9
];

// Starting a rating count
var sum = 0;

// Arrays to hold movie scores
var goodMovieScores = [];
var okMovieScores = [];
var badMovieScores = [];

for (var i=0;i<movieScores.length;i++)
var score = movieScores[i]
sum += sum; 
{
    console.log("Iteration # ", i)

  {
    for (var j=0; j<movieScores;j++)
      if (score < 7)
        goodMovieScores = push(score);
        console.log("It is a good Movie");
      elseif(score>5 && score <7)
      okMovieScores = push(score);

        console.log(" They are okMovies");
      
    console.log(movieScores[j]);
  }
}
