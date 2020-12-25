data = []
count = 0
with open('reviews1.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 
		if count % 1000 == 0: # %是用来求余数
			print(len(data))
print(len(data))

#print(data)
print(data[0])
print('--------')
print(data[1])