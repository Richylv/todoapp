filenames = ['1.raw data.txt', '2.reports.txt', '3.presentation.txt']  #lista
filenames1 = ('1.raw data.txt', '2.reports.txt', '3.presentation.txt')  #tuple no se puede modificar

filename = '1.raw data.txt'
print(filename[1])
filename = filename.replace('.', '-', 1)  # '1' cambia solo la primera vez que aparezca
print(filename)

print(dir(str))

for meal in 'meals':
    print(meal)

a = '5'
b = 10

# print(a+b) #Error por diferentes tipos str != int

print(a * 10)
print('hi' * 5)

list = ['a', 'b', 'c']

print(dir(list))  #muestra los metodos de list

# list.__setitem__(1,'w') es lo mismo que list[1] = 'w'

mylist = ['f', 'a', 'r']
mylist.sort()  #ordena ascendente
mylist.sort(reverse=True)  #orden desendente

#file = open(r'C:\Users\Ricardo\Documents\python\toDo0', 'r')
#r al inicio raw sting ya que puede haber caracteres especiales como \t
#r como argumento para leer (read) el archivo; w para escribir (write)

a = [1, 2, 3]
b = [10, 20, 30]
x = zip(a, b) # zip junta las dos listas [(1,10),(2,20),(3,30)]

