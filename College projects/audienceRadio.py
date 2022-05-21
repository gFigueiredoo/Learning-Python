audiencetList = []
crescent = True
keep = "S"

while keep == "S":

    index = int(input("Digite a quantidade de índices de audiência serão digitados: "))

    for x in range(index):
        audience = float(input())
        audiencetList.append(audience)

    av = sum(audiencetList) / index

    for i in range(1, index):
        if audiencetList[i - 1] > audiencetList[i]:
            crescent = False
        break
    
    print("AUDIÊNCIA SEMPRE CRESCENTE. Média de audiência: " if crescent else "AUDIÊNCIA NEM SEMPRE CRESCENTE. Média de audiência: ", av)
    keep = input("Deseja continuar? S ou N: ")