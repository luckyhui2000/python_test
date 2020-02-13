#判断一个数（自然数）是否为质数100
'''
tnum = 2
num = int(input("请输入一个自然数"))
if num == 1:
	print("1不是一个质数")
else:
	while (num % tnum != 0) and tnum < num:
		tnum += 1
	if tnum == num:
		print(num, "是一个质数")
	else:
		print(num, "不是一个质数")
'''
num = int(input("请输入一个数"))
if num == 1:
	print("1不是一个质数")
n = 2
while n < num:
	if num % n == 0:
		print(num, "不是一个质数")
	n += 1
if num == n:
	print(num, "是一个质数")
