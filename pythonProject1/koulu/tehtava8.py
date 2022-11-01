avaimet = ['Kymmenen', 'kaksikymmentä', 'kolmekymmentä']
arvot = [10, 20, 30]

numbers = {}

for x in range(0,3):
    numbers.update({avaimet[x]:arvot[x]})

print(numbers)