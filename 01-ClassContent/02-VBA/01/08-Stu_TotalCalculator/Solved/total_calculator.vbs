Sub VariableSetting():

    ' Create variables for the Price, Tax, Quantity, and Total
    Dim Price as Double
    Dim Tax as Double
    Dim Quantity as Double
    Dim Total as Double

    ' Retrieve and store the data values in each variable
    Price = Range("B2").value 
    Tax = Range("C2").value
    Quantity = Range("D2").value

    ' Calculate the total by using each of the variables 
    Total = Price * (1 + Tax) * Quantity

    ' Create a Message Box for the Total and insert into cell
    MsgBox("Your total is $" + str(Total))
    Range("E2").value = Total

End Sub