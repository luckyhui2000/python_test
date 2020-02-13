#从五个数中返回第二大的值
print("请输入五个值")
n1 = 0 
list1 = []
while n1 < 5:
	list1.append(int(input()))
	n1 +=1

print(list1)

fmax = list1[0]
smax = list1[0]

n2 = 1

while n2 < len(list1):
	if list1[n2] > fmax:
		smax = fmax
		fmax = list1[n2]
	if smax < list1[n2] <fmax:
		smax = list1[n2]
	n2 +=1

print("第二大的值smax=", smax)
	
