# BMI = 體重（公斤）/身高**2（公尺平方） 　
#過重：24≦BMI＜27
#輕度肥胖：27≦BMI＜30
#中度肥胖：30≦BMI＜35
#重度肥胖：BMI≧35
#18.5≦BMI＜24
#BMI ＜ 18.5 過輕
print('您好，歡迎面對自己的BMI數值')
height = input('請輸入您的身高(公尺)')
weight = input('請輸入您的體重(公斤)')
BMI = float(weight) / (float(height) ** 2)
print(BMI)
if BMI < 18.5:
	print('您已經過輕了，真的太瘦了！')
elif BMI >= 18.5 and BMI < 24:
	print('您的BMI正常喔！')
elif BMI <= 24 and BMI < 27:
	print('小心一點唷，您已經過重了！')
elif BMI <= 27 and BMI < 30:
	print('您的BMI指數已達輕度肥胖，請小心注意飲食。')
elif BMI <= 30 and BMI < 35:
	print('您的BMI指數已達中度肥胖，請詢專業醫師調整飲食。')
else:
	print('您的BMI指數已達重度肥胖，請儘速就醫！')