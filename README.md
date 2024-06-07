# 🌎 GS Inovação Azul

[Vídeo de Explicação](https://drive.google.com/file/d/1GN2nHNuG33uEqMDNzeV3WUVm6VlePUiJ/view?usp=sharing)

## 🐍 Computational Thinking with Python

Entrega da matéria Computational Thinking with Python para GS 2024.

## 👥 Integrantes

- RM: 556506 // Nicolas Caciolato Reis
- RM: 554736 // Rafael Federici de Oliveira

## 📕 Sobre o Projeto

Sistema da BlueWave, para gerir e administrar coleta de residuos poluentes nos mares, os quais são coletados e filtrados por embarcações marinhas, com o intuito de serem levados a um sistema de reciclagem.

## 🔨 Ferramentas

- [Visual Studio Code](https://code.visualstudio.com/docs)
- [Python](https://www.python.org/doc/)

## 🖥️ Requisitos

- Instalar uma IDE ou Editor de Código ([PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/?section=windows) ou [Visual Studio Code](https://code.visualstudio.com/Download)) em seu computador.
- Instalar [Python](https://www.python.org/downloads/) em seu computador.
- Abrir estre projeto no aplicativo escolhido.

## 📒 Instruções de Uso

- Abrir este [projeto](https://github.com/yyRaffa/GS_Python.git) em uma IDE ou Editor de Código.
- Compilar e 'rodar' o código.
- Seguir as intruções qua aparecerão no console do programa.

## 🧠 Explicando o Código

- Função para forçar uma entrada numerica no sistema:
``` python
def forcaNumerico(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print('\n > Digite apenas valores numericos. \n')    
```

- Função para forçar uma escolha pré determinada do sistema:
``` python
def forcaEscolha(lista, msg):
    erro = ', '.join(lista)
    while True:
        elemento = input(msg)
        if elemento in lista:
            return elemento
        else:
            print(f'\n > Digite uma destas opcoes: {erro}. \n')   
```

- Função que busca e guarda o indice de um elemento de uma lista.
``` python
def buscaIndice(elemento, lista):
    for i in range(len(lista)):
        if lista[i] == elemento:  
            return i
```

- Declaração das listas utilizadas no sistema.
``` python
lista_opcoes = ['REGISTRAR', 'METAS', 'REGISTROS', 'SAIR']
lista_residuos = ['PLASTICOS', 'MICROPLASTICOS', 'POLUENTES LIQUIDOS', 'ORGANICOS']
lista_quantidades = [0, 0, 0, 0]
lista_metas = [50, 100, 150, 50]
```

- Parte inicial, onde se escolhe oque dejesa fazer no programa.
``` python
while True:
    print('\n----------------------------------------------------------------')
    print('----------------------------BlueWave----------------------------')
    print('>>> GESTAO DE RESIDUOS COLETADOS E FILTRADOS PARA RECICLAGEM <<<')
    print('----------------------------------------------------------------\n')
    print('1. Registrar residuo coletado \n'
          '2. Verificar meta dos residuos filtrados \n'
          '3. Visualizar residuos registrados \n'
          '4. Sair')

    erro = ', '.join(lista_opcoes)
    print(f'\n > Digite uma destas opcoes: {erro}. \n')

    escolha = forcaEscolha(lista_opcoes, 'Escolha uma opcao: ')
```

- Código executada caso a escolha seja REGISTRAR.

Registra residuos coletados e suas respectivas quantidades.
``` python
if escolha == 'REGISTRAR':
        print('\n > RESIDUOS: \n')
        print('1. Plasticos \n'
              '2. Microplasticos \n'
              '3. Poluentes Liquidos \n'
              '4. Organicos \n')
        
        residuo = forcaEscolha(lista_residuos, 'Digite o residuo que foi coletado: ')
        i = buscaIndice(residuo, lista_residuos)
        qtd = forcaNumerico(f'Digite a quantidade de {lista_residuos[i]} que foi coletada (Kg ou L): ')
        lista_quantidades[i] += qtd

        print('\n > Residuo registrado com sucesso: \n' 
              f'Residuo: {lista_residuos[i]} \n'
              f'Quantidade: {lista_quantidades[i]} Kg ou L \n')
```

- Código executada caso a escolha seja METAS.

Verifica se os residuos coletados até então atingiram as metas pré estipuladas.
``` python
elif escolha == 'METAS':
        print('\n > METAS: \n')
        
        for i in range(len(lista_residuos)):
            if lista_quantidades[i] >= lista_metas[i]:
                print(f'A meta de {lista_residuos[i]} coletados e filtrados para reciclagem FOI ALCANCADA.')
            else:
                print(f'A meta de {lista_residuos[i]} coletados e filtrados para reciclagem ainda NÃO FOI ALCANCADA.')
            print('')
```

- Código executada caso a escolha seja REGISTROS.

Exibe todos os registros de residuos, com o total de suas quantidades.
``` python
elif escolha == 'REGISTROS':
        print('\n > RESIDUOS REGISTRADOS: \n')
        
        for i in range(len(lista_residuos)):
            print(f'Residuo: {lista_residuos[i]} \n'
                  f'Quantidade: {lista_quantidades[i]} Kg ou L \n')
```

- Código executada caso a escolha seja SAIR.

Encerra o funcionamento do código, saindo do programa.
``` python
elif escolha == 'SAIR':
        print('\n > SAINDO...')
        break

print('\n > Obrigado por utilizar nosso sistema!!! \n')
```