# coding: utf-8
#Copyright (c) 2020. LSHT LLC.
#Published on Github.
#https://GitHub.com/LUMOGROUP/lumogroup.github.io/tree/master/python/
#求平均数 ver 0.2

def pause(message="Press any key to continue..."):
    pause_pause = input(message)

#`import sys
digits = []
i = 0
print("求平均数\n帮助：逐个输入数字，输入完成请输入q")
while True:
    i = i + 1
    userin = input("输入第"
                   + str(i)
                   + "个数字>>")
    if userin == "q":
        break
    else:
        userin = int(userin)
        digits.append(userin)
num = len(digits)
all = sum(digits)
print("数字数量=" + str(num) + "\n总和=" + str(all))
out = all / num
out = str(out)
print("平均数是 " + out + " .")
pause("按 Enter 退出")
