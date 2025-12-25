son = int(input("Son kiriting: "))

if son == 0:
    print(0)
else:
    teskari = 0
    while son > 0:
        digit = son % 10
        teskari = teskari * 10 + digit
        son //= 10
    print(teskari)
