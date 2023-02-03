import functions
import PySimpleGUI as psg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

psg.theme("DarkTeal10")
clock = psg.Text('', key="clock", font=("Helvetica", 8))
label = psg.Text("Type in a to-do")
input_box = psg.InputText(tooltip="Enter to-do", key="todo")
add_button = psg.Button("Add", tooltip="Add to-do", key="Add")
list_box = psg.Listbox(values=functions.get_todos(),
                       key='todos', enable_events=True,
                       size=[40, 10])
edit_button = psg.Button("Edit")
complete_button = psg.Button("Complete",
                             tooltip="Complete", key="Complete")

window = psg.PySimpleGUI.Window("To-Do App",
                                layout=[[clock],
                                        [label],
                                        [input_box, add_button],
                                        [list_box, edit_button, complete_button]],
                                font=("Helvetica", 15))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case psg.WINDOW_CLOSED:
            break
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Edit":
            try:
                todo_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                psg.popup("Please select an item first", font =("Helvetica", 15))
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "todos":
            window['todo'].update(value=values['todos'][0])


window.close()


