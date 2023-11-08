# 本程序中涉及数组的正常使用 0 下标位，输出时请下标 + 1，下同。
# 开数组时请正常开，输出时加一。
import random

import numpy

num = int(input("请输入参与人数："))

student = [i + 1 for i in range(num)]  # student——记学生序列
gift = [i + 1 for i in range(num)]  # gift——记礼物序列
selfGift = 0  # 抽签时统计是否存在自己分配给自己的事件数

print(student)
print(gift)

randNum = input("请输入打乱次数(如不输则在 1-10000 随机取数)：")

if randNum == "":
    randNum = random.randint(1, 10000)
    for i in range(int(randNum)):
        numpy.random.shuffle(gift)
    for i in range(int(randNum)):
        numpy.random.shuffle(student)
else:
    for i in range(int(randNum)):
        numpy.random.shuffle(gift)
    for i in range(int(randNum)):
        numpy.random.shuffle(student)

# print("随机打乱后的交换对象:")
# print(student)
# print(gift)

for person in range(num):

    if str(student[person]) == str(gift[person]):
        selfGift = selfGift + 1
        print("在数组下标第 " + str(person) + " 处发生意外的自主分配: 学生 " + str(student[person]) + " 取走了 " + str(gift[person]) + " 的礼物。")
print("发生自己分配给自己的事件数: " + str(selfGift))

print("以下是交换礼品结果~")
for person in range(num):
    print(str(person) + ": 请 " + str(student[person]) + " 号同学领取 " + str(gift[person]) + " 号礼品~")
