print("sinh viên: TRAN VAN TRUNG")
print("MSV:245752021610133")
n=int(input('nhap n'))
for i in range(1, n):
    tong=0
    for j in range(1,i):
        if i%j ==0:
            tong +=j
    if tong > i:
        print(i)

