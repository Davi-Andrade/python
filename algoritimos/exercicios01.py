def menu():
    print("\n----MENU----")
    print("1 hello world")
    print("2 Olá {nome}")
    print("3 Multiplique 2 num")
    print("4 Sucessor Antecessor")
    print("5 Media de notas")
    print("6 Calculo expressão")
    print("7 Reajuste salario")
    print("0 Sair")
    print("---------------\n")

def verifyContinue():
    print("\nDeseja continuar?")
    print("1 - SIM")
    print("0 - NÃO")
    return int(input())

option = 1
while option >= 1:
    menu()
    option = int(input("Digite o numero da opção: "))

    if option == 1:
        print("Hello world")
        option = verifyContinue()
    elif option == 2:
        nome = input("Digite seu nome: ")
        print(f"Olá {nome}\n")
        option = verifyContinue()
    elif option == 3:
        numero1 = int(input("numero 1:"))
        numero2 = int(input("numero 2:"))
        print(f"{numero1} x {numero2} = {numero1*numero2}" )
        option = verifyContinue()
    elif option == 4:
        numero = int(input("Digite o numero:"))
        print(f"Antecessor {numero-1} Sucessor {numero+1}")
        option = verifyContinue()
    elif option == 5:
        nota1 = float(input("Digite a nota 1: "))
        nota2 = float(input("Digite a nota 2: "))
        media = ((nota1*0.6)+(nota2*0.4))/2
        print(f"Media ponderada é {media}")
        option = verifyContinue()
    elif option == 6:
        valor_x = int(input("Digite o valor de X:"))
        valor_y = int(input("Digite o valor de Y:"))
        valor_z = (valor_x**2 + valor_y**2)/(valor_x-valor_y)**2
        print(f"Valor de Z = {valor_z}")
        option = verifyContinue()
    elif option == 7:
        salario = float(input("Digite seu salario:"))
        aumento = salario * 25 / 100
        print(f"O reajuste é {aumento} o salario agora é {salario+aumento}")
        option = verifyContinue()
print("\nAté Logo!")
