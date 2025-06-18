def get_average():
    with open('data.txt','r') as file:
        data = file.readlines()

    print(data)
    values = data[1:] #dont take title from file data
    print(values)
    values = [float(i) for i in values] #change values from str to float
    print(values)
    average_local = sum(values) / len(values)
    return average_local


average = get_average()
print(average)