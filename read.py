data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: #每1000筆印一次
			print(len(data))

print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
	print(sum_len)

print('留言的平均長度為', sum_len/len(data))


new = []
for d in data: #d 是字串 / data 是100萬筆留言
	if len(d) < 100: #如果字串長度小於100
		new.append(d) #就把這個d字串, 裝到new這個清單
print('一共有', len(new), '筆留言長度小於100')
print(new[0]) #印出清單的第1筆資料


