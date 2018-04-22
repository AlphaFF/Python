#!/usr/bin/env python3
#coding:utf-8

#表格的读写


#表格的读取
import xlrd
import xlwt

def read_excel(path):
	workbook = xlrd.open_workbook(path)

	#文件中所有表格的名字
	sheet_names = workbook.sheet_names()
	print(sheet_names)

	#获取对应的表格

	#根据索引获取
	sheet = workbook.sheet_by_index(0)
	#根据表名获取
	sheet = workbook.sheet_by_name(sheet_names[0])

	#表的名称、行数、列数
	print(sheet.name,sheet.nrows,sheet.ncols)

	#获取整行或整列的值

	#获取第四行的值
	rows = sheet.row_values(3)
	#获取第三列的值
	cols = sheet.col_values(2)

	#获取单元格的内容
	value1 = sheet.cell(0,4).value
	value2 = sheet.cell_value(4,0)
	print(value1,value2)

	#获取单元格内容的数据类型
	#ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
	value_type = sheet.cell(1,0).ctype
	print(value_type)

#设置表格样式
def set_style(name,height,bold=False):
	#初始化样式
	style = xlwt.XFStyle()

	#为样式创建字体
	font = xlwt.Font()
	font.name = name
	font.bold = bold
	font.color_index = 4
	font.height = height

	borders = xlwt.Borders()
	borders.left = 6
	borders.right = 6
	borders.top = 6
	borders.bottom = 6

	style.font = font
	style.borders = borders

	return style

#表格的写入
def write_excel(path):
	#创建工作簿
	f = xlwt.Workbook()

	#创建sheet
	sheet = f.add_sheet('sheet1',cell_overwrite_ok=True)
	row0 = ['1','2','3']
	col0 = ['one','two','three']

	for i in range(len(row0)):
		sheet.write(0,i,row0[i],set_style('Times New Roman',220,True))

	for i in range(0,len(col0)):
		sheet.write(i+1,0,col0[i])

	#保存文件
	f.save(path)


#向已经有数据的excel添加数据

#思路：
# 1：打开已经存在的.xls文件
# 2：copy一份已经存在.xls的文件
# 3：向文件中写入数据
# 4：删除之前的文件
# 5：保存一份相同的文件
from xlutils.copy import copy

def write_exist_excel(old_path,new_path):
	#打开excel
	rb = xlrd.open_workbook(old_path)

	#复制excel
	wb = copy(rb)
	sheet = wb.get_sheet(0)
	sheet.write(1,3,'old')
	os.remove(old_path)
	wb.save(new_path)




if __name__ == '__main__':
	# path = '/Users/alpha/ys/读excel表的数据/data.xlsx'
	# read_excel(path)

	#存.xlsx文件时，mac会出问题，存xls无问题
	path = '/Users/alpha/test.xls'
	write_excel(path)
