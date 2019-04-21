film = input('Доступные фильмы:\n"Пятница", "Чемпионы" и "Пернатая банда".\nВыберите фильм: ')
date = input('Доступные даты: сегодня, завтра\nВыберите дату: ')
if film == 'Пятница':
    print('Доступные сеансы: в 12, 16 и 20 часов.')
elif film == 'Чемпионы':
    print('Доступные сеансы: в 10, 13 и 16 часов.')
elif film == 'Пернатая банда':
    print('Доступные сеансы: в 10, 14 и 18 часов.')
time = input('Выберите время сеанса: ')
time = int(time)
num = input('Выберите число билетов: ')
num = int(num)
print('Выбрали фильм:',film,'\nДень:',date,'\nВремя:',time,'\nКоличество билетов:',num)

if film == 'Пятница':
    if date == 'завтра':
        if time == 12:
            if num >= 20:
                cost = 250*0.8*0.95*num
            else:
                cost = 250*0.95*num
        elif time == 16:
            if num >= 20:
                cost = 350*0.8*0.95*num
            else:
                cost = 350*0.95*num
        elif time == 20:
            if num >= 20:
                cost = 450*0.8*0.95*num
            else:
                cost = 450*0.95*num
    elif date == 'сегодня':
        if time == 12:
            if num >= 20:
                cost = 250*0.8*num
            else:
                cost = 250*num
        elif time == 16:
            if num >= 20:
                cost = 350*0.8*num
            else:
                cost = 350*num
        elif time == 20:
            if num >= 20:
                cost = 450*0.8*num
            else:
                cost = 450*num
elif film == 'Чемпионы':
    if date == 'завтра':
        if time == 10:
            if num >= 20:
                cost = 250*0.8*0.95*num
            else:
                cost = 250*0.95*num
        elif time == 13:
            if num >= 20:
                cost = 350*0.8*0.95*num
            else:
                cost = 350*0.95*num
        elif time == 16:
            if num >= 20:
                cost = 350*0.8*0.95*num
            else:
                cost = 350*0.95*num
    elif date == 'сегодня':
        if time == 10:
            if num >= 20:
                cost = 250*0.8*num
            else:
                cost = 250*num
        elif time == 13:
            if num >= 20:
                cost = 350*0.8*num
            else:
                cost = 350*num
        elif time == 16:
            if num >= 20:
                cost = 350*0.8*num
            else:
                cost = 350*num
elif film == 'Пернатая банда':
    if date == 'завтра':
        if time == 10:
            if num >= 20:
                cost = 350*0.8*0.95*num
            else:
                cost = 350*0.95*num
        elif time == 14:
            if num >= 20:
                cost = 450*0.8*0.95*num
            else:
                cost = 450*0.95*num
        elif time == 18:
            if num >= 20:
                cost = 450*0.8*0.95*num
            else:
                cost = 450*0.95*num
    elif date == 'сегодня':
        if time == 10:
            if num >= 20:
                cost = 350*0.8*num
            else:
                cost = 350*num
        elif time == 14:
            if num >= 20:
                cost = 450*0.8*num
            else:
                cost = 450*num
        elif time == 18:
            if num >= 20:
                cost = 450*0.8*num
            else:
                cost = 450*num

print('Результат:',cost,'руб.')
