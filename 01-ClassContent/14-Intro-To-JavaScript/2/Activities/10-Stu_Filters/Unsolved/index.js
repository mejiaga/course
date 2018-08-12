// @TODO: Uncomment the following file and complete the code
//        according to the instructions in README.md.

// Roster of player
var roster = [{
  name: "Doug",
  position: "Quarterback",
  madeTeam: true
},
{
  name: "Antonio",
  position: "Tight End",
  madeTeam: true
},
{
  name: "Nick",
  position: "Kicker",
  madeTeam: false
},
{
  name: "Ereck",
  position: "Offensive Live",
  madeTeam: false
},
{
  name: "AJ",
  position: "Line Backer",
  madeTeam: true
}];

// YOUR CODE HERE

function selected_team(player) {
    return player.madeTeam === true; // there is no need to return for a boolean == true
  }
  
  // filter() uses the custom function as its argument
  var made_into_team = roster.filter(selected_team);
  
  // Test
  console.log(made_into_team);
