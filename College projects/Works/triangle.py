print('Olá Fulano')

choose = 0
while choose != 7:
    choose = int(input('''
    Olá Fulano.
    Digite a opção desejada:
    1) Verificar triângulo
    2) Calcular equação do segundo grau
    3) Conferir data
    4) Verificar tamanho do texto
    5) Analisar CPF
    6) Contar caracteres
    7) Sair
    Escolha: ''' ))
    
    if choose == 1:
        firstSide  = float(input('First Side: '))
        secondSide = float(input('second Side: '))
        thirdSide  = float(input('third Side: '))
        
        if (firstSide + secondSide < thirdSide) or (firstSide + thirdSide < secondSide) or (secondSide + thirdSide < firstSide):
            print('\n***Não é um triângulo***\n')
            
        elif (firstSide == secondSide) and (firstSide == thirdSide):
            print('\n***O triângulo eh Equilatero***\n')
            
        elif (firstSide == secondSide) or (firstSide == thirdSide) or (secondSide == thirdSide):
            print('\n***O triângulo eh Isósceles***\n')
            
        else:
            print('\n***O triângulo eh Escaleno***\n')
    
    elif choose == 2:
        print('\nA equação é a seguinte: ax² - bx + c = 0\n')
        
        a = int(input('Digite o valor de a: '))
        
        if a == 0:
            print('\nNão se trata de uma equação de segundo grau, o valor de A nao pode ser 0')

        else:    
            b = int(input('Digite o valor de b: '))
            c = int(input('Digite o valor de c: '))
            
            delta= b * b - 4 * a * c
        
            if delta < 0:
                print('\nO delta é {} e a equação não possui raízes reais'.format(delta))

            elif delta == 0:
                print('A equação possui apenas uma raiz real')
                x = (-b - (delta) ** (1/2) / (2*a))
            
            else:
                x = (-b - (delta) ** (1/2) / (2*a))
                x1 = (-b + (delta) ** (1/2) / (2*a))
            
                print('x1 = {}, x2 = {}'.format(x1, x))
    
    elif choose == 3:
        day   = int(input('Dia: '))
        month = int(input('Mês: '))
        year  = int(input('Ano: '))

        valida = False
        
        if(month == 1 or month == 2 or month == 3 or month == 5 or \
            month == 7 or month == 8 or month == 10 or month == 12):
            
            if(day <= 31):
                valida = True
                
        elif(month == 4 or month == 6 or month == 9 or month == 11):
            
            if(day <= 30):
                valida = True

        if(valida):
            print('\nData válida\n')
        else:
            print('\nInválida\n')
    
    elif choose == 4:
        text = input('Digite o texto: ')
        size = len(text)
        
        if size < 5:
            print('\nO texto é muito pequeno\n')
        elif size >= 5 and size < 15:
            print('\nO texto é do tamanho médio\n')
        elif size >= 15 and size <= 20:
            print('\nO texto é grande\n')
        else: 
            print('\nTexto invalido\n')     
    
    elif choose == 5:
        cpf = input('Digite o CPF apenas com números: ')     
        isValid = cpf.isdigit() and len(cpf) == 11
        
        if isValid:
            print('\nCPF valido\n')
        else: 
            print('\nCPF invalido\n')
    
    elif choose == 6:
        word = input('\nDigite a palavra: ')
        
        space = word.count(' ')
        
        vowels = 'aeiou'
        qtd_vowels = len([c for c in word.lower() if c in vowels])
        
        nonVowels = 'bcdfghjklmnpqrstvxywz'
        qtd_nonVowels = len([c for c in word.lower() if c in nonVowels])
        
        ec = len(word) - qtd_vowels - qtd_nonVowels - space
        
        print('\nQuantidade de espaços: ', space)
        print('\nQuantidade de vogais: ', qtd_vowels)
        print('\nQuantidade de consoantes: ', qtd_nonVowels)
        print('\nQuantidade de caracteres especiais: ', ec)
    
    elif choose == 7:
        print('\nEncerrando Programa...\n')
        exit(0)
    
    elif choose > 7 or choose < 1:
        print("\nEste número não está nas alternativas, tente novamente.")