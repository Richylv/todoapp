# List Comprehension
#---------------------------------------------------------------------------
filenames = ['1.raw data', '2.reports', '3.presentation']

filenames = [filename.replace('.','-') + '.txt' for filename in filenames]

print(filenames)
#---------------------------------------------------------------------------
#converts the numbers from strings to floats
user_entries = ['10', '19.1', '20']
number = [float(number) for number in user_entries]
print(number)
#----------------------------------------------------------------------
#list containing the number of characters for each username.
usernames = ["john 1990", "alberta1970", "magnola2000"]
usernames = [len(user) for user in usernames]
print(usernames)