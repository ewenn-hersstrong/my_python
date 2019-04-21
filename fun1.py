num = input('Введите вещественное число: ')
num = float(num)

def fun1(x):
    if -2.4 <= x <= 5.7:
        print('f = ',pow(x,2))
    else:
        print('f = ', 4)

print(fun1(num))  

