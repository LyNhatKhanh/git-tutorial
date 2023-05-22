def dien_tich_HT(r):
    return '{0:.{1}f}'.format(r*3.14*r,2)

def chu_vi_HT(r):
    return '{0:.{1}f}'.format(2*3.14*r,2)

r=int(input("Nhap ban kinh: "))
print("Chu vi hinh tron: " + chu_vi_HT(r)) 
print("Dien tich hinh tron: " + dien_tich_HT(r)) 

print("Hello")