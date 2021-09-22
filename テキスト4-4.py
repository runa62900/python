print('1からnまでの和を求めます。')

while True:
    n= int(input('nの値 :'))
    if n > 0:
        break

    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
        print('１から',n,'までの和は',sum,'です。')
