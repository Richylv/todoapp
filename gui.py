import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todo.txt','w') as file:
        pass

sg.theme('DarkPurple4')
labelDate = sg.Text('',key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter To do',key='todo')
add_btn = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True,size=[45,10])
edit_btn = sg.Button('Edit')
complete_btn = sg.Button('Complete')
exit_btn = sg.Button('Exit')

window = sg.Window('My to-do app',
                   layout=[[labelDate],
                           [label],
                           [input_box,add_btn],
                           [list_box,edit_btn, complete_btn],
                           [exit_btn]],
                   font=('Helvetica',14))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y, %H:%M:%S"))
    #print(event)
    #print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Select an item first')
        case 'Complete':
            try:
                todo_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Select an item first')
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case sg.WINDOW_CLOSED:
            break

window.close()
