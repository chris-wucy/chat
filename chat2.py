# 對話格式 -> 13:32 Allen 請問分公司代號是 9432 嗎
# 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: # 加上 -sig:可把\ufeff去掉
		for line in f:
			lines.append(line.strip())
	return lines

# 計算字數
def convert(lines):
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_word_count = 0
	viki_word_count = 0
	allen_image_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ') # 切割
		time = s[0]
		name = s[1]
		words = s[2:]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			else:
				for m in words:
					if '圖片' in words:
						allen_image_count += 1
						continue
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			else:
				for m in words:
					if '圖片' in words:
						viki_image_count += 1
						continue
					viki_word_count += len(m)
		#print(words)			
	print('Allen說了', allen_word_count, '個字')
	print('傳了', allen_sticker_count, '個貼圖')
	print('傳了', allen_image_count, '個圖片')

	print('Viki說了', viki_word_count, '個字')
	print('傳了', viki_sticker_count, '個貼圖')
	print('傳了', viki_image_count, '個圖片')
	#return 

# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('[LINE]Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

main()				