Sub Easy()
    dim ws as Worksheet
    For Each ws In WorkSheets
        ws.Activate
        dim rowCount As Long
        dim x As Integer 
        dim total As LongLong
        dim ticker As String 

        ws.Range("I1").Value = "Ticker"
        ws.Range("J1").Value = "Total Stock Volume"

        rowCount = ws.Cells(1,1).End(xlDown).Row 
        x = 2
        total = 0

        For i = 2 To rowCount
            If Not Cells(i, 1).Value = Cells(i+1,1).Value Then 
                ticker = Cells(i,1).Value 
                total = total + Cells(i,7).Value
                Range("I" & x).Value = ticker 
                Range("J" & x).Value = total 
                x = x + 1
                total = 0
            Else
                total = total + Cells(i,7).Value
            End If
        Next i 
    Next ws 
End Sub 


Sub Moderate()
    dim ws As Worksheet 
    For Each ws in WorkSheets
        ws.Activate
        
        dim x As Integer 
        dim first, last As Double
        dim rowCount As Long
        dim this, that As String
        dim yearly, percent As Range 

        x = 2
        first = Range("C2").Value
        rowcount = ws.Cells(1,1).End(xlDown).Row 

        ws.Range("K1").Value = "Yearly Change"
        ws.Range("L1").Value = "Percent Change"

        For i = 2 To rowCount 
            this = ws.Cells(i,1).Value
            that = ws.Cells(i+1,1).Value
            Set yearly = ws.Cells(x, 11)
            Set percent = ws.Cells(x, 12)

            If Not this = that Then 
                last = ws.Cells(i,6).Value 
                yearly.Value = last - first
                first = ws.Cells(i+1,3).Value 

                'If yearly.Value > 0 Then
                 '   yearly.Interior.Color = 4
                'Else 
                 '   yearly.Interior.Color = 3
                'End If 

                x = x + 1 
            End If 
        Next i 
    Next ws 
End Sub 