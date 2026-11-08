from todo import create_list, add_task, delete_task, finish_task

tasks = create_list()

while True:
    print("\n=== Список задач ===")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Выполнить задачу")
    print("4. Удалить задачу")
    print("0. Выход")

    choice = input("Выбор: ")

    if choice == "1":
        title = input("Название: ")
        add_task(tasks, title)
        print("Задача добавлена")

    elif choice == "2":
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "-"
            print(f"{i + 1}. [{status}] {task['title']}")

    elif choice == "3":
        try:
            index = int(input("Номер задачи: ")) - 1
            if not 0 <= index < len(tasks):
                raise IndexError
            finish_task(tasks, index)
            print("Задача выполнена")
        except (ValueError, IndexError):
            print("Неверный номер")

    elif choice == "4":
        try:
            index = int(input("Номер задачи: ")) - 1
            if not 0 <= index < len(tasks):
                raise IndexError
            delete_task(tasks, index)
            print("Задача удалена")
        except (ValueError, IndexError):
            print("Неверный номер")

    elif choice == "0":
        break

    else:
        print("Неизвестная команда")
EOFcat > main.py <<'EOF'
from todo import create_list, add_task, delete_task, finish_task

tasks = create_list()

while True:
    print("\n=== Список задач ===")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Выполнить задачу")
    print("4. Удалить задачу")
    print("0. Выход")

    choice = input("Выбор: ")

    if choice == "1":
        title = input("Название: ")
        add_task(tasks, title)
        print("Задача добавлена")

    elif choice == "2":
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "-"
            print(f"{i + 1}. [{status}] {task['title']}")

    elif choice == "3":
        try:
            index = int(input("Номер задачи: ")) - 1
            if not 0 <= index < len(tasks):
                raise IndexError
            finish_task(tasks, index)
            print("Задача выполнена")
        except (ValueError, IndexError):
            print("Неверный номер")

    elif choice == "4":
        try:
            index = int(input("Номер задачи: ")) - 1
            if not 0 <= index < len(tasks):
                raise IndexError
            delete_task(tasks, index)
            print("Задача удалена")
        except (ValueError, IndexError):
            print("Неверный номер")

    elif choice == "0":
        break

    else:
        print("Неизвестная команда")
EOFcat > main.py <<'EOF'
from todo import create_list, add_task, delete_task, finish_task

tasks = create_list()

while True:
    print("\n=== Список задач ===")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Выполнить задачу")
    print("4. Удалить задачу")
    print("0. Выход")

    choice = input("Выбор: ")

    if choice == "1":
        title = input("Название: ")
        add_task(tasks, title)
        print("Задача добавлена")

    elif choice == "2":
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "-"
            print(f"{i + 1}. [{status}] {task['title']}")

    elif choice == "3":
        try:
            index = int(input("Номер задачи: ")) - 1
            if not 0 <= index < len(tasks):
                raise IndexError
            finish_task(tasks, index)
            print("Задача выполнена")
        except (ValueError, IndexError):
            print("Неверный номер")

    elif choice == "4":
        try:
            index = int(input("Номер задачи: ")) - 1
            if not 0 <= index < len(tasks):
                raise IndexError
            delete_task(tasks, index)
            print("Задача удалена")
        except (ValueError, IndexError):
            print("Неверный номер")

    elif choice == "0":
        break

    else:
        print("Неизвестная команда")
EOFcat > main.py <<'EOF'
from todo import create_list, add_task, delete_task, finish_task

tasks = create_list()

while True:
    print("\n=== Список задач ===")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Выполнить задачу")
    print("4. Удалить задачу")
    print("0. Выход")

    choice = input("Выбор: ")

    if choice == "1":
        title = input("Название: ")
        add_task(tasks, title)
        print("Задача добавлена")

    elif choice == "2":
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "-"
            print(f"{i + 1}. [{status}] {task['title']}")

    elif choice == "3":
        try:
            index = int(input("Номер задачи: ")) - 1
            if not 0 <= index < len(tasks):
                raise IndexError
            finish_task(tasks, index)
            print("Задача выполнена")
        except (ValueError, IndexError):
            print("Неверный номер")

    elif choice == "4":
        try:
            index = int(input("Номер задачи: ")) - 1
            if not 0 <= index < len(tasks):
                raise IndexError
            delete_task(tasks, index)
            print("Задача удалена")
        except (ValueError, IndexError):
            print("Неверный номер")

    elif choice == "0":
        break

    else:
        print("Неизвестная команда")
EOFcat > main.py <<'EOF'
from todo import create_list, add_task, delete_task, finish_task

tasks = create_list()

while True:
    print("\n=== Список задач ===")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Выполнить задачу")
    print("4. Удалить задачу")
    print("0. Выход")

    choice = input("Выбор: ")

    if choice == "1":
        title = input("Название: ")
        add_task(tasks, title)
        print("Задача добавлена")

    elif choice == "2":
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "-"
            print(f"{i + 1}. [{status}] {task['title']}")

    elif choice == "3":
        try:
            index = int(input("Номер задачи: ")) - 1
            if not 0 <= index < len(tasks):
                raise IndexError
            finish_task(tasks, index)
            print("Задача выполнена")
        except (ValueError, IndexError):
            print("Неверный номер")

    elif choice == "4":
        try:
            index = int(input("Номер задачи: ")) - 1
            if not 0 <= index < len(tasks):
                raise IndexError
            delete_task(tasks, index)
            print("Задача удалена")
        except (ValueError, IndexError):
            print("Неверный номер")

    elif choice == "0":
        break

    else:
        print("Неизвестная команда")
