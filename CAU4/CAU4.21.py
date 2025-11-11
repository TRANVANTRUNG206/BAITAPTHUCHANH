print("sinh viên: TRAN VAN TRUNG")
print("MSV:245752021610133")
s = input("Nhập chuỗi số nhị phân 4 chữ số, cách nhau bởi dấu phẩy: ")
lst = s.split(",")
kq=[]
for x in lst:
    so=int(x,2)
    if so % 5 == 0:
        kq.append(x)
print(",".join(kq))



