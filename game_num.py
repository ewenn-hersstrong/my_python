from random import randint
ai = randint(0,10)
print('Компьютер загадал число.\nУ вас есть 3 попытки. Удачи!')
counter = 3
while counter > 0:
    user = input('Попробуйте угадать:')
    if user.lower() == 'выход':
        print('Выход из программы.')
        break
    elif int(user) == ai:
        print('Победа!')
        break
    elif int(user) < ai:
        print('Попробуйте число больше!')
        counter -= 1
    else:
        print('Попробуйте число меньше!')
        counter -= 1
if counter == 0:
    print(f'Game over!\nЧисло: {ai}')
    
