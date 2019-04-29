s = input('Введите строку:')
n = int(input('Введите число:'))
def func(string, num):
    if len(string) > num:
        return(string.upper())
    else:
        return(string)
print(func(s,n))
