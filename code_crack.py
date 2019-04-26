import random
code = str(random.randint(1000,9999))
while True:
    crack = input('Попробуйте угадать 4хзначный код')
    if crack == code:
        print('Ты угадал! Замок открыт')
        break
    else:
        for i in range(len(code)):
            if crack[i] == code[i]:
                print('*', end = '')
            elif crack[i] > code[i]:
                print('-', end = '')
            else:
                print('+', end = '')
