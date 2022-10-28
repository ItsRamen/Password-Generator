import secrets, string, os, sys
import pyperclip as pc
from unicodedata import digit

# Declare letters, numbers, and special characters as variables.
letters = string.ascii_letters
numbers = string.digits
special_characters = string.punctuation
alphabet = letters + numbers + special_characters

# Password length
pwd_length = 16
pwd = ''

# Password generation
for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

# Conditions
while True:
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    if (any(char in special_characters for char in pwd) and 
        sum(char in numbers for char in pwd)>=2):
        break

# Copy password to clipboard
copied_text = 'Password is in clipboard!'
pc.copy(pwd)

# GUI PROGRAM
import PySimpleGUI as sg

def callback_function1():
    window['PASSWORD'].update(copied_text)

def callback_function2():
    if event == "Close":
      window.close()

def callback_function3():
    if event == 'Reset':
        window.close()      # Currently figuring out a reset button

layout = [[sg.Text('Welcome to my first GUI program!')],
          [sg.Text('made by Ramee :)')],
          [sg.Button('Generate Password'), sg.Button('Close'), sg.Button('Reset')],
          [sg.Text('', key='PASSWORD')]]

window = sg.Window('Password Generator', layout)

# Event Loop
while True:             
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

# Callback Functions
    elif event == 'Generate Password':
        callback_function1()
    elif event == 'Close':
        callback_function2()
    elif event == 'Reset':
        callback_function3()

window.close()
