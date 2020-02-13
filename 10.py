#判断一个数是否为水仙花数（Narcissistic number）
#水仙花数：它的每个位上的数字的 3次幂之和等于它本身
#输出所有的水仙花数
num = int(input("请输入一个三位数："))

tnum = num % 10
snum = num // 10 % 10
fnum = num // 100

if tnum**3 + snum**3 + fnum**3 == num:
	print(num, "是一个水仙花数")
else:
	print(num, "不是一个水仙花数")
	

num = 100
while num <= 999:
	tnum = num % 10
	snum = num // 10 % 10
	fnum = num // 100	
	if tnum**3 + snum**3 + fnum**3 == num:
		print(num, "是一个水仙花数")
	num += 1
	
