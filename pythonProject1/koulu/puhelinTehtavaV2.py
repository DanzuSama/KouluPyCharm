phonebook = {'Pekka': 45454545454}


def checkNum(name, num):
    if name in phonebook:
        x = {phonebook[name] + str(num)}
        phonebook.update(x)

    if name not in phonebook:
        phonebook[name] = num
        print("ok")


while True:
    print(phonebook.values())
    print(phonebook.keys())
    userInput = input('komento (1 hae, 2 lisää, 3 lopeta): ')
    if userInput == "1":
        searchName = input('nimi: ')
        if searchName in phonebook.keys():
            print(str(phonebook[searchName]))
        else:
            print("ei ole")
    if userInput == '2':
        newUserName = input('nimi: ')
        newUserNum = input('numero: ')
        checkNum(newUserName, newUserNum)
    if userInput == '3':
        print('lopetetaan...')
        break
