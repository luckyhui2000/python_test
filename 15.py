#分解质因数    200 2 2 2 5 5  
num = int(input("请输入一个数"))
i = 2
while num != 1:
	if num % i == 0:
		print(i)
		num //= i
	else:
		i += 1

n = 0
while n <= 10000000000000000000000000000:
	print(n)	
	n += 1 




