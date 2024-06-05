
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
        
def registrarResiduo(lista):
    elemento = input('Digite o residuo que foi filtrado: ')
    erro = ', '.join(lista)
    if elemento in lista:
        return elemento
    else:
        print(f'\n > Digite uma destas opcoes: {erro}. \n')  
        
        
# ----- PROGRAMA ----- #

opcoes = ['REGISTRAR', 'VERIFICAR META', 'VISUALIZAR REGISTRADOS', 'SAIR']
lista_residuos = ['Plasticos', 'Microplasticos', 'Poluentes Liquidos', 'Organicos']
lista_quantidades = [0, 0, 0, 0]
metas = [50, 100, 150, 50]

while True:
    print('\n > Sistema de gestão de residuos filtrados: \n')
    print('1. Registrar residuo filtrado \n'
          '2. Verificar meta dos residuos filtrados \n'
          '3. Visualizar residuos filtrados \n'
          '4. Sair')

    erro = ', '.join(opcoes)
    print(f'\n > Digite uma destas opcoes: {erro}. \n')

    escolha = forcaEscolha(opcoes, 'Escolha uma opcao: ')
    
    if escolha == 'REGISTRAR':
        print('\n > RESIDUOS: \n')
        print('1. Plasticos \n'
              '2. Microplasticos \n'
              '3. Poluentes Liquidos \n'
              '4. Organicos \n')
        
        residuo = forcaEscolha(lista_residuos, 'Digite o residuo que foi filtrado: ')
        i = buscaIndice(residuo, lista_residuos)
        
        qtd = forcaNumerico(f'Digite a quantidade de {lista_residuos[i]} que foi filtrada: ')
        lista_quantidades[i] += qtd

        print('\n > Residuo registrado com sucesso: \n' 
              f'Residuo: {lista_residuos[i]} \n'
              f'Quantidade: {lista_quantidades[i]} Kg ou L \n')
    
    elif escolha == 'VERIFICAR META':
        print('\n > METAS: \n')
        
    elif escolha == 'VISUALIZAR REGISTRADOS':
        print('\n > RESIDUOS REGISTRADOS: \n')
        
        for i in range(len(lista_residuos)):
            print(f'Residuo: {lista_residuos[i]} \n'
                  f'Quantidade: {lista_quantidades[i]} Kg ou L \n')
        
    elif escolha == 'SAIR':
        break

print('\n > Obrigado por utilizar nosso programa!!! ')