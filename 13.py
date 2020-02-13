#打印一个字符串中所有数字字符的和  12dsf15asd12  12
strl = str(input("请输入一个字符串"))
n = 0
Sum = 0
while n < len(strl): 
	if strl[n] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
		Sum += int(strl[n])
	n += 1
print(Sum)
