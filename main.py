from todo_functions import *
import time


now = time.strftime("%d %b, %Y   %H:%M:%S")
print("It is", now)
filepath = "todos.txt"
todos = get_todos()

while True:
    userAction = input("Please enter what you want to do: Add, Show, Delete, Edit, Save or exit: ")
    userAction = userAction.casefold().strip()

    if userAction.startswith("add") or userAction.startswith("new"):
        todo = userAction[4:]
        if todo == "":
            todo = input("Please enter a new todo: ").strip()
            if todo in todos:
                print("Already exists")
                continue
        todos = add_todo(todos, todo)
        print(f"{todo} added to list.")

    elif userAction.startswith("show"):
        print("Your current todo list is as follows: ")
        for index, item in enumerate(todos):
            print((str(index + 1) + "_ " + item).strip())

    elif userAction.startswith("delete"):
        todoNumber = userAction[7:]
        if todoNumber == "":
            todoNumber = input("Please enter the number of the todo you want to delete: ")
        try:
            todoNumber = int(todoNumber) - 1
            removedTodo = todos[todoNumber]
            todos = delete_todo(todos, todoNumber)
        except IndexError:
            print("Invalid Input")

    elif userAction.startswith("edit"):
        todoNumber = userAction[5:]
        if todoNumber == "":
            todoNumber = input("Please enter the number of the todo you want to delete: ")
        try:
            todoNumber = int(todoNumber) - 1
            editedTodo = todos[todoNumber]
            todo = input("What do you want to edit it into? ")
            edit_todo(todos, todoNumber, todo)
            print(f"'{editedTodo}' was changed to {todo}.")
        except IndexError:
            print("Invalid Input")

    elif userAction.startswith("save"):
        print("Saving...")
        save_todos(todos)
        time.sleep(2)
        print("Saved Successfully")

    elif userAction.startswith("exit"):
        break
    else:
        print("invalid Input")

print("Bye!")
