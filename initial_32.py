# coding=UTF-8
import cv2
import pandas as pd
from pandas import DataFrame

number=9908  #图片总数量
# 建立信息表
data = pd.read_excel("example32.xls", sheet_name='Sheet1')

for i in range(0,number): # 因为从0开始，同时range右值不取
     img = cv2.imread('D:/file/image.vary.jpg/%s.jpg'%i)
     histB = cv2.calcHist([img], [0], None, [32], [0.0, 255.0])
     histG = cv2.calcHist([img], [1], None, [32], [0.0, 255.0])
     histR = cv2.calcHist([img], [2], None, [32], [0.0, 255.0])

     arr = [0 for x in range(0,96)]
     for j in range(0,32):
         arr[j]=histB[j][0]
     for j in range(32,64):
         arr[j]=histG[j-32][0]
     for j in range(64,96):
         arr[j]=histR[j-64][0]

     strRGB = ','.join(str(m) for m in arr)
     value = [["%s.jpg"%i, strRGB],]

     data.loc[i+1] = ["%s.jpg"%i, strRGB]
     print(i)
DataFrame(data).to_excel('example32.xls', sheet_name='Sheet1', index=False, header=True)

# 建立模板表（模板法不适用于该方法，无需此部分）
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
