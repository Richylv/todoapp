import functions
import time

now = time.strftime("%b %d, %Y, %H:%M:%S")
print('It is', now)
while True:

    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] +'\n' # example user_action: 'add play games' extract content starting from index 4 'play games'
        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif 'show' in user_action:
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')  # .strip('/n') remmove the caracter from the list
            print(f"{index + 1}-{item}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input('Enter new to do: ')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print('Your command is not valid')
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f'To Do {todo_to_remove} was removed from the list'
            print(message)
        except IndexError:
            print('There is no item with that number')
            continue
    elif 'exit' in user_action:
        break
    else:
        print('Command not valid')

print('BYE')
