"""
The main purpose of the module is to open a web browser from a Python script,
and it can be used to open URLs in the default browser or a specific browser.
"""
import webbrowser

user = input('Enter a search term: ')

webbrowser.open('https://google.com/search?q='+ user)