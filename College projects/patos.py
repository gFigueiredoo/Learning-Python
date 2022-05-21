p = int(input("Digite a quantidade de patos: "))
pInicial = p

while p != 0:
    if p == 1:
        print(p, "Patinho")
        print("Foi passear\nAlém das montanhas\nPara brincar\nA mamãe gritou\nQuack quack quack\nMas nenhum patinho\nVoltou de lá\n")
    else:
        print(p, "Patinhos")
        print ("Foram passear\nAlém das montanhas\nPara brincar\nA mamãe gritou\nQuack quack quack\nMas só", p-1, "patinhos\nVoltaram de lá\n")
  
    p -= 1

if p == 0:
    print("A mamãe patinha\nFoi procurar\nAlém das montanhas\nNa beira do mar\nA mamãe gritou\nQuack quack quack\nE os", pInicial, "patinhos\nVoltaram de lá")