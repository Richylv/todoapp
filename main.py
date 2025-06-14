from traceback import print_exc

todos = ['a','b','c']

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a to do: ")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                print(f"{index + 1}-{item}")
        case 'edit':
            number = int(input('number of todo to edit: '))
            number = number - 1
            new_todo = input('Enter new to do: ')
            todos[number] = new_todo
        case 'complete':
            number = int(input('number of to do complete: '))
            todos.pop(number- 1)
        case 'exit':
            break
        case _:
            print('Hey! you entered an unknown command')

print('BYE')
