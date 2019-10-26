import xlrd
import xlwt
from xlutils.copy import copy
import cv2
from scipy.stats import pearsonr
import heapq
book_name_xls = 'img颜色直方库RGB_v2.0.xls'
sheet_name_xls = '颜色直方RGB'
value_title = [["name", "BGR"], ]

def read_excel_xls(path,row,col):
     workbook = xlrd.open_workbook(path)  # 打开工作簿
     sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
     worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
     temp=worksheet.cell_value(row,col)
     return temp

i = input("请输入要比对的图片序号：")

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

#对输入的图片与所有图片进行比较,将皮尔逊系数存在数组中
pearson_max = []
for j in range(0,9908):
    print(j)
    strDb = read_excel_xls(book_name_xls, j+1, 1)#读取字符串
    arrDb = strDb.split(',')  # 字符串转char型数组
    histDb = list(map(float, arrDb))  # char型数组转float型
    #print(pearsonr(arr,histDb)[0])
    pearson_max.append(pearsonr(arr,histDb)[0])

max_pearson_index_list = map(pearson_max.index, heapq.nlargest(5, pearson_max))
max_pearson_index_list=list(max_pearson_index_list) #map()生成的不是list，直接print不出来
print(max_pearson_index_list)
print("与输入图片最相近的5张图片为：")
for i in range(0,5):
    x = max_pearson_index_list[i]
    print("%s.jpg" %x)
    print(pearson_max[x])

# max_pearson_index_list = map(pearson_max.index, heapq.nlargest(100, pearson_max))
# max_pearson_index_list=list(max_pearson_index_list)
# print(max_pearson_index_list)
# print("与输入图片%s.jpg最相近的100张图片为：" %i)
# for i in range(0,100):
#     x = max_pearson_index_list[i]
#     print("%s.jpg" %x)
#     #print(pearson_max[x])