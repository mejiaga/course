Sub Begin_Journey()
    
    ' Use conditionals to change message box based on user input
    If (Range("B1").value = 1) Then
        MsgBox("You choose to enter the wooded forest of doom!")

    Elseif (Range("B1").value = 2) Then
        MsgBox("You choose to enter the fiery volcano of doom!")

    Elseif (Range("B1").value = 3) Then
        MsgBox("You choose to enter the terrifying jungle of doom!")

   Elseif (Range("B1").value = 4) Then
        MsgBox("You choose to enter the bathroom")        

    Else
        MsgBox("Try following directions")

    End If
End Sub
