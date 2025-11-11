print("sinh viên: TRAN VAN TRUNG")
print("MSV:245752021610133")
s=input('nhap cac so,Cách nhau dau phay : ')
so=s.split(',')
le=[]
for x in so:
    if int(x)%2 != 0:
        le.append(x)
print(','.join(le))
