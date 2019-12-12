import pandas as pd
import numpy as np
import cv2
from scipy.stats import pearsonr
import heapq
import matplotlib.pyplot as plt


# 使用matplotlib展示多张图片
def matplotlib_multi_pic1():
    # 先在第一行显示原图
    img = cv2.imread('D:/file/image.vary.jpg/%s.jpg'%i)
    title = "%s.jpg"%i
    plt.subplot(3, 3, 2)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # 因为OpenCV和matplotlib中的颜色通道顺序不一样
    plt.imshow(img)
    plt.title(title, fontsize=8)
    plt.xticks([]) # 去除坐标
    plt.yticks([])
    # 再显示与之最相近的五张图片
    j=3
    for k in max_pearson_index_list:
        img = cv2.imread('D:/file/image.vary.jpg/%s.jpg'%k)
        title="%s.jpg"%k
        # 行，列，索引
        j=j+1
        plt.subplot(3,3,j)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.title(title,fontsize=8)
        plt.xticks([])
        plt.yticks([])
    plt.show()


def matplotlib_multi_pic2():
    # 先在第一行显示原图
    img = cv2.imread('D:/file/image.vary.jpg/%s.jpg'%i)
    title = "%s.jpg"%i
    plt.subplot(11, 10, 5)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # 因为OpenCV和matplotlib中的颜色通道顺序不一样
    plt.imshow(img)
    plt.title(title, fontsize=8)
    plt.xticks([]) # 去除坐标
    plt.yticks([])
    # 再显示与之最相近的100张图片
    j=10
    for k in max_pearson_index_list:
        img = cv2.imread('D:/file/image.vary.jpg/%s.jpg'%k)
        title="%s.jpg"%k
        # 行，列，索引
        j=j+1
        plt.subplot(11,10,j)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.title(title,fontsize=8)
        plt.xticks([])
        plt.yticks([])
    plt.show()


i = input("请输入要比对的图片序号：")

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

test = pd.read_excel('example32.xls',header=None)
# 对输入的图片与所有图片进行比较,将皮尔逊系数存在数组中
pearson_max = []
for j in range(0,9908):
    print(j)
    strDb = test.loc[[j + 1], [1]]
    strDb = np.array(strDb)
    strDb = strDb.tolist()
    a = strDb[0][0]
    arrDb = a.split(',')  # 字符串转char型数组
    histDb = list(map(float, arrDb))  # char型数组转float型
    pearson_max.append(pearsonr(arr, histDb)[0])

max_pearson_index_list = map(pearson_max.index, heapq.nlargest(5, pearson_max))
max_pearson_index_list=list(max_pearson_index_list) # map()生成的不是list，直接print不出来
print(max_pearson_index_list)
print("与输入图片最相近的5张图片为：")  # 9804、2426、1604、4982
for j in range(0,5):
    x = max_pearson_index_list[j]
    print("%s.jpg" %x)
    print(pearson_max[x])
matplotlib_multi_pic1()

max_pearson_index_list = map(pearson_max.index, heapq.nlargest(100, pearson_max))
max_pearson_index_list=list(max_pearson_index_list)
print(max_pearson_index_list)
print("与输入图片%s.jpg最相近的100张图片为：" %i)  # 1793、6959
for j in range(0,100):
    x = max_pearson_index_list[j]
    print("%s.jpg" %x)
    print(pearson_max[x])
matplotlib_multi_pic2()