FILEPATH = 'todo.txt'

def get_todos(file_path=FILEPATH ):
    """ Read a text file and return the list of
    to-do items """
    with open(file_path, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg,file_path=FILEPATH):
    """  Write a text file with the list of
    to-do items """
    with open(file_path, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__": #
    print("Hello")
    print(get_todos())