import xlrd
print ('Ahmed')
workbook = xlrd.open_workbook("Corporate APNs.xlsx")
worksheet = workbook.sheet_by_index(0)
print(worksheet)
    #sheet = wb.sheet_by_index(0)

    #for x, y in range(worksheet.nrows):
x= 0
y=10
colx=0
row = worksheet.col_values(colx, start_rowx=0, end_rowx=10)
print(row)