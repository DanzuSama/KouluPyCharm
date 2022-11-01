names = ["Michele", "Robin", "Sara", "Michele", "Taylor", "Nora"]

def double(list):
    k = []
    for x in list:
        if x not in k:
           k.append(x)
    return k
print(double(names))