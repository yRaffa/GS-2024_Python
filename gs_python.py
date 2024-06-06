# ----- FUNÇÕES ----- #

# Funcao para forcar uma entrada numerica
def forcaNumerico(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\n > Digite apenas valores numericos. \n')               
    return num

# Funcao para forcar uma escolha pre determinada do sistema
def forcaEscolha(lista, msg):
    erro = ', '.join(lista)
    while True:
        elemento = input(msg)
        if elemento in lista:
            break
        else:
            print(f'\n > Digite uma destas opcoes: {erro}. \n')   
    return elemento

# Funcao para guardar o indice da escolha feita
def buscaIndice(elemento, lista):
    for i in range(len(lista)):
        if lista[i] == elemento:  
            return i
        
        
# ----- PROGRAMA ----- #

# Declarando listas
lista_opcoes = ['REGISTRAR', 'METAS', 'REGISTROS', 'SAIR']
lista_residuos = ['Plasticos', 'Microplasticos', 'Poluentes Liquidos', 'Organicos']
lista_quantidades = [0, 0, 0, 0]
lista_metas = [50, 100, 150, 50]

# Loop do sistema
while True:
    
    # Inicio do sistema
    print('\n----------------------------------------------------------------')
    print('>>> GESTAO DE RESIDUOS COLETADOS E FILTRADOS PARA RECICLAGEM <<<')
    print('----------------------------------------------------------------\n')
    
    # Funcionalidades do sistema
    print('1. Registrar residuo coletado \n'
          '2. Verificar meta dos residuos filtrados \n'
          '3. Visualizar residuos registrados \n'
          '4. Sair')

    erro = ', '.join(lista_opcoes)
    print(f'\n > Digite uma destas opcoes: {erro}. \n')

    # Escolha da funcionalidade do sistema
    escolha = forcaEscolha(lista_opcoes, 'Escolha uma opcao: ')
    
    # Registrando residuos coletados
    if escolha == 'REGISTRAR':
        
        # Residuos
        print('\n > RESIDUOS: \n')
        print('1. Plasticos \n'
              '2. Microplasticos \n'
              '3. Poluentes Liquidos \n'
              '4. Organicos \n')
        
        # Residuo coletado
        residuo = forcaEscolha(lista_residuos, 'Digite o residuo que foi coletado: ')
        i = buscaIndice(residuo, lista_residuos)
        
        # Quantidade do residuo
        qtd = forcaNumerico(f'Digite a quantidade de {lista_residuos[i]} que foi coletada (Kg ou L): ')
        lista_quantidades[i] += qtd

        # Registro bem sucedido
        print('\n > Residuo registrado com sucesso: \n' 
              f'Residuo: {lista_residuos[i]} \n'
              f'Quantidade: {lista_quantidades[i]} Kg ou L \n')

    # Verificando metas
    elif escolha == 'METAS':
        
        # Metas
        print('\n > METAS: \n')
        
        # Percorrendo todos os itens da lista de residuos
        for i in range(len(lista_residuos)):
            
            # Meta alcancada
            if lista_quantidades[i] >= lista_metas[i]:
                print(f'A meta de {lista_residuos[i]} coletados e filtrados para reciclagem FOI ALCANCADA.')
                
            # Meta nao alcancada
            else:
                print(f'A meta de {lista_residuos[i]} coletados e filtrados para reciclagem ainda NÃO FOI ALCANCADA.')
            print('')
    
    # Visualizando registros do sistema
    elif escolha == 'REGISTROS':
        
        # Registros
        print('\n > RESIDUOS REGISTRADOS: \n')
        
        # Percorrendo todos os itens da lista de residuos
        for i in range(len(lista_residuos)):
            
            # Registro do residuo e sua respectiva quantidade
            print(f'Residuo: {lista_residuos[i]} \n'
                  f'Quantidade: {lista_quantidades[i]} Kg ou L \n')
    
    # Saida do sistema
    elif escolha == 'SAIR':
        print('\n > SAINDO...')
        break

print('\n > Obrigado por utilizar nosso sistema!!! \n')