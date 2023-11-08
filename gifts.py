# 本程序中涉及数组的正常使用 0 下标位，输出时请下标 + 1，下同。
# 开数组时请正常开，输出时加一。

import numpy

num = int(input("请输入参与人数："))
student = [i + 1 for i in range(num)]  # student——记学生序列
sumPerson = num  # sumPerson——记总人数

isMultiGift = input("是否存在一个学生多个礼物的情况？(y/N)")
if isMultiGift == "y":
    multiGiftLen = int(input("输入多个礼物的学生人数:"))
    multiGiftList = numpy.zeros((multiGiftLen, 2))  # 初始化值为 0 的二维数组——记多礼物学生人数和礼物个数
    print("接下来请输入学生号和礼物数，以逗号分隔。\n例如，1 号同学有 3 个礼物，请输入 1,3 。\n")
    for person in range(multiGiftLen):
        src = input("输入第 " + str(person + 1) + " 位同学的编号和礼物数：")
        stu = src.split(",", 1)
        print(stu)
        multiGiftList[person][0] = stu[0]
        multiGiftList[person][1] = stu[1]
    print(multiGiftList)
    print("存在多个礼物的同学如下:\n" + numpy.lexsort(multiGiftList[0, None]) + "")
else:
    print(student)
    numpy.random.shuffle(student)
    print("随机打乱后的交换对象:")
    print(student)

    # print(gift)
