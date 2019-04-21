num = input('Введите атомарный номер элемента: ')
atomNumber = int(num)
if atomNumber == 80:
    print('Ртуть (Hg)')
elif atomNumber == 3:
    print('Литий (Li)')
elif atomNumber == 25:
    print('Марганец (Mn)')
elif atomNumber == 17:
    print('Хлор (Cl)')
else:
    print('Извините, в моей базе данных нет элемента с таким номером.')
