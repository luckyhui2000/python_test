#输入一个时间返回加一秒后的时间 12:13:55
time = str(input(""))
ls = time.split(":")

h = int(ls[0])
m = int(ls[1])
s = int(ls[2])

s += 1
if s == 60:
	s =0
	m += 1
	if m == 60:
		m = 0
		h += 1
		if h == 24:
			h == 0
#格式化输出，2：保证输出两位数
print("%.2d:%.2d:%.2d" %(h, m, s))
