#输入两个数，求这两个数的最大公约数25 99
print("请输入两个数")
a = int(input())
b = int(input())
m = min(a, b)
while a%m !=0  or b%m !=0:
	m -= 1

print(m)
