"""Exercício 1: Soma de Dois Números Inteiros"""

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
print(soma)

"""Exercício 2: Resto da Divisão por 5"""

num = int(input('Digite um número: '))
resto = num % 5
print(f'Resto: {resto}')

"""Exercício 3: Multiplicação de Dois Números"""

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
multiplicacao = num1 * num2
print(f'Resultado: {multiplicacao}')


"""Exercício 4: Divisão Inteira do Primeiro pelo Segundo Número"""

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
divisao = num1 // num2
print(f'Resultado: {divisao}')

"""Exercício 5: Quadrado de um Número"""

num = int(input('Digite um número: '))
quadrado = num ** 2
print(f'Resultado: {quadrado}')

"""Exercício 6: Adição de Dois Números Flutuantes"""

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
soma = num1 + num2
print(f'Resultado: {soma}')

"""Exercício 7: Média de Dois Números Flutuantes"""

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
media = (num1+num2)/2
print(f'Resultado: {media}')

"""Exercício 8: Potência de um Número"""

num1 = int(input('Digite a base da potência: '))
num2 = int(input('Digite o expoente da potência: '))
potenciacao = num1 ** num2
print(f'Resultado: {potenciacao}')

"""Exercício 9: Conversão de Celsius para Fahrenheit"""

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")

"""Exercício 10: Área de um Círculo"""

raio = float(input("Digite o raio do círculo: "))
area = 3.14159 * raio ** 2
print("A área do círculo é:", area)

"""Exercício 11: Converter String para Maiúsculas"""

texto = input('Digite uma palavra: ')
texto = texto.upper()
print(texto)

"""Exercício 12: Imprimir Nome Completo em Minúsculas"""

nome = input('Digite seu nome completo: ')
nome = nome.lower()
print(nome)

"""Exercício 13: Remover Espaços em Branco de uma Frase"""

frase = input('Digite uma frase: ')
#frase = frase.replace(' ','')
frase = frase.strip()
print(frase)

"""Exercício 14: Separar Dia, Mês e Ano de uma Data"""

data = input('Digite uma data: ')
dia, mes, ano = data.split('/')
print(dia)
print(mes)
print(ano)

"""Exercício 15: Concatenar Duas Strings"""

texto1 = input('Digite texto 1: ')
texto2 = input('Digite texto 2: ')
texto_final = texto1 + texto2
print(texto_final)

"""Exercício 16. Operador and (E lógico)"""

valor1 = True
valor2 = False
resultado = valor1 and valor2
print(resultado)

"""Exercício 17. Operador or (OU lógico)"""

valor1 = False
valor2 = True
resultado = valor1 or valor2
print(resultado)

"""Exercício 18. Operador not (NÃO lógico)"""

valor = input('Digite é alto(a): ')
resultado = not valor

print(f'Resultado: {resultado}')

"""Exercício 19. Operador == (Igualdade)"""

valor1 = input('Digite sua senha: ')
valor2 = input('Confirme sua senha: ')
resultado = (valor1 == valor2)
print(resultado)

"""Exercício 20. Operador != (Diferença)"""

valor1 = input('Digite seu email: ')
valor2 = input('Confirme seu email: ')
resultado = (valor1 != valor2)
print(resultado)


