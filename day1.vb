'VBA
'Data is in column A (just copy/paste into cell A1 in Excel)

Sub day1()
Dim i As Long
Dim sum As Double
Dim comp As Double

sum = 0
comp = 0

For i = 1 To Rows.Count
    If Not IsEmpty(Cells(i, 1).Value) Then
        sum = sum + Cells(i, 1).Value
    Else
        If sum > comp Then
            comp = sum
            Range("B1").Value = comp
        End If
        sum = 0
    End If
Next i
End Sub
