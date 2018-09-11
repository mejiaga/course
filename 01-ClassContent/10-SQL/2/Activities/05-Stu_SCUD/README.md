# Seek, Create, Update, and Destroy

## Instructions

* Import the `GlobalFirePower.csv` into a new table within a localhost database.

  * Add a primary key to the table.

  * Find all of those rows that have a "ReservePersonnel" of 0 and then remove these rows from the dataset. **Note** MySQL often adds a safety measure to avoid deleting data. Check [Stack Overflow](https://stackoverflow.com/questions/11448068/mysql-error-code-1175-during-update-in-mysql-workbench) for help.

  * Every country in the world at least deserves one "FighterAircraft". Only seems fair. Lets add one to each nation that has none.

  * Oh no! By updating this column, the values within "TotalAircraftStrength" column are now off for those nations! We've got to [add one](https://stackoverflow.com/a/2680352) to the original number.

  * Find the [Averages](https://www.w3schools.com/sql/sql_count_avg_sum.asp) for `TotalMilitaryPersonnel`, `TotalAircraftStrength`, `TotalHelicopterStrength` and `TotalPopulation`. Record these averages.

  * A new nation has been founded and you are declared its leader! Congratulations! Unfortunately for you, every other nation is now looking to take over your land. Insert a new country with the average values you have just calculated.

## Bonus

* After creating your new nation and some parts of your military strategies, go through each column in the newly created row and update their values in any way that you desire!
