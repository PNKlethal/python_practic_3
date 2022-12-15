def my_func_2(x, y):
    counter = 1
    result = 1 / x
    while counter < abs(y):
        result = result * (1 / x)
        counter += 1
    return result

print(f'Возведения степени вариантом 2: '
      f'{my_func_2(int(input("Основание степени Х: ")), int(input("Показатель степени Y: ")))}')
