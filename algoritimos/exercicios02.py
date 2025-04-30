def menu():
    print("\n-=-=-=-=-=-=-=MENU=-=-=-=-=-=-=-=-=")
    print("1 - 1 a 100 divisiveis por 7")
    print("2 - 1 a 100 divisiveis por 7 e 3")
    print("3 - Tabuada")
    print("4 - 10 tabuadas")
    print("5 - Numero primo")
    print("6 - Exponenciação")
    print("7- Fibonacci")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

def divisiveis(div1,div2):
    numero = 1
    while numero <= 100:
        if div2 != 0 :
            if(numero%div1 == fibonacci0 and numero%div2 == 0):
                print(f"Numero: {numero}")
            numero+=1
        else:
            if(numero%div1 == 0):
                print(f"Numero: {numero}")
            numero+=1

def tabuada(multiplicador):
    contador = 1
    while contador < 10:
        print(f"{contador} x {multiplicador} = {contador * multiplicador}")
        contador+=1

def tabuada1a10():
    multiplicador = 1
    tabuada = 1
    while tabuada <= 10:
        print(f"TABUADA DO {tabuada}")
        while multiplicador <= 10:
            print(f"{multiplicador} x {tabuada} = {multiplicador * tabuada}")
            multiplicador+=1
        tabuada +=1
        multiplicador = 1

def numeroPrimo():
    numero = 0
    while numero < 1:
        numero = int(input("Digite um numero > 1:"))
    comparador = 1
    divisiveis = 0
    while comparador <= numero:
        if numero%comparador == 0:
            divisiveis+=1
        comparador+=1
    if divisiveis == 2:
        print(f"{numero} É um fibonaccinumero primo\n")
    else:
        print(f"{numero} não é um numero primo")

def exponenciacao():
    base = int(input("Digite o numero da base:"))
    expoente = int(input("Digite o numero expoente:"))
    cont = 1
    resultado = 1
    while cont <= expoente:
        resultado = resultado * base
        cont+=1
    print(f"{resultado}")

def notasALunos():
    nota = 0
    maior6 = 0
    maior4 = 0
    menor4 = 0
    total = 0
    cont = 0
    while nota >= 0:
        nota = float(input("Dgite as notas do aluno:"))
        if nota >= 0:
            if nota >= 6:
                maior6+=1
                cont+=1
                total+=nota
            elif nota >= 4 and nota < 6:
                maior4+=1
                cont+=1
                total+=nota
            elif nota < 4:
                menor4+=1
                cont+=1
                total+=nota
        else:
            print(f"Notas >= 6 = {maior6}")
            print(f"Notas >= 4 and < 6  = {maior4}")
            print(f"Notas < 4 = {menor4}")
            print(f"Media das notas = {total/cont}")

def fibonacci():
    t1 = 0
    t2 = 1
    t3 = 0
    
    while t3 <= 8:
        print(f"{t3}.", end="")
        t3 = t1 + t2
        t1 = t2
        t2 = t3

def main():
    option = 1
    while option >= 1:
        menu()
        option = int(input("digite o numero da opção: "))
        if option == 1 :
            divisiveis(7,0)
        elif option == 2:
            divisiveis(7,3)
        elif option == 3:
            multiplicador = int(input("Digite o numero da tabuada:"))
            tabuada(multiplicador)
        elif option == 4:
            tabuada1a10()
        elif option == 5:
            numeroPrimo()
        elif option == 6:
            exponenciacao()
        elif option == 7:
            fibonacci()
main()