import openpyxl

wb = openpyxl.load_workbook('student.xlsx')
sheet1 = wb.sheetnames
sheet = wb['Sheet1']
name = ['Emjay', 'Gospel', 'Chibe', 'Musa', 'Sponge']

#for n in name:
#    sheet['A' + str(j)] = n
for i,j in range(1, len(name)):
        sheet['A' + str(j)] = name[j-1]
wb.save('student.xlsx')
print(sheet1)