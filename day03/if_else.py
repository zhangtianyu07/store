#分析成绩是否合格

score = int(input("请输入你的成绩："))


if score >= 90 and score < 100:
    print("优秀！！！")
elif score >= 80 and score < 90:
    print("良好！！！")
elif score >= 70 and score < 80:
    print("一般！！！")
elif score >= 60 and score < 70:
    print("合格！！！")
elif score >= 0 and score < 60:
    print("不合格！！！")
else:
    print("不存在！！！")