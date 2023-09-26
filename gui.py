import todo_functions
import PySimpleGUI as sg


todos = todo_functions.get_todos()

label = sg.Text("Please enter a todo: ")
inputBox = sg.InputText(tooltip="Enter todo", key="todo")
addButton = sg.Button("Add")
editButton = sg.Button("Edit")
deleteButton = sg.Button("Delete")
saveButton = sg.Button("Save")
exitButton = sg.Button("Exit")
listBox = sg.Listbox(todos, size=(40, 10), key="todos")
window = sg.Window("My To-Do App",
                   layout=[[label], [inputBox, addButton],
                           [listBox, editButton, deleteButton],
                           [saveButton, exitButton]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todo = values["todo"].strip()
            if todo == "":
                print("Please enter a todo")
            else:
                todo_functions.add_todo(todos, todo)
                listBox.update(todos)
        case "Edit":
            break
        case "Delete":
            break
        case "Save":
            todo_functions.save_todos(todos)
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
