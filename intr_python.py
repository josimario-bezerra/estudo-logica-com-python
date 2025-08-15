# introducao_python.py
# Este é um exemplo básico em Python para demonstrar a estrutura mínima de um programa
# e apresentar alguns conceitos iniciais.

# Imprimir uma mensagem na tela
print("Olá! Este é meu primeiro programa em Python 🐍")

# Pedir informações ao usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (em metros): "))

print("\n📌 Informações cadastradas:")
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura, "m")

#Estrutura condicional
if idade >= 18:
    print("\nVocê é maior de idade.")
else:
    print("\nVocê é menor de idade.")


