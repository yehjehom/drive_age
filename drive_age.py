driving = input('請問有沒有開過車？')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit #離開系統


age = input('請輸入年齡？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('恭喜你通過測驗')
	else:
		print('奇怪！你怎麼可以開車')
elif driving == '沒有':
    if age >= 18:
    	print('你可以報考駕照')
    else:
    	print('滿18歲就可以報考駕照囉！')
