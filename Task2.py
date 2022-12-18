# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
# фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

print('Enter your first name: ')
first_name = input()

print('Enter your last name: ')
last_name = input()

print('Enter your birth date: ')
birth_date = input()

print('Enter your city: ')
user_city = input()

print('Enter your email: ')
user_email = input()

print('Enter your phone: ')
user_phone = input()

def user_string (name, lastname, date, city, email, phone):
    print(f'Mr(Mrs) {name} {lastname} was born in {date} and lives in {city}. {name} {lastname}\'s email is {email} and phone is {phone} .')


user_string(phone = user_phone, email = user_email, city = user_city, date = birth_date, lastname = last_name, name = first_name)

