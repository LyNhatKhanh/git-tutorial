import math

def ktra_hop_le(a,b,c):
    if a == 0 or b == 0 or c == 0:
        return 1
    elif a+b < c or a+c < b or b+c < a:
        return 1
    else:   return 2



def cac_phep_tinh_TG(a,b,c):
    cv = (a+b+c)
    p = cv/2
    dt = '{0:.{1}f}'.format(math.sqrt(p*(p-a)*(p-b)*(p-c)),2)
    print("Chu vi:",cv)
    print("p:",p)
    print("Dien tich:",dt)

a=int(input("Nhap canh a: "))
b=int(input("Nhap canh b: "))
c=int(input("Nhap canh c: "))

if (ktra_hop_le(a,b,c) == 1):
    print("Tam giac khong hop le.")
else:
    print("Tam giac hop le.")
    cac_phep_tinh_TG(a,b,c)

print('Hello')