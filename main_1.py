#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль
def div(*args):

    try:
        arg1 = float(input("Введите делимое: "))
        arg2 = float(input("Введите делитель: "))
        result = arg1 / arg2
    except ValueError:
        return 'Ошибка значения'
    except ZeroDivisionError:
        return ": На ноль делить нельзя!"

    return result

print(f'result  {div()}')
