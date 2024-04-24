"""Exercício 21: Conversor de Temperatura"""

# celsius = None

# while celsius == None:
#     try:
#         celsius = float((input("\nDigite a temperatura em Celsius: ")).strip())
#     except ValueError:
#         print("\nVocê digitou um número inválido.\nExemplo de formato correto: 25.3")
#         celsius = None
#     except:
#         print('\nErro inesperado. Digite a temperatra novamente: ')
#         celsius = None
    
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius}°C é igual a {fahrenheit}°F")

"""Exercício 22: Verificador de Palíndromo"""

"""Crie um programa que verifica se uma palavra ou frase é um palíndromo 
(lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
Utilize try-except para garantir que a entrada seja uma string. 
Dica: Utilize a função isinstance() para verificar o tipo da entrada."""

# texto = input('Digite uma palavra: ')

# if isinstance(texto, str):
#     texto_final = texto.replace(" ","").lower()
#     if texto_final == texto_final[::-1]:
#         print('É um palíndromo')
#     else:
#         print('Não é um palíndromo')
# else:
#     print(f'A entrada {texto} é inválida. Tente novamente com uma palavra ou texto')
#     texto = None

"""Exercício 23: Calculadora Simples

Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador 
(+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas 
não numéricas. 
Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
Imprima o resultado ou uma mensagem de erro apropriada."""

# num1 = None
# num2 = None
# operador = None

# while operador == None:
#     operador = input('Digite a letra correspondente a operação desejada: \n a. Soma \n b. Subtração \n c. Multiplicação \n d. Divisão:\n ').lower().replace(" ","").replace(".","")
#     if len(operador) != 1:
#         print('Você digitou um valor inválido! selecione dentre as opções: a, b, c ou d')
#         operador = None
#     elif operador not in ('a','b','c','d'):
#         print('Você digitou um valor inválido! selecione dentre as opções: a, b, c ou d')
#         operador = None

# while num1 == None:
#     try:
#         num1 = float(input('Digite um valor: ').replace(" ",""))
#     except ValueError:
#         print('Você inseriu um valor inválido! digite apenas números. \nExemplos: 25 ou 10.5')
#         num1 = None

# while num2 == None:
#     if operador == 'd':    
#         try:
#             num2 = float(input('Digite outro valor: ').replace(" ",""))
#             num1 / num2
#         except ValueError:
#             print('Você inseriu um valor inválido! digite apenas números. \nExemplos: 25 ou 10.5')
#             num2 = None
#         except ZeroDivisionError:
#             print('Você inseriu um valor inválido! digite um número diferente de zero. \nExemplos: 25 ou 10.5')
#             num2 = None
#     else:
#         try:
#             num2 = float(input('Digite outro valor: ').replace(" ",""))
#         except ValueError:
#             print('Você inseriu um valor inválido! digite apenas números. \nExemplos: 25 ou 10.5')
#             num2 = None

# if operador == 'a':
#     resultado = num1 + num2
# elif operador == 'b':
#     resultado = num1 - num2
# elif operador == 'c':
#     resultado = num1 * num2
# elif operador == 'd':
#     resultado = num1 / num2

# print(resultado)

"""Exercício 24: Classificador de Números

Escreva um programa que solicite ao usuário para digitar um número. 
Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else 
para classificar o número como "positivo", "negativo" ou "zero". 
Adicionalmente, identifique se o número é "par" ou "ímpar"."""

# num = None

# while num == None:
#     try:
#         num = float(input('\nDigite um número: ').replace(" ",""))
#     except ValueError:
#         print('Você digitou um valor inválido. Serão aceitos apenas número como nos exemplos abaixo: \n 10\n 10.5\n -12\nTente novamente: ')
#         num = None

# if num > 0:
#     sinal = 'positivo'
# elif num == 0:
#     sinal = 'zero'
# elif num < 0:
#     sinal = 'negativo'

# if num % 2 == 0:
#     par_ou_impar = 'par'
# else:
#     par_ou_impar = 'ímpar'


# print(f'O número é {sinal} e {par_ou_impar}')

"""Exercício 25: Conversão de Tipo com Validação

Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
O programa deve converter a string de entrada em uma lista de números inteiros. 
Utilize try-except para tratar a conversão de cada número e validar que cada elemento 
da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um 
inteiro, imprima uma mensagem de erro. 
Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros."""

num = None
while num == None:
    try:
        num = input('\nDigite uma lista de números: ')
        num_v2 = num.split(',')
        num_int = []

        for num in num_v2:
            num_int.append(int(num.strip()))
    except ValueError:
        print('\nValor digitado inválido! a lista deve ser composta da seguinte forma:\nExemplo: 12, -1, 20, 30,40\n\nTente novamente!')
        num = None
print(f'\nAqui está sua lista de números: {num_int}')
    
