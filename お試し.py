#foo = 'hello'
#print(type(foo))

#foo = 10.55
#print(foo, type(foo))
#foo = round(foo)
#print(foo,type(foo))

foo = 10
#fooを1ビット右シフト
foo = foo << 1
#2進数に変換
foo = bin(foo)
#fooを画面表示
print(foo)