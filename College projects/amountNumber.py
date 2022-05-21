condition = True
numberList = []
minorHundred = 0
twoHundred = 0
fourHundred = 0
highHundred = 0

while condition == True:
    number = float(input("Write a int number: "))

    if (number >= 0):
        numberList.append(number)
    else:
        condition = False

    for numberInList in numberList:
      if (0 < numberInList < 100):
        minorHundred += 1
      elif ( 101 < numberInList < 200):
        twoHundred += 1
      elif ( 201 < numberInList < 400):
        fourHundred += 1
      elif (numberInList > 400):
        highHundred += 1

    
    print("Quantidade de numeros digitados entre 0 e 100: ", minorHundred)
    print("Quantidade de numeros digitados entre 101 e 200: ", twoHundred)
    print("Quantidade de numeros digitados entre 201 e 400: ", fourHundred)
    print("Quantidade de numeros digitados maior que 400: ", highHundred)