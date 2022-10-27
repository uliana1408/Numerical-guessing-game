from random import *

def is_valid(text):
    if text.isdigit() and 1 <= int(text) <= 100:
        return True
    else:
        return False

number = randrange(1, 101)
print('Добро пожаловать в числовую угадайку')

while True:
    num = input('Попробуйте угадать число от 1 до 100 ... ')
    if is_valid(num):
        num = int(num)
        if num < number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        if num > number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        if num == number:
            print('Вы угадали, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break

    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
