def create_list():
    return []


def add_task(tasks, title):
    tasks.append({"title": title, "done": False})


def get_tasks(tasks):
    return tasks.copy()


def count_tasks(tasks):
    return len(tasks)


def finish_task(tasks, index):
    tasks[index]["done"] = True


def delete_task(tasks, index):
    tasks.pop(index)


def get_task(tasks, index):
    return tasks[index]


def rename_task(tasks, index, title):
    tasks[index]["title"] = title


def reopen_task(tasks, index):
    tasks[index]["done"] = False
