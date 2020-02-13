#输入一个字符串；判断有多个单词  i am a good man 
str1 = str(input("请输入一个字符串："))
n = 0
Sum = 0
while n <= len(str1) - 1:
	if str1[n] != " ":
		Sum += 1
		n += 1
		while n <= len(str1) - 1 and (str1[n] != " "):
			n += 1
	n += 1
print(Sum)
