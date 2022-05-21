quantidadeAtletas = int(input("Digite a quantidade de atletas: "))
alturaMin = 9999.0
idadeMax = 0
media = []
nomeMaisVelho = ""
nomeMaisBaixo = ""

for i in range(quantidadeAtletas):
    print("\nAtleta", i + 1)
    nome = input("\nDigite o nome do atleta ")
    idade = int(input("Digite a idade do atleta "))
    altura = float(input("Digite a altura do atleta "))

    if idade > idadeMax:
        idadeMax = idade
        nomeMaisVelho = nome

    media.append(altura)

    if altura < alturaMin:
        alturaMin = altura
        nomeMaisBaixo = nome

mediaDeAltura = sum(media)/len(media)

print("\n\nO atleta mais baixo é: ", nomeMaisBaixo)
print("a média de altura dos atletas é: ", mediaDeAltura)
print("O atleta mais velho é: ", nomeMaisVelho)