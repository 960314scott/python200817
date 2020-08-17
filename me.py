# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:38:31 2020

@author: user
"""

math = int(input("請輸入數學成績"))
english = int(input("請輸入英文成績"))
if (math >=0 and math <=100) and (english >=0 and english<=100):
        if math <60 or english <60:
            if math >60:
                print("請加油，強化你的英文")
            elif english >60:
                print("請加油，強化你的數學")
            else:
                print("哭阿，你有處罰")
        if math >=90 and english >=90:
                print("你有獎品，你好棒!")
        elif math >=60 and english >=60:
                print("可憐阿，你沒有獎品")
else:
    print("笨蛋請看數字，請重新輸入")
