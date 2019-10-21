# Задача программы - вывести фигуру из заданных символов
print('Помните, что введенные значения сторон должны состоять из равного количества символов')
print('Какую фигуру вы хотите нарисовать?')
print('Если вы хотите квадрат - введите 1')
print('Если вы хотите квадрат с диагоналями - введите 2')
print('Если вы хотите диагонали квадрата без обводки - введите 3')
print('Если вы хотите закрашенный квадрат - введите 4')
print('Если вы хотите закрашенный квадрат с диагоналями - введите 5')
print('Если вы хотите прямоугольник - введите 6')
print('Если вы хотите прямоугольник с диагоналями - введите 7')
print('Если вы хотите диагонали прямоугольника без обводки - введите 8')
print('Если вы хотите закрашенный прямоугольник - введите 9')
print('Если вы хотите закрашенный прямоугольник с диагоналями - введите 10')
ans = int(input())

while ans > 10 or ans < 1:
    print('Ошибка: введите верный ответ')
    ans = int(input())

if ans == 1:
    print('Какого размера будет фигура?')
    side = int(input())
    print('Из каких символов она будет состоять?')
    symbol = str(input())
    for i in range(side):
        for j in range(side):
            if i == 0 or i == side - 1:
                print(' ', symbol, ' ', end='', sep='')
            elif j == 0 or j == side - 1:
                print(' ', symbol, ' ', end='', sep='')
            else:
                print('   ', end='')
        print()

elif ans == 3:
    print('Какого размера будет сторона квадарата для этих диагоналей?')
    side = int(input())
    print('Из каких символов они будут состоять?')
    symbol = str(input())
    for i in range(side):
        for j in range(side):
            if i == j or i == side - 1 - j:
                print(' ', symbol, ' ', end='', sep='')
            else:
                print('   ', end='')
        print()

elif ans == 2:
    print('Какого размера будет фигура?')
    side = int(input())
    print('Из каких символов она будет состоять?')
    symbol = str(input())
    print('Из каких символов будут состоять диагонали?')
    symbol_diag = str(input())
    for i in range(side):
        for j in range(side):
            if i == 0 or i == side - 1:
                print(' ', symbol, ' ', end='', sep='')
            elif j == 0 or j == side - 1:
                print(' ', symbol, ' ', end='', sep='')
            elif i == j or i == side - 1 - j:
                print(' ', symbol_diag, ' ', end='', sep='')
            else:
                print('   ', end='')
        print()

elif ans == 4:
    print('Какого размера будет фигура?')
    side = int(input())
    print('Из каких символов она будет состоять?')
    symbol = str(input())
    print('Из каких символов состоит закраска?')
    symbol_paint = str(input())
    for i in range(side):
        for j in range(side):
            if i == 0 or i == side - 1:
                print(' ', symbol, ' ', end='', sep='')
            elif j == 0 or j == side - 1:
                print(' ', symbol, ' ', end='', sep='')
            else:
                print(' ', symbol_paint, ' ', end='', sep='')
        print()

elif ans == 5:
    print('Какого размера будет фигура?')
    side = int(input())
    print('Из каких символов она будет состоять?')
    symbol = str(input())
    print('Из каких символов будут состоять диагонали?')
    symbol_diag = str(input())
    print('Из каких символов будет состоять закраска?')
    symbol_paint = str(input())
    for i in range(side):
        for j in range(side):
            if i == 0 or i == side - 1:
                print(' ', symbol, ' ', end='', sep='')
            elif j == 0 or j == side - 1:
                print(' ', symbol, ' ', end='', sep='')
            elif i == j or i == side - 1 - j:
                print(' ', symbol_diag, ' ', end='', sep='')
            else:
                print(' ', symbol_paint, ' ', end='', sep='')
        print()

elif ans == 6:
    print('Какого размера будет фигура?')
    side = int(input())
    print('Из каких символов будет состоять ее короткая сторона?')
    symbol_short = str(input())
    print('Из каких символов будет состоять ее длинная сторона?')
    symbol_long = str(input())
    for i in range(side):
        for j in range(side):
            if i == 0 or i == side - 1:
                print(symbol_short, ' ', end='', sep='')
            elif j == 0 or j == side - 1:
                print(symbol_long, ' ', end='', sep='')
            else:
                print('  ', end='')
        print()

elif ans == 8:
    print('Какого размера будет сторона прямоугольника для этих диагоналей?')
    side = int(input())
    print('Из каких символов они будут состоять?')
    symbol = str(input())
    for i in range(side):
        for j in range(side):
            if i == j or i == side - 1 - j:
                print(symbol, ' ', end='', sep='')
            else:
                print('  ', end='')
        print()

elif ans == 7:
    print('Какого размера будет фигура?')
    side = int(input())
    print('Из каких символов будет состоять ее короткая сторона?')
    symbol_short = str(input())
    print('Из каких символов будет состоять ее длинная сторона?')
    symbol_long = str(input())
    print('Из каких символов будут состоять диагонали?')
    symbol_diag = str(input())
    for i in range(side):
        for j in range(side):
            if i == 0 or i == side - 1:
                print(symbol_short, ' ', end='', sep='')
            elif j == 0 or j == side - 1:
                print(symbol_long, ' ', end='', sep='')
            elif i == j or i == side - 1 - j:
                print(symbol_diag, ' ', end='', sep='')
            else:
                print('  ', end='')
        print()

elif ans == 9:
    print('Какого размера будет фигура?')
    side = int(input())
    print('Из каких символов будет состоять ее короткая сторона?')
    symbol_short = str(input())
    print('Из каких символов будет состоять ее длинная сторона?')
    symbol_long = str(input())
    print('Из каких символов состоит закраска?')
    symbol_paint = str(input())
    for i in range(side):
        for j in range(side):
            if i == 0 or i == side - 1:
                print(symbol_short, ' ', end='', sep='')
            elif j == 0 or j == side - 1:
                print(symbol_long, ' ', end='', sep='')
            else:
                print(symbol_paint, ' ', end='', sep='')
        print()

elif ans == 10:
    print('Какого размера будет фигура?')
    side = int(input())
    print('Из каких символов будет состоять ее короткая сторона?')
    symbol_short = str(input())
    print('Из каких символов будет состоять ее длинная сторона?')
    symbol_long = str(input())
    print('Из каких символов будут состоять диагонали?')
    symbol_diag = str(input())
    print('Из каких символов будет состоять закраска?')
    symbol_paint = str(input())
    for i in range(side):
        for j in range(side):
            if i == 0 or i == side - 1:
                print(symbol_short, ' ', end='', sep='')
            elif j == 0 or j == side - 1:
                print(symbol_long, ' ', end='', sep='')
            elif i == j or i == side - 1 - j:
                print(symbol_diag, ' ', end='', sep='')
            else:
                print(symbol_paint, ' ', end='', sep='')
        print()