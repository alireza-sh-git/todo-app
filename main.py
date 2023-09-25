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
        todos = add_todo(todos, userAction)
    elif userAction.startswith("show"):
        show_todos(todos)
    elif userAction.startswith("delete"):
        todos = delete_todo(todos, userAction)
    elif userAction.startswith("edit"):
        edit_todo(todos, userAction)
    elif userAction.startswith("save"):
        save_todos(todos)
    elif userAction.startswith("exit"):
        break
    else:
        print("invalid Input")

print("Bye!")
