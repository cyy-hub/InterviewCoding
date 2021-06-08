import sys

# 按行读入， 会读取末尾'\n' 读入数据为字符串类型
# 加.strip()，去掉回车符，同时去掉前后的空格
# 加.split() 以括号里的符号将字符串分割为列表
#line = sys.stdin.readline().strip() 

# 1.读入单行一个数 
#n=int(sys.stdin.readline().strip())

# 2.读入单行多个数字
line=sys.stdin.readline().strip().split(" ")
n,m = int(line[0]), int(line[1])

# 读入数组
arr = []
for i in range(n):
    line = sys.stdin.readline().strip()
    value = list(map(int, line.split(" ")))   # 转换成迭代器，再转换成List
    arr.append(value)
print(n,m)
print(arr)