#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
name = input('введите имя: ')
surname = input('введите фамилию: ')
year = str(input('введите год рождения: '))
city = input('введите город проживания: ')
email = input('введите почту: ')
telephone = input('введите номер телефона ')


def my_func(name, surname, year, city, email, telephone):
    return ','.join([name, surname, year, city, email, telephone])


print(my_func(name, surname, year, city, email, telephone))
