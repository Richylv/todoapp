while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a to do: ") + '\n'
            with open('todo.txt','r') as file:
                todos = file.readlines()

            todos.append(todo)
            with open('todo.txt', 'w') as file:
                file.writelines(todos)
        case 'show' | 'display':
            with open('todo.txt','r') as file:
               todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n') #.strip('/n') remmove the caracter from the list
                print(f"{index + 1}-{item}")
        case 'edit':
            number = int(input('number of todo to edit: '))
            number = number - 1

            with open('todo.txt','r') as file:
               todos = file.readlines()
            new_todo = input('Enter new to do: ')
            todos[number] = new_todo + '\n'

            with open('todo.txt','w') as file:
               file.writelines(todos)
        case 'complete':
            number = int(input('number of to do complete: '))
            with open('todo.txt','r') as file:
               todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            with open('todo.txt','w') as file:
               file.writelines(todos)
            message = f'To Do {todo_to_remove} was removed from the list'
            print(message)
        case 'exit':
            break
        case _:
            print('Hey! you entered an unknown command')

print('BYE')
