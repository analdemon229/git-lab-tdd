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
