
import xlrd
book = xlrd.open_workbook('明坡小学.xls')
print('sheet页名称:',book.sheet_names())
sheet = book.sheet_by_index(0)
rows = sheet.nrows
cols = sheet.ncols
print('该工作表有%d行，%d列.'%(rows,cols))
print('第三行内容为:',sheet.row_values(2))
print('第二列内容为%s,数据类型为%s.'%(sheet.col_values(1),type(sheet.col_values(1))))
print('第二列内容为%s,数据类型为%s.'%(sheet.col(1),type(sheet.col(1))))
print('第二行第二列的单元格内容为:',sheet.cell_value(1,1))
print('第三行第二列的单元格内容为:',sheet.cell(2,1).value)
print('第五行第三列的单元格内容为:',sheet.row(4)[2].value)
print('第五行第三列的单元格内容为%s,数据类型为%s'%(sheet.col(2)[4].value,type(sheet.col(2)[4].value)))
print('第五行第三列的单元格内容为%s,数据类型为%s'%(sheet.col(2)[4],type(sheet.col(2)[4])))



import xlwt
proj = ['名称','单价/元','库存/kg']
fruit = ['苹果','梨','香蕉','橘子']
price = [8,3.5,4.5,3.8]
storage = [150,130,100,300]
book = xlwt.Workbook()
sheet = book.add_sheet('Sheet1')
for i in range(0,len(proj)):
    sheet.write(0,i,proj[i]) #按行插入行标题
for i in range(0,len(fruit)):
    sheet.write(i+1,0,fruit[i])  #插入第一列水果名称
for i in range(0,len(price)):
    sheet.write(i+1,1,price[i])  #插入第二列单价
for i in range(0,len(storage)):
    sheet.write(i+1,2,storage[i])   #插入第三列库存
book.save('写入表格.xls')

# xlwt逐行或列写入excel





