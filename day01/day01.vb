' VBA Excel

Sub day1()
    
' column A contain all the data
Range("B:C").ClearContents
    
Dim i As Long
Dim j As Double
Dim sum As Double

sum = 0
j = 1

For i = 1 To Rows.Count
    If Not IsEmpty(Cells(i, 1).Value) Then
        sum = sum + Cells(i, 1).Value
    Else
        If sum <> 0 Then
            Cells(j, 2).Value = sum
        End If
        j = j + 1
        sum = 0
    End If
Next i
Range("B:B").Sort Key1:=Range("B1"), _
                     Order1:=xlDescending, _
                    Orientation:=xlSortColumns
Range("C1").Value = "=sum(B1:B3)" ' Answer is in cell "C1"
End Sub

