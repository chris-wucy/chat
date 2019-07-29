# 對話格式 -> 13:32Allen 請問分公司代號是 9432 嗎
lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())
for line in lines:
	s = line.split(' ')
	# s[0] = 13:32Allen
	# 前5個代表時間，固定格式
	#        01234 
	# s是清單，可以用清單分割，s[0]是字串，在Python裡字串可當成清單看待！
	# 寫成 s[0][:5] = 13:32
	time = s[0][:5] 
	name = s[0][5:]
	msg = s[1:]
	print(time)
	print(name)
	print(msg)