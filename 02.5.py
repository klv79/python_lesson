my_list = [7, 5, 3, 3, 2]
number = int(input('Введите число '))
print('Исходный список', my_list)
my_list.append(number)
print('Список с новым числом', my_list)
my_list1 = sorted(my_list, reverse=True)
print('Список отсортированный по убыванию', my_list1)