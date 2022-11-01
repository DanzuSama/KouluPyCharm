
def check_note():
    try:
        mynote = open('notebook.txt', 'w')
        x = mynote.readlines()
        for i in x:
            print(i[:-1])
    except IOError:
        print("No default notebook was found, created one.")


go = True
while go:
    notebook = check_note()
    print('Now using file ' + str([notebook]))
    print('(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Change the notebook \n(5) Quit')
    i = int(input('Please select one: '))
    if i == 1:
        mynote = open('notebook.txt', 'r')
        x = mynote.readlines()
        for i in x:
            print(i[:-1])
    elif i == 2:
        mynote = open('notebook.txt', 'a')
        addText = str(input('Write a new note:'))
        mynote.write(addText + '\n')
        mynote.close()
    elif i == 3:
        mynote = open('notebook.txt', 'w')
        addText = ''
        mynote.write(addText)
        mynote.close()
        print('Notes deleted.')
    elif i == 4:
        print("Give the name of the new file: ")
    elif i == 5:
        go = False
        print('Notebook shutting down, thank you.')
    else:
        print('Incorrect selection')



