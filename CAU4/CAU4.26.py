print("sinh viên: TRAN VAN TRUNG")
print("MSV:245752021610133")
T= 0
ds=[]
print('nhap giao dịch,kt bang dong trong :')
for dong in iter(input,''):
    ds.append(dong)
for d in ds:
    lenh,tien=d.split()
    tien=int(tien)
    if lenh =='D':
        T +=tien
    elif lenh =='W':
        T -= tien
print('so tien con lai',T)
