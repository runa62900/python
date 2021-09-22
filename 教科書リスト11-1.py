class Menber:
    pass

yamada = Menber()
yamada.no = 15
yamada.name = '山田太郎'
yamada.weight = 72.7

sekine = Menber()
sekine.no = 37
sekine.name = '関根信彦'
sekine.weight = 65.3

print('{}:{}{}kg'.format(yamada.no,yamada.name,yamada.weight))
print('{}:{}{}kg'.format(sekine.no,sekine.name,sekine.weight))
