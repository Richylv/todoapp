#los dos metodos son similares

#file = open('todo.txt','r') #read file todo txt
#   todos = file.readlines() #asignar text from file to a list
#file.close()

#with open('todo.txt','r') as file:  #open ('todo.txt') sin argumeto se toma por default 'r' read
#    todos = file.readlines()
#---------------------------------------------------
name = input('name of the file: ')
with open(f'../{name}.txt', 'w') as file:
    file.write('this is an example on how to create a file .txt')
