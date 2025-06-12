from traceback import print_exc

todos = ['a','b','c']

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a to do: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input('number of to editing: '))
            number = number - 1
            new_todo = input('Enter new to do: ')
            todos[number] = new_todo
        case 'exit':
            break
        case _:
            print('Hey! you entered an unknown command')

print('BYE')
