#ProcessamentoDeDados
import sys
def soma(a,b):
    return a+b
def sub (a,b):
    return a-b
def div(a,b):
    return a/b
def mult(a,b):
    return a*b

def calc():
    
    print("Bem vindo!")
    print("Essa é uma calculadora programada em python com o objetivo de aprendizado.")
    print("Para prosseguir selecione uma das opções abaixo:")
    print("1.Somar.\n2.Subtrair.\n3.Dividir\n4.Multiplicar.")
    while True:
        try:
            escolha = int(input("Escolha uma opção com o número inteiro: "))
            if escolha == 1:
                entrada = float(input("Digite o primeiro número: "))
                entrada2 = float(input("Digite o segundo número: "))
                resultado = soma(entrada,entrada2)
                print("Resultado: ", resultado)
                break
            elif escolha == 2:
                entrada = float(input("Digite o primeiro número: "))
                entrada2 = float(input("Digite o segundo número: "))
                resultado = sub(entrada,entrada2)
                print("Resultado:", resultado)
                break
            elif escolha == 3:
                entrada = float(input("Digite o primeiro número: "))
                entrada2 = float(input("Digite o segundo número: "))
                resultado = div(entrada,entrada2)
                print("Resultado:", resultado)
                break
            elif escolha == 4:
                entrada = float(input("Digite o primeiro número: "))
                entrada2 = float(input("Digite o segundo número: "))
                resultado = mult(entrada,entrada2)
                print("Resultado:", resultado)
                break
            else:
                print("Código inválido.")

        except ValueError:
            print("Resposta inválida!\nRetornando opção da escolha de função..")

#SaídaDosDados
def main():
    
    while True:
        calc()
        
        continuar = input("Deseja calcular novamente? (S/n): ").strip().lower()

        if continuar == "n":
            print("Obrigado por usar esta calculadora!\nAté a próxima!")
            sys.exit()
main()

