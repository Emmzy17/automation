import openpyxl

wb = openpyxl.load_workbook('sales.xlsx')
sheets = wb.sheetnames
userSheet = wb['Users']
saleSheet = wb['Sales']
#newSheet = wb.create_sheet('new sheet')
#print(wb.active)
#wb.save('sales.xlsx')
#wb.remove_sheet('new sheet1')
#wb.save('sales.xlsx')
dict_cell = userSheet._cells
for column in userSheet.columns:
    print(column[0].value,column[1].value, column[2].value,column[3].value)

print(saleSheet.dimensions)
print(userSheet['b2'].value)

