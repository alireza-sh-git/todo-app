import todo_functions
import PySimpleGUI as sg
import time
import os


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")


todos = todo_functions.get_todos()


popupFont = ("Calibri", 20)
clock = sg.Text("", key="clock")
label = sg.Text("Please enter a todo: ")
inputBox = sg.InputText(tooltip="Enter todo", key="todo")
addButton = sg.Button("Add")
editButton = sg.Button("Edit")
deleteButton = sg.Button("Delete")
saveButton = sg.Button("Save")
exitButton = sg.Button("Exit")
listBox = sg.Listbox(todos, size=(40, 10), key="todos",
                     enable_events=True)
window = sg.Window("My To-Do App",
                   layout=[[clock], [label], [inputBox, addButton],
                           [listBox, editButton, deleteButton],
                           [saveButton, exitButton]],
                   font=("Helvetica", 20))


while True:
    event, values = window.read(timeout=200)
    clock.update(time.strftime("%d %b, %Y    %H:%M:%S"))
    match event:

        case "Add":
            todo = values["todo"].strip()
            if todo == "":
                sg.popup("Please enter a todo", font=popupFont)
                continue
            todo_functions.add_todo(todos, todo)
            listBox.update(todos)
            inputBox.update("")

        case "Edit":
            todo = values["todo"].strip()
            if todo == "":
                sg.popup("Please enter a todo.", font=popupFont)
                continue
            try:
                editTodo = todos.index(values["todos"][0])
                todo_functions.edit_todo(todos, editTodo, todo)
                listBox.update(todos)
                inputBox.update("")
            except IndexError:
                sg.popup("Please select a todo.", font=popupFont)

        case "todos":
            inputBox.update(values["todos"][0])

        case "Delete":
            try:
                todo = todos.index(values["todos"][0])
                todo_functions.delete_todo(todos, todo)
                listBox.update(todos)
                inputBox.update("")
            except IndexError:
                sg.popup("Please select a todo.", font=popupFont)

        case "Save":
            todo_functions.save_todos(todos)

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()
