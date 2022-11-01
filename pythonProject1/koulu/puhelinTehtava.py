
phonebook = {'Pekka': 45454545454}
while True:
    userInput = input('komento (1 hae, 2 lisää, 3 lopeta): ')
    if userInput == "1":
        searchName = input('nimi: ')
        if searchName in phonebook.keys():
            print('numero:' + str(phonebook[searchName]))
        else:
            print("ei ole")
    if userInput == '2':
        newUserName = input('nimi: ')
        newUserNum = input('numero: ')
        phonebook[newUserName] = newUserNum
        print("ok")
    if userInput == '3':
        print('lopetetaan...')
        break
