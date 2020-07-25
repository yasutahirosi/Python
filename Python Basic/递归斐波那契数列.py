#递归实现斐波那契数列
fib_list=[]
for i in range(500):
    if i<=2:
        fib_list.append(1)
    else:
        fib_list.append(fib_list[-1]+fib_list[-2])
print(fib_list)