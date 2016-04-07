# -*- coding:utf-8 -*-
#   python3.4.4
#   目录下所有txt文件两两求交集

import os
import glob


#获取目标目录下文件名列表
filelist = glob.glob("C:\\poj\\target\\*.txt")
#如果目录下文件少于2个，结束程序
if len(filelist) < 2:
    print('少于2个文件')
    exit()
#获取目录下文件数量
fnum = len(filelist)
#创建包含文件内容的二维数组
file = [[] for i in range(fnum)]

#获取文件名列表及文件内容二维数组
for i in range(fnum):
    f = open(filelist[i])
    s = f.read()
    filecont= s.split()
    file[i] = filecont
f.close()
#循环进行两两求交集
for i in range(fnum):
    for j in range(i+1,fnum):
        jiaoji = set(file[i])&set(file[j])
        f1 = open("target.txt",'a+')
        f1.writelines("\nIntersection of %s and %s : "%(filelist[i],filelist[j]))
        for d in jiaoji:            #遍历字典，每个元素之间加空格
            f1.writelines(" %s "%d)
print('done!')
f1.close()
