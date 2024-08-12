class Task:
    # Принимаем имя задачи, ее описание и статус выполнения, пол умолчанию false
    def __init__(self, name, description, status=False):
        self.name = name
        self.description = description
        self.status = status

    # Выводим на экран имя задачи и сделано/не сделано в зависимости от статуса выполнения
    def display(self):
        if self.status:
            print(f'{self.name} (Сделана)')
        else:
            print(f'{self.name} (Не сделана)')


class TaskList:
    # Создаем пустой список для будущих задач
    def __init__(self):
        self.tasks = list()

    # Добавляем задачу в конец списка
    def add_task(self, task):
        self.tasks.append(task)

    # удаляем задачи с конца списка
    def remove_task(self, rtask):
        self.tasks.remove(rtask)


class TaskManager:
    # Сохраняем ЭК из класса TaskList в атрибут task_list
    def __init__(self, task_list):
        self.task_list = task_list

    def mark_done(self, task):
        self.task = task
        self.task.status = True
        return self.task.status

    def mark_undone(self, task):
        self.task = task
        self.task.status = False
        return self.task.status
    def show_tasks(self):
        for task in self.task_list.tasks:
            task.display()

# # Ниже код для проверки классов Task, TaskList и TaskManager

# Создаем список задач
todo = TaskList()
assert todo.tasks == []

# Создаем несколько задач и добавляем их в список
task1 = Task("Стирка", "Постирать трусы, носки, слюнявчики")
assert task1.name == 'Стирка'
assert task1.description == 'Постирать трусы, носки, слюнявчики'
assert task1.status is False
task1.display()

todo.add_task(task1)
assert len(todo.tasks) == 1

task2 = Task("Продукты", "Купить лук чеснок огурцы хлеб и биток")
assert task2.name == 'Продукты'
assert task2.description == 'Купить лук чеснок огурцы хлеб и биток'
assert task2.status is False

todo.add_task(task2)
assert len(todo.tasks) == 2

# Создаем менеджер задач и показываем список задач
manager = TaskManager(todo)
assert isinstance(manager.task_list, TaskList)
print('-----Список дел-----')
manager.show_tasks()

# Отмечаем первую задачу выполненной и показываем список задач
manager.mark_done(task1)

# Проверяем изменился ли статус 2мя способами
assert task1.status is True
assert manager.task_list.tasks[0].status is True

print('-----Список дел-----')
manager.show_tasks()

# Удаляем вторую задачу и показываем список задач
todo.remove_task(task2)

assert len(todo.tasks) == 1
assert len(manager.task_list.tasks) == 1

print('-----Список дел-----')
manager.show_tasks()
