user_count_input = 0
score_count = ['', '', '', '', '', '']
average_score = 0
pro_count = 0

#add * in list when know score

def statistic(x):
    if x == 0:
        score_count[0] += "*"
    if x == 1:
        score_count[1] += "*"
    if x == 2:
        score_count[2] += "*"
    if x == 3:
        score_count[3] += "*"
    if x == 4:
        score_count[4] += "*"
    if x == 5:
        score_count[5] += "*"

#printing all Data when press ""

def printingAllData():
    print(f"Tilasto: \nPisteiden keskiarvo: {average_score / user_count_input}"
          f" \nHyväksymisprosentti: {100-((100 / user_count_input) * pro_count)}\nArvosanajakauma: "
          f"\n5: {score_count[5]}\n4: {score_count[4]}\n3: {score_count[3]}\n2: "
          f"{score_count[2]}\n1: {score_count[1]}\n0: {score_count[0]}")

#determine the number of points

def count(x):
    global pro_count
    score = 0
    if x < 14:
        score = 0
        pro_count += 1
    elif x <= 17:
        score = 1
    elif x <= 20:
        score = 2
    elif x <= 23:
        score = 3
    elif x <= 27:
        score = 4
    elif x <= 30:
        score = 5
    return score

#slice and get num value for input

def sliceInput(x):
    global average_score

    x = user.split()
    num1 = x[0]
    num2 = x[1]
    num3 = int(num1) + (int(num2) / 100) * 10
    num4 = int(num3)
    average_score += num4

    final_score = count(num4)
    statistic(final_score)


while True:
    user = input("Koepisteet ja harjoitusten määrä: ")
    if user == "":
        printingAllData()
        break
    user_count_input += 1
    sliceInput(user)