#足し算の関数
def 足し算(num1, num2):
    return num1 + num2

# 引き算の関数  
def 引き算(num1, num2):
    return num1 - num2

# 掛け算の関数
def 掛け算(num1, num2):
    return num1 * num2

# 割り算の関数
def 割り算(num1, num2):
    return num1 / num2

#計算番号表示
print("計算したい種類の番号を半角で入力してください -\n" \
        "1. 足し算\n" \
        "2. 引き算\n" \
        "3. 掛け算\n" \
        "4. 割り算\n")


# ユーザーに入力
select = input("この中から計算したい番号を選んでください！ 1, 2, 3, 4 :")

number_1 = int(input("計算したい最初の数字を入力してください: "))
number_2 = int(input("2回目の数字を入力してください: "))

if select == '1':
    print(number_1, "+", number_2, "=",
                    足し算(number_1, number_2))

elif select == '2':
    print(number_1, "-", number_2, "=",
                    引き算(number_1, number_2))

elif select == '3':
    print(number_1, "*", number_2, "=",
                    掛け算(number_1, number_2))

elif select == '4':
    print(number_1, "/", number_2, "=",
                    割り算(number_1, number_2))
else:
    print("この結果は表示できません")