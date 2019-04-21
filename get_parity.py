num = input('Введите целое число: ')
num = int(num)

def if_even(x):
    parity = ((x % 2) == 0)
    if parity == True:
        print('Число чётное')
    else:
        print('Число нечётное')

print(if_even(num))  

