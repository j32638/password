password ='123456'
i = 3
while True:#回圈
	paw = input('請輸入密碼')
	if paw == password:
		print('登入成功')
		break#跳出
	else:
		i = i - 1
		print('輸入錯誤還有', i ,'次機會')
	if i == 0:
		break