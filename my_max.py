num1 = input('Введите первое число: ')
num1 = float(num1)

num2 = input('Введите второе число: ')
num2 = float(num2)

def my_max (x, y):
    res = x - y
    if res >= 0:
        return('Наибольшее из введенных чисел: ', x)
    else:
        return('Наибольшее из введенных чисел: ', y)

print(my_max(num1, num2))


