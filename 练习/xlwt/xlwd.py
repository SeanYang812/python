import xlwt

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf8')

# 创建一个worksheet
worksheet = workbook.add_sheet('my_worksheet')

# 写入excel
# 参数对应 行， 列， 值
worksheet.write(0,0,label = 'this is test')

# 保存
workbook.save('test.xls')