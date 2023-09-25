FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Returns a list of todos stored in a file.
     """
    with open(filepath, "r") as file:
        newtodo = file.readlines()
    newtodo = [item.strip() for item in newtodo]
    return newtodo


def add_todo(todo_list, todo):
    todo_list.append(todo.strip())
    return todo_list


def save_todos(newtodo, filepath=FILEPATH):
    for item in newtodo:
        newtodo[newtodo.index(item)] = item + '\n'
    with open(filepath, "w") as file:
        file.writelines(newtodo)


def delete_todo(todo_list, todo_number):
    todo_list.pop(todo_number)
    return todo_list


def edit_todo(todo_list, todo_number, todo):
    todo_list[todo_number] = todo
    return todo_list
