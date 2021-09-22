#じゃんけんゲーム
import random

print('じゃんけんゲーム')

#勝敗の結果
kati_no = make_no= hikiwake_no = 0

#じゃんけん結果の繰り返し関数
while True:
    comp = random.randint(0,2)
    while True:
        men = int(input('じゃんけん(0:グー/1:チョキ/2:パー):'))
        if 0 <=men <=2:
            break

    print('私は',end='')
    if comp == 0:
        print('グー',end='')
    elif comp == 1:
        print('チョキ', end='')
    else:
        print('パー', end='')
    print('です')

    
    #勝敗結果
    result = (men - comp + 3) % 3
    if result ==0:
        print('引き分け')
        hikiwake_no += 1
    elif result ==1:
        print('負け')
        make_no +=1
    else:
        print('勝ち')
        kati_no +=1

    retry = int(input('もう一回(0:はい/1:いいえ):'))
    if retry == 1:
        break

    #結果表示
    print('結果:',kati_no, '勝ち',make_no,'負け',hikiwake_no,'引き分け' )





    