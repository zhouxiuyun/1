def factorization(n):
    for i in range(2,n):
        if n%i==0:
        # 当n%i=0时表示i为n的一个因子
            global count
            count=count+1
            # 输出n的一种分解式，用于验证
            print("{}*{}={} count={}".format(i,n//i,n,count))
            # 继续分解n的一个因子i
            factorization(i)
# 从文件中读出数据
file_readpath = 'input.txt'
with open(file_readpath) as file:
    txt = file.read()
n = eval(txt)

# 初始化count=1，代表n=n*1的情况
count = 1
factorization(n)
# 输出结果用于验证
print("{}共有{}种不同的分解式".format(n, count))

#将结果存入文件output.txt
file_writepath = 'output.txt'
file = open(file_writepath, "w")
file.write(str(count))
file.close()
