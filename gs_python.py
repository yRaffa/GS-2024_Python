# ----- FUNÇÕES ----- #

def forcaNumerico(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\n > Digite apenas valores numericos. \n')               
    return num

def forcaEscolha(lista, msg):
    erro = ', '.join(lista)
    while True:
        elemento = input(msg)
        if elemento in lista:
            break
        else:
            print(f'\n > Digite uma destas opcoes: {erro}. \n')   
    return elemento

def buscaIndice(elemento, lista):
    for i in range(len(lista)):
        if lista[i] == elemento:  
            return i
        
        
# ----- PROGRAMA ----- #

lista_opcoes = ['REGISTRAR', 'METAS', 'REGISTROS', 'SAIR']
lista_residuos = ['Plasticos', 'Microplasticos', 'Poluentes Liquidos', 'Organicos']
lista_quantidades = [0, 0, 0, 0]
lista_metas = [50, 100, 150, 50]

while True:
    print('\n > Sistema de gestão de residuos coletados e filtrados: \n')
    print('1. Registrar residuo filtrado \n'
          '2. Verificar meta dos residuos filtrados \n'
          '3. Visualizar residuos filtrados \n'
          '4. Sair')

    erro = ', '.join(lista_opcoes)
    print(f'\n > Digite uma destas opcoes: {erro}. \n')

    escolha = forcaEscolha(lista_opcoes, 'Escolha uma opcao: ')
    
    if escolha == 'REGISTRAR':
        print('\n > RESIDUOS: \n')
        print('1. Plasticos \n'
              '2. Microplasticos \n'
              '3. Poluentes Liquidos \n'
              '4. Organicos \n')
        
        residuo = forcaEscolha(lista_residuos, 'Digite o residuo que foi filtrado: ')
        i = buscaIndice(residuo, lista_residuos)
        
        qtd = forcaNumerico(f'Digite a quantidade de {lista_residuos[i]} que foi filtrada (Kg ou L): ')
        lista_quantidades[i] += qtd

        print('\n > Residuo registrado com sucesso: \n' 
              f'Residuo: {lista_residuos[i]} \n'
              f'Quantidade: {lista_quantidades[i]} Kg ou L \n')

    elif escolha == 'METAS':
        print('\n > METAS: \n')
        for i in range(len(lista_residuos)):
            if lista_quantidades[i] >= lista_metas[i]:
                print(f'A meta de {lista_residuos[i]} coletados e filtrados para reciclagem FOI ALCANCADA.')
            else:
                print(f'A meta de {lista_residuos[i]} coletados e filtrados para reciclagem ainda NÃO FOI ALCANCADA.')
            print('')
        
    elif escolha == 'REGISTROS':
        print('\n > RESIDUOS REGISTRADOS: \n')
        for i in range(len(lista_residuos)):
            print(f'Residuo: {lista_residuos[i]} \n'
                  f'Quantidade: {lista_quantidades[i]} Kg ou L \n')
        
    elif escolha == 'SAIR':
        print('\n SAINDO...')
        break

print('\n > Obrigado por utilizar nosso sistema!!! \n')