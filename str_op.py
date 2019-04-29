s = 'У лукоморья 123 дуб зеленый 456'
if s.find('я') != -1:
    print('1) Индекс буквы "Я" в строке = ', s.find('я'))
print('2) В строке буква "У" встречается',s.count('у'),'раз.')
if not s.isalpha():
    print('3)',s.upper())
print(f'4) Длина строки "{s}" - {len(s)} символов')
if len(s) > 4:
    print(s.lower())
print('5) О'+s[1:])
