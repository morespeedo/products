import os 

products = []
if os.path.isfile('products.csv'):
	print('yeah!找到檔案了!')
	with open('products.csv' ,'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到檔案.......')

#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	products.append([name, price])
print(products)

#確認消費紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#添加新消費
with open('products.csv', 'w') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')