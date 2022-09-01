#1. Напишите функцию, которая будет принимать номер кредитной карты и
#показывать только последние 4 цифры. Остальные цифры должны заменяться
#звездочками
def kartochka(card):
    return '*' * len(card[:-4]) + card[-4:]

print(kartochka('1626575781724356'))

#2. Напишите функцию, которая проверяет: является ли слово палиндромом
def palindrome(str):
    str = str.replace(' ', '').lower()
    return 'Палиндром' if str == str[::-1] else 'Не палиндром'

print(palindrome('lllfhhhdhhf'))
print(palindrome('vnnvnvnnvnv'))
print(palindrome('12233221'))

