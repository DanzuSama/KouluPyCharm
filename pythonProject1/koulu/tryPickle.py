list = []
num_list = []
for x in num:
    list.append(x)
for i in range(len(list)):
    num_list = (list[i][1])
    print(min(int(num_list)))

# -*- coding: cp1252 -*-

import pickle

listexample = ["Pineapple", "Atlas", ("Shaft", "Blade"), 1150]
filename = open("saveme.txt","wb")
print(listexample)
pickle.dump(listexample,filename)

filename.close()