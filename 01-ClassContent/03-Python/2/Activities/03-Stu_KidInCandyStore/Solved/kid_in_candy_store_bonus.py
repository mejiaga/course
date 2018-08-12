# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit",
             "Swedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []

# Print all of the candies to the screen and their index in brackets
for candy in candyList:
    print("[" + str(candyList.index(candy)) + "] " + candy)


# Set answer to "yes" for while loop
answer = "yes"


while answer == "yes":

    # Ask which candy the user would like to bring ho
    selected = input("Which candy would you like to bring home? ")

    # Add the candy at the index chosen to the candyCart list
    candyCart.append(candyList[int(selected)])

    # ask the user if they want more candy
    answer = input("Would you like to make another selection? ('yes' or 'no') ")


# Loop through the candyCart to say what candies were brought home
print("I brought home with me...")
for candy in candyCart:
    print(candy)
