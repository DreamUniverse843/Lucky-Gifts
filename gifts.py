# 本程序中涉及数组的正常使用 0 下标位，输出时请下标 + 1，下同。
# 开数组时请正常开，输出时加一。
import random
import numpy
import tkinter
from tkinter import filedialog
import pandas

print("请在接下来弹出的窗口中选择学生名册 Excel 文件。\n")
nameList = []
nameInputPath = tkinter.filedialog.askopenfilename()
# print("给定的表格输入文件为: " + nameInputPath)
for person in pandas.read_excel(io=nameInputPath, usecols=["姓名"]).values.tolist():
    nameList.append(person[0])
# print("成功转换为 List:" + str(nameList))
num = len(nameList)
student = [i + 1 for i in range(num)]  # student——记学生序列
gift = [i + 1 for i in range(num)]  # gift——记礼物序列
selfGift = 0  # 抽签时统计是否存在自己分配给自己的事件数

randNum = input("请输入打乱次数(如不输则在 1-10000 随机取数)：")
if randNum == "":
    randNum = random.randint(1, 10000)
    print("已随机取次数为 " + str(randNum))
    print("正在抽取......")
    for i in range(int(randNum)):
        numpy.random.shuffle(gift)
    for i in range(int(randNum)):
        numpy.random.shuffle(student)
else:
    print("已指定取次数为 " + str(randNum))
    print("正在抽取......")
    for i in range(int(randNum)):
        numpy.random.shuffle(gift)
    for i in range(int(randNum)):
        numpy.random.shuffle(student)

print("正在抽取......如果长时间卡在此提示，可能是频繁出现自己给自己发礼物的情况，请耐心等候！\n")
# 检测到有同学自己给自己发礼物就重新抽，直到没有为止
isRepeated = 1
while isRepeated != 0:
    isRepeated = 0
    for person in range(num):
        if str(student[person]) == str(gift[person]):
            isRepeated = 1
            numpy.random.shuffle(gift)
            numpy.random.shuffle(student)

print("以下是交换礼品结果~")
print("学生人数: " + str(num))
print("学生名单: " + str(nameList))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for person in range(num):
    print("请 " + str(nameList[student[person] - 1]) + " 同学领取 " + str(nameList[gift[person] - 1]) + " 的礼品~")
