# 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: # 加上 -sig:可把\ufeff去掉
		for line in f:
			lines.append(line.strip())
	return lines

# 轉換格式
def convert(lines):
	new = []
	person = None # 無，表示有宣告變數，但是沒有值
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: # 如果person有值，避免第一行不是人名crash
		 	new.append(person + ': ' + line)
	return new

# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()				