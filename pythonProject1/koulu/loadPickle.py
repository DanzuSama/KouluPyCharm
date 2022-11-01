import pickle

filename = open("notebook.dat","rb")
justread = pickle.load(filename)

print("Following was just read: ",justread)
print(justread[2],justread[3])
filename.close()