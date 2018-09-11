Sub Variables():

    ' Basic String Variable 
    ' ----------------------------------------
    Dim name as String
    name = "Gandalf"

    msgbox(name)

    ' Basic String Concatenation (Combination)
    ' ----------------------------------------
    Dim title as String
    title = "The Great"

    Dim fullname as String
    fullname = name + " " + title 

    msgbox(fullname)

    ' Basic Integer, Double, Long Variables
    ' ----------------------------------------
    Dim age1 as Integer
    Dim age2 as Integer 
    age1 = 5
    age2 = 10

    Dim price as Double
    Dim tax as Double 
    price = 19.99
    tax = 0.05

    Dim lightspeed as Long
    lightspeed = 299792458

    ' Basic Numeric manipulation
    ' ----------------------------------------
    msgbox(age1 + age2)
    Cells(1,1).value = price * (1 + tax)

    ' String, Numeric Combination (Casting)
    ' ----------------------------------------
    msgbox("I am " + str(age1) + " years old.")

    ' Booleans
    ' ----------------------------------------
    Dim money_grows_on_trees as Boolean
    money_grows_on_trees = False

End Sub