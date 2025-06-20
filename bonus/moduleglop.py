"""
The glob module in Python is used for finding files and directories that match a specific pattern,
following Unix shell rules. It is particularly useful for tasks such as searching for files
with specific extensions, prefixes, or patterns in their names
"""

import glob

myfiles = glob.glob('../files/*.txt')

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())