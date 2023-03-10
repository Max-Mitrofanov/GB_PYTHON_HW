# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def user_sum ():
    sum_total = 0
    stop = False
    while stop == False:
        user_number = input('Введите числа через пробел или S для выхода: ').split()
        result = 0
        for el in range(len(user_number)):
            if user_number[el] == 's' or user_number[el] == 'S':
                stop = True
                break
            else:
                result = result + int(user_number[el])
        sum_total = sum_total + result
        print(f'Текущая сумма {sum_total}')
    print(f'Общая сумма {sum_total}')


user_sum()