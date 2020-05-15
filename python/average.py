# coding: utf-8
#Copyright (c) 2020. LSHT LLC.
#Published on Github. https://github.com/LUMOGROUP/lumogroup.github.io/python/
#求平均数

def pause(message="Press any key to continue..."):
    pause_pause = input(message)

#`import sys
digits = []
print("求平均数\n帮助：逐个输入数字，输入完成请输入q")
while True:
    userin = input("输入数字>>")
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
