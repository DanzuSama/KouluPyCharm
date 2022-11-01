import time

opening_note = ""
default_note = "notebook.txt"


def checkNote():
    try:
        global opening_note
        opening_note = open(default_note, "r")
        print(f'Now using file {opening_note.name}')
    except IOError:
        opening_note = open(default_note, 'x')
        print(f'No default notebook was found, created one. \n'
              f'Now using file {opening_note.name}')

def checkName():
    try:
        global opening_note
        opening_note.close()
        opening_note = open(default_note, "r")
    except IOError:
        opening_note = open(default_note, 'w')
        print(f'No notebook with that name detected, created one.')

go = True
while go:

    checkNote()
    print('(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Change the notebook \n(5) Quit')
    i = int(input('Please select one: '))
    if i == 1:
        opening_note.close()
        opening_note = open(default_note, 'r')
        x = opening_note.readlines()
        for i in x:
            print(i[:-1])
    elif i == 2:
        opening_note.close()
        opening_note = open(default_note, 'a')
        addText = str(input('Write a new note:'))
        opening_note.write(addText + ':::' + time.strftime("%X %x") + '\n')
        opening_note.close()
    elif i == 3:
        opening_note.close()
        opening_note = open(default_note, 'w')
        addText = ''
        opening_note.write(addText)
        opening_note.close()
        print('Notes deleted.')
    elif i == 4:
        default_note = input("Give the name of the new file: ")
        checkName()
    elif i == 5:
        go = False
        print('Notebook shutting down, thank you.')
    else:
        print('Incorrect selection')
