def parse(feet_inches):
    print(feet_inches)
    parts = feet_inches.split(' ')
    print(parts)
    feet = float(parts[0])
    inches = float(parts[1])

    return feet, inches

def convert(feet, inches):
    """ recive feet and inches and returns a message with the value in meters"""
    meters = feet * 0.3048 + inches * 0.0254
    return f'{feet} feet and {inches} inches is equal {meters} meters.'

print(help(convert)) #print the description that is writing on the function


feet_inches = input('Enter feet and inches: ') #expect input example 5 11
f, i = parse(feet_inches)

print(convert(f,i))

#################################################3
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