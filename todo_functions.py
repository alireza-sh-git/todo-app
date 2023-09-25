import time


FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Returns a list of todos stored in a file.
     """
    print("Loading previous todo list...")
    with open(filepath, "r") as file:
        newtodo = file.readlines()
    newtodo = [item.strip() for item in newtodo]
    time.sleep(2)
    print("Todo list loaded")
    return newtodo


def add_todo(todo_list, todo):
    user_input = todo[4:]
    if todo == "":
        user_input = input("Please enter a new todo: ").strip()
        if user_input in todo_list:
            print("Already exists")
        else:
            todo_list.append(user_input.strip())
            print(f"{user_input} added to list.")
    else:
        todo_list.append(user_input.strip())
        print(f"{user_input} added to list.")
    return todo_list

if __name__ == "__main__":
    print("hello")


def show_todos(todo_list):
    print("Your current todo list is as follows: ")
    for index, item in enumerate(todo_list):
        print((str(index+1) + "_ " + item).strip())


def save_todos(newtodo, filepath=FILEPATH):
    print("Saving...")
    for item in newtodo:
        newtodo[newtodo.index(item)] = item + '\n'
    with open(filepath, "w") as file:
        file.writelines(newtodo)
    time.sleep(2)
    print("Saved Successfully")


def delete_todo(todo_list, todoNumber):
    todoNumber = todoNumber[7:]
    if todoNumber == "":
        todoNumber = input("Please enter the number of the todo you want to delete: ")
    try:
        user_input = int(todoNumber)-1
    except ValueError:
        print("invalid input")
        return todo_list
    try:
        removedTodo = todo_list[user_input]
        todo_list.pop(user_input)
        print(f"'{removedTodo}' was removed from the list.")
    except IndexError:
        print("Invalid Input")
    return todo_list


def edit_todo(todo_list, todoNumber):
    todoNumber = todoNumber[5:]
    if todoNumber == "":
        todoNumber = input("Please enter the number of the todo you want to delete: ")
    try:
        todo_index = int(todoNumber) - 1
        editedTodo = todo_list[todo_index]
        newtodo = input("What do you want to edit it into? ")
        todo_list[todo_index] = newtodo
        print(f"'{editedTodo}' was changed to {newtodo}.")
    except ValueError:
        print("invalid input")
    return todo_list
