try:
    i = 1
    mynote = open('notebook.txt', 'w')
    x = mynote.readlines()
    for i in x:
        print(i[:-1])
except IOError:
    print("No default notebook was found, created one.")