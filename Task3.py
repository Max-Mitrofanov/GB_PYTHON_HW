# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

print('Enter three numbers: ')

a = int(input())
b = int(input())
c = int(input())

def my_func (a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    print(my_list[0] + my_list[1])

my_func(a, b, c)