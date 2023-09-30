# EXERCÍCIO 10.1
'''
filename = "learning_python.txt"

with open(filename) as file_object:
     lines = file_object.readlines()
     
for line in lines:
    print(line.rstrip())
    
print("######################################################################")

#EXERCÍCIO 10.2

filename = "learning_python.txt"

with open(filename) as file_object:
     lines = file_object.readlines()
     
for line in lines:
    print(line.replace("Python", "C").rstrip())

print("######################################################################")

#EXERCÍCIO 10.3
filename = 'guest.txt'
nome = input("Qual é o seu nome? ")

with open(filename, 'a') as file_object:
    file_object.write(nome)

print("######################################################################")

#EXERCÍCIO 10.4

filename = "guest_book.txt"
resposta = True
while resposta:
    pergunta1 = input("\nQual é o seu nome de usuário? ")
    print("\nOlá! Seja bem-vindo(a)!!! " + pergunta1)
    pergunta2 = input("\nDeseja inserir um novo usuário?(sim ou não) ")
    
    with open(filename, "a") as file_object:
        file_object.write(pergunta1 + "\n")
        
    if pergunta2 == "não":
        resposta = False

print("######################################################################")

#EXERCÍCIO 10.5

filename = "pqamamosprogramacao.txt"

while True:
    pergunta_1 = input("\nPor que você amar programar? ")
    pergunta_2 = input("\nDeseja perguntar a outra pessoa? (s ou n) ")
    
    with open(filename, "a") as file_object:
        file_object.write(pergunta_1 + "\n")
        
    if pergunta_2 == "n":
        break

print("######################################################################")

#EXERCÍCIO 10.6

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    resultado = num1 + num2

    print("A soma é igual a " + str(resultado))

except ValueError:
    print("Opa! Parece que você inseriu algum número válido. Tente novamente!")

print("######################################################################")

#EXERCÍCIO 10.7
'''

    
    
    






