import todo_functions
import PySimpleGUI as sg


label = sg.Text("Please enter a todo: ")
inputBox = sg.InputText(tooltip="Enter todo")
addButton = sg.Button("Add")
window = sg.Window("My To-Do App", layout=[[label], [inputBox, addButton]])
window.read()
print("Hello")
window.close()
