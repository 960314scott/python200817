# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:58:33 2020

@author: user
"""

score = int(input("請輸入成績"))
if score >= 0 and score <= 100:
    if score == 100:
        print("你是不是作弊")
    if score >= 90:
        print("恭喜你承認了你智商不低")
        print("你是levelA")
    else:
        if score >=80:
            print("你在標準之上")
            print("你是levelB")
        elif score >=70:
            print("你好棒嗎")
            print("你是levelC")
        else:
            if score >= 60:
                print("你低空飛過")
                print("你是levelD")
            else:
                print("你好爛")
                print("你是levelE")
            
            
else:
    print("笨蛋看鍵盤很難嗎?")    
    print("請重新輸入")