#!/usr/bin/python
#BMI 测量工具
the_weight=float(input("体重："))
the_height=float(input("身高："))
print("正在计算中。。。")
the_BMI = the_weight / (the_height/100)**2
print("你的BMI指数：",the_BMI)
if the_BMI <=18.5:
    print("偏瘦")
    if the_BMI <=18.5:
        # 打开网页
        import webbrowser
    webbrowser.open("https://baidu.com/")
elif the_BMI<=24.9:
    print("正常")
elif the_BMI<=29.9:
    print("超重")
elif the_BMI>29.9:
    print("肥胖")
    if the_BMI <=29.9:
        # 打开网页
        import webbrowser
    webbrowser.open("https://keep.com/")
import os
os.system("pause")




