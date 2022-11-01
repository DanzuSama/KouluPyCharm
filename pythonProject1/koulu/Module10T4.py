# -*- coding: cp1252 -*-
import time
import pickle

default_note = "notebook.dat"
file_list = ['some data']

with open(default_note, 'rb') as f:
    x = pickle.load(f)
    print(x)



while True:
    print('(1) Read the notebook \n(2) Add note '
          '\n(3) Edit a note \n(4) Delete a note \n(5) Save and quit')
    userInput = int(input('Please select one: '))
    if userInput == 1:
        print(file_list)
    if userInput == 2:
        add_text = str(input('Write a new note: '))
        new_line = (add_text + ':::' + time.strftime("%X %x"))
        file_list.append(new_line)
    if userInput == 3:
        print(f'The list has {len(file_list)} notes.')
        user_edit_input = input('Which of them will be changed?:')
        print(file_list[user_edit_input])
        user_edit_text_input = input('Give the new note: ')

    if userInput == 4:
        print(f'The list has {len(file_list)} notes.')
        userDeleteInput = int(input('Which of them will be deleted?: '))
        file_list.pop(userDeleteInput)
    if userInput == 5:
        print('Notebook shutting down, thank you.')
        break
