'''
•Cho p là số nguyên tố, khi đó:
    • Nếu a là số nguyên dương và GCD(a, p) = 1, thì: 
    a^(p-1) (mod p) = 1
    • Nếu a là số nguyên dương bất kỳ thì:
    a^p (mod p) = a (mod p)

'''

# Đề bài: Tính b = 𝒂^m (mod n) theo fermat
import ThuatToan_Euclid_Tim_GCD as TT_GCD

def nhapSoNguyen(mes):
    while True:
        a = input(mes)
        try:
            a = int(a)
            return a
        except ValueError:
            print("Bạn phải nhập số nguyên")

def nhapSoNguyenDuong(mes):
    while True:
        a = input(mes)
        try:
            a = int(a)
            if a>0: return a
            print("Bạn phải nhập số nguyên dương")
        except ValueError:
            print("Bạn phải nhập số nguyên")
    A,B = 0,0   # khai bao bien
    # Đưa về A>=B
    if a>=b: A,B = a,b 
    else: A,B = b,a
    while True:
        if B==0: return A 
        r = A%B 
        A,B = B, r

def Fermat(a, m, n):
    # Nếu a<0 chuyển a thành số đồng dư với a
    while a<0:
        a = a+n
    if a==0:
        return 0
    #a^p (mod p) = a (mod p)
    if m==n:
        return a%n
    if TT_GCD.ThuatToan_Euclid_Tim_GCD.GCD(a, n)==1 and m>n:
        m = m%(n-1)
    result = (a**m)%n
    return result

if __name__=="__main__":
    #Input
    a = nhapSoNguyen("Nhap so nguyen a: ")
    m = nhapSoNguyenDuong("Nhap so nguyen duong m: ")
    n = nhapSoNguyenDuong("Nhap so nguyen duong n: ")
    print("b = 𝒂^m (mod n)=" + str(Fermat(a, m, n)) )
