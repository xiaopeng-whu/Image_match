# coding=UTF-8
import xlrd
import xlwt
from xlutils.copy import copy
import cv2
from scipy.stats import pearsonr

def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")

def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    # print("xls格式表格【追加】写入数据成功！")


def read_excel_xls(path, row, col):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    temp = worksheet.cell_value(row, col)
    return temp

book_name_xls = 'img颜色直方库RGB_v2.0.xls'
sheet_name_xls = '颜色直方RGB'
value_title = [["name", "BGR"], ]
write_excel_xls(book_name_xls, sheet_name_xls, value_title)
# book_name_xls1 = 'template.xls'
# sheet_name_xls1 = 'average'
# value_title1 = [["No.","average"],]
# write_excel_xls(book_name_xls1, sheet_name_xls1, value_title1)
number=9908; #图片总数量
#建立信息表
for i in range(0,number): #因为从0开始，同时range右值不取
     img = cv2.imread('D:/file/image.vary.jpg/%s.jpg'%i)
     histB = cv2.calcHist([img], [0], None, [4], [0.0, 255.0])
     histG = cv2.calcHist([img], [1], None, [4], [0.0, 255.0])
     histR = cv2.calcHist([img], [2], None, [4], [0.0, 255.0])

     arr = [0 for x in range(0,12)]
     for j in range(0,4):
         arr[j]=histB[j][0]
     for j in range(4,8):
         arr[j]=histG[j-4][0]
     for j in range(8,12):
         arr[j]=histR[j-8][0]

     strRGB = ','.join(str(m) for m in arr)
     value = [["%s.jpg"%i, strRGB],]

     write_excel_xls_append(book_name_xls, value)
     print(i)

#建立模板表（模板法不适用于该方法，无需此部分）
# for i in range(0,number//100+1):
#     average_hist=[0 for x in range(0, 12)]
#     if ((i>=0)&(i<number//100)):
#         for j in range(100*i,100*(i+1)):
#             strDb = read_excel_xls(book_name_xls, j+1, 1)  # 读取字符串
#             arrDb = strDb.split(',')  # 字符串转char型数组
#             print(arrDb)
#             histDb = list(map(float, arrDb))  # char型数组转float型
#             #average_hist = average_hist+histDb   wrong!!
#             average_hist = [average_hist[i]+histDb[i] for i in range(0,12)]
#         #average_hist=average_hist/100
#         average_hist=[x / 100 for x in average_hist]
#     else:
#         for j in range(100*i,number):
#             strDb = read_excel_xls(book_name_xls, j+1, 1)  # 读取字符串
#             arrDb = strDb.split(',')  # 字符串转char型数组
#             histDb = list(map(float, arrDb))  # char型数组转float型
#             #average_hist = average_hist + histDb  wrong!!
#             average_hist = [average_hist[i]+histDb[i] for i in range(0,12)]
#         #average_hist = average_hist / (number-100*(i-1))  wrong!!
#         average_hist = [x / (number-100*(i-1)) for x in average_hist]
#     average_hist = ','.join(str(m) for m in average_hist)
#     value = [["第%s组"%i, average_hist],]
#     print(value)
#     write_excel_xls_append(book_name_xls1, value)
#     print(i)
