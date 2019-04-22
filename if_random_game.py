import random
ai = random.randint(1,4)
user = input('Введите число от 1 до 4: ')
user = int(user)
if ai == user:
    print('Ты угадал!')
elif user > ai:
    print('Твоё число больше. Попробуй ещё раз.')
else:
    print('Твоё число меньше. Попробуй ещё раз.')
