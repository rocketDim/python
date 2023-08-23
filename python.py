import random

HELP = '''
help - напечатать справку о программе.
add - добавить задачу в список (название задачи запрашивается у пользователя).
show - напечатать все добавленные задачи.'''

RANDOM_TASKS = ['Записаться к барберу', 'Сходить на прогулку', 'Закупиться продуктами', 'Сходить на концерт', 'Записаться в бассейн']

tasks = {

}

# Сегодня, Завтра, 31.12...
# [Задача1, Задача2, Задача3]....
# Дата -> [Задача1, Задача2, Задача3]

def add_todo(date, task):
    if date in tasks:
            # Дата есть в словаре
            # Добавляем в список задачу
        tasks[date].append(task)
    else:
            # Даты в словаре нет
            # Создаем запись в ключе
        tasks[date] = []
        tasks[date].append(task)
    print('Задача ', task, 'добавлена на дату', date)

while True:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'add':
        date = input('Введите дату: ')
        task = input('Введите название: ')
        add_todo(date, task)
    elif command == 'show':
        date = input('Введите дату: ')
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print('Такой даты нет')
    elif command == 'random':
        task = random.choice(RANDOM_TASKS)
        add_todo('Сегодня', task)
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная команда')
        break

print('До свидания!')
