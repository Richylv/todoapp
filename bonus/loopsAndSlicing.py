"""Loops and Slicing
In the coding area we have defined a list of filenames. Your task is to:
(1) loop over the list
(2) print out the filename of each item without the extension using slicing."""

filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
#Solution with Slicing
for file in filenames:
    file = file[0:-4] # [0:5] number positive primer caracter al caracter 4
                      # [0:-4] negative number gives you four last element
    print(file)
    
#solution with List Comprehension
#filenames = [filename.replace('.txt','') for filename in filenames]
#for file in filenames:
#    print(file)

