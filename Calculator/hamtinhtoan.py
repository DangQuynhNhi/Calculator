def cong(a,b):
    return a+b

def tru(a,b):
    return a-b

def nhan(a,b):
    return a*b

def chia(a,b):
    if b == 0:
        print("Số chia không thể bằng 0")
    else:
        return a/b

def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def shh(n):
    if n < 2:
        return False
    total = 1

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i

def giai_thua(n):
    if n < 0:
        return "Không có giai thừa của số âm"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    if n < 0:
        return "Vui lòng nhập số không âm"
    a, b = 0, 1
    for i in range(3,n):
        a, b = b, b+i
    return a

def tong_uoc(n):
    s = 1
    for i in range(2,n**0.5):
        if n % i == 0:
            s = s + i +(n//i)
    return s

def phan_tich_thua_snt(n):
    if n < 2:
        return
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

