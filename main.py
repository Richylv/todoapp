from django.db.models.fields import return_None


def get_todos():
    with open('todo.txt', 'r') as file:
        todos = file.readlines()
    return todos

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] +'\n' # example user_action: 'add play games' extract content starting from index 4 'play games'
        todos = get_todos()

        todos.append(todo)
        with open('todo.txt', 'w') as file:
            file.writelines(todos)
    elif 'show' in user_action:
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')  # .strip('/n') remmove the caracter from the list
            print(f"{index + 1}-{item}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input('Enter new to do: ')
            todos[number] = new_todo + '\n'

            with open('todo.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print('Your command is not valid')
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            with open('todo.txt', 'w') as file:
                file.writelines(todos)
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
