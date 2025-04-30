
def menu():
    print("\n-=-=-=-MENU=-=-=-=")
    print("1 - OIBR")
    print("2 - Alice e Bob")
    print("3 - Maior Numero")
    print("4 - Informa se vota")
    print("5 - Ordem crescente")
    print("6 - Verifica Triangulos")
    print("7 - Equação 2° Grau")
    print("8 - Nota de compra Loja")
    print("-=-=-=-=-=-=-=-=-=\n")

#Dada a distância D do robô até o início da quadra, onde está a cesta, a
#regra é a seguinte:
# Se D ≤ 800, a cesta vale 1 ponto;
# Se 800 < D ≤ 1400, a cesta vale 2 pontos;
# Se 1400 < D ≤ 2000, a cesta vale 3 pontos.
#Restrição: 0 ≤ D ≤ 2000
def verificaPonto(distancia):    
    if distancia <= 0 or distancia >= 2000:
        print("Distancia invalida\n")
    elif distancia <= 800:
        print("Robo fez 1 ponto\n")
    elif distancia > 800 and distancia <= 1400:
        print("Robo fez 2 pontos\n")
    elif distancia > 1400 and distancia <= 2000:
        print("Robo fez 3 pontos\n")

def maiorNumero():
    maior = 0
    cont = 1
    while cont <= 5:
        valor = int(input(f"Digite o numero {cont}: "))
        if valor > maior:
            maior = valor
        cont+=1 
    print(f"Maior numero digitado é {maior}\n")

def informaVoto():
    idade = int(input("Digite a sua idade: "))
    if idade < 16 or idade > 65:
        print("Não tem idade para votar")
    elif idade == 16 or idade == 17:
        print("voto facultativo")
    elif idade > 17 and  idade <= 65:
        print("voto obrigatorio")

def ordemCrescente():
    maior = 0
    menor = 0
    meio = 0
    numero1 = int(input("Digite o 1° numero: "))
    numero2 = int(input("Digite o 2° numero: "))
    numero3 = int(input("Digite o 3° numero: "))
    if(numero1 > numero2 and numero1 > numero3):
        maior = numero1
    elif(numero2 > numero1 and numero2 > numero3):
        maior = numero2
    elif(numero3 > numero1 and numero3 > numero2):
        maior = numero3
    
    if(numero1 < numero2 and numero1 < numero3):
        menor = numero1
    elif(numero2 < numero1 and numero2 < numero3):
        menor = numero2
    elif(numero3 < numero1 and numero3 < numero2):
        menor = numero3
    
    if(numero1 != maior and numero1 != menor):
        meio = numero1
    elif(numero2 != maior and numero2 != menor):
        meio = numero2
    elif(numero3 != maior and numero3 != menor):
        meio = numero3

    print(menor,meio,maior)

#algoritmo que receba três valores A, B e C e verifica se
#eles podem ser os comprimentos dos lados de um triângulo. Se
#forem, mostrar se é um triângulo equilátero, isósceles ou escaleno.
def verificaTriangulo():
    valorA = int(input("Digite o valor de A:"))
    valorB = int(input("Digite o valor de B:"))
    valorC = int(input("Digite o valor de C:"))

    if(valorA < valorB+valorC and valorB < valorA+valorC and valorC < valorB+valorA):
        print("Esses valores formam um triangulo")
    
        if( valorA == valorB and valorA == valorC):
            print("Equilátero\n")
        elif(valorA != valorB and valorA != valorC and valorB != valorC):
            print("Escaleno\n")
        elif(valorA == valorB or valorA == valorC or valorB == valorC):
            print("Isóceles\n")
    else:
        print("Esses valores não formam um triangulo\n")

#algoritmo para resolver equações do 2º grau.
def equacao():
    valorA = float(input("Digite o valor de A != 0:"))
    while valorA == 0:
       valorA = float(input("Digite o valor de A != 0:"))
    valorB = float(input("Digite o valor de B:"))
    valorC = float(input("Digite o valor de C:"))

    delta = valorB**2 - (4*valorA*valorC)

    if(delta < 0):
        print("Não existe raiz real\n")
    elif(delta == 0):
        raizX = (-valorB)/()
        print(f"existe uma raiz real: x={raizX:.2F}\n")
    else:
        import math
        x1 = (-valorB + math.sqrt(delta))/(2*valorA)
        x2 = (-valorB - math.sqrt(delta))/(2*valorA)
        print(f"X1 = {x1:.2F}  X2 = {x2:.2F}\n")

#Uma determinada loja está fazendo promoções de vendas. Qualquer
#compra que um cliente fizer até R$ 100,00 receberá 5% de desconto. Se
#a compra for maior que R$ 100,00, mas inferior a R$ 200,00, o desconto
#será de 10%. Se for superior ou igual a R$ 200,00, o desconto será de 20%.
def notaLoja():
    valorGasto = float(input("Digite o total da compra:"))
    if(valorGasto <= 100):
        desconto = valorGasto*5/100
        print("-=-=-=-=-=LOJA-==-=-=-=-=")
        print(f"Total gasto: {valorGasto}")
        print(f"Total desconto 5%: {desconto} ")
        print(f"Total: {valorGasto - desconto}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    elif(valorGasto > 100 and valorGasto <= 200):
        desconto = valorGasto*10/100
        print("-=-=-=-=-=LOJA-==-=-=-=-=")
        print(f"Total gasto: {valorGasto}")
        print(f"Total desconto 10%: {desconto} ")
        print(f"Total: {valorGasto - desconto}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    elif(valorGasto > 200):
        desconto = valorGasto*20/100
        print("-=-=-=-=-=LOJA-==-=-=-=-=")
        print(f"Total gasto: {valorGasto}")
        print(f"Total desconto 20%: {desconto} ")
        print(f"Total: {valorGasto - desconto}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

#Loop para escolha e teste de cada exercicio
def main():
    option = 1
    while option >= 1:
        menu()
        option = int(input("digite o numero da opção: "))
        if option == 1:
            distancia = int(input("Digite a distancia do Robo: "))
            verificaPonto(distancia)
        elif option == 2:
            print("Em desenvolvimento")
        elif option == 3:
            maiorNumero()
        elif option == 4:
            informaVoto()
        elif option == 5:
            ordemCrescente()
        elif option == 6:
            verificaTriangulo()
        elif option == 7:
            equacao()
        elif option == 8:
            notaLoja()

main()