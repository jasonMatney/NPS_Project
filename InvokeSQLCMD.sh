Invoke-Sqlcmd -Query "SELECT * FROM dbo.tbl_Consultation;" -Database RTCA  | Export-Csv -NoTypeInformation -Path "C:\Users\jamatney\RTCA_Tables\tbl_Consultaton.csv"
