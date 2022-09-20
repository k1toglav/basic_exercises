# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = {}

for student in students:
    if student['first_name'] not in names:
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names_students = {}

for names in students:
    names_students[names['first_name']] = names_students.get(names['first_name'], 0) + 1

print('Самое частое имя среди учеников:' , max(names_students, key=names_students.get))


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],
    [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

class_names = {}
for i in range(len(school_students)):
    for students in school_students[i]:
        class_names[students['first_name']] = class_names.get(students['first_name'], 0) + 1
    print('Самое частое имя среди учеников', i+1, 'класса:', max(class_names, key=class_names.get))
    class_names.clear()


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for student in school: 
	men=0
	women=0
	for i in student['students']: 
		if is_male.get(i['first_name']) == False: 
			women += 1
		if is_male.get(i['first_name']) == True: 
			men += 1
	print(f"{women} девочек и {men} мальчиков")
	   
	



# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

my_list = []

for class_ in school:
    men = 0
    women = 0
    for students in class_:
        if is_male.get(class_['students']) == False:
            women += 1
        else:
            men += 1
    my_list.append(dict(class_name = class_['class'], men = men, women = women))
print(my_list)

if my_list[0]['men'] > my_list[1]['men']:
    print(my_list[0]['class_name'], 'больше мальчиков')
    print(my_list[1]['class_name'], 'больше девочек')
else:
    print(my_list[0]['class_name'], 'больше девочек')
    print(my_list[1]['class_name'], 'больше мальчиков')