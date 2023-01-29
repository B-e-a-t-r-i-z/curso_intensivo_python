# EXERCÍCIO 7.1

carro = input("Qual tipo de carro você gostaria de alugar? ")
print(f"Deixe-me ver se consigo um {carro} para você!")

print("#####################################################################")

# EXERCÍCIO 7.2

pessoas = int(input("Mesa pra quantas pessoas? "))

if pessoas > 8:
    print("Por favor aguarde alguns minutos até ser liberda uma mesa para \
vocês.")
else:
    print("Por favor me acompanhe até a sua mesa.")

print("#####################################################################")

# EXERCÍCIO 7.3

numero = int(input("Digite um número: "))

if numero % 10 == 0:
    print("Esse número é multiplo por 10!")
else:
    print("Esse número não é multiplo por 10.")
    
print("#####################################################################")

# EXERCÍCIO 7.4

ingredientes = "Informe os ingredientes para fazer uma pizza, "
ingredientes += "ou digite 'quit' se deseja sair: "
mensagem = ""
while mensagem != "quit":
    mensagem = input(ingredientes)
    if mensagem != "quit":
        print(f"Vamos acrescentar {mensagem} a nossa pizza!")
    
print("#####################################################################")

# EXERCÍCIO 7.5/7.6

idade = int(input("Qual é a sua idade? "))

while idade <= 3:
    print("Seu ingresso é gratuito!")
    break
while idade > 3 and idade <= 12:
    print("O ingresso custa R$ 10,00")
    break
while idade > 12:
    print("O ingresso custa de R$ 15,00")
    break

print("#####################################################################")

# EXERCÍCIO 7.7 - FEITO!

print("#####################################################################")

# EXERCÍCIO 7.8

sandwich_orders = ["x-tudo", "x-salada","x-eggy","x-baccon"]
finished_sandwiches = []

while sandwich_orders:
    preparo = sandwich_orders.pop()
    print("Preparei seu sanduíche de ", preparo.title())
    finished_sandwiches.append(preparo)

print("\nSandwiches preparados: ")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())
    
print("#####################################################################")

# EXERCÍCIO 7.9

sandwich_orders = ["x-tudo","pastrami","x-salada","pastrami","x-eggy",\
"x-baccon","pastrami"]
finished_sandwiches = []

print("infezlismente, mas sem pastrami no momento!!!\n".upper())

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    preparo = sandwich_orders.pop()
    print("Preparei seu sanduíche de ", preparo.title())
    finished_sandwiches.append(preparo)

print("\nsandwiches preparados:".title())
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())

print("#####################################################################")

# EXERCÍCIO 7.10

enquetes = {}
flag = True

while flag:
    pergunta_1 = input("Qual é o seu nome? ")
    pergunta_2 = input("Se pudesse visitar um lugar do mundo, para onde você \
iria? ")
    enquetes[pergunta_1] = pergunta_2
    outra_pessoa = input("Você gostaria que outra pessoa respondesse a \
enquete? (sim/não) ")
    if outra_pessoa == "não":
        flag = False

print("\n--- resultados da enquete---".title())
for pergunta_1, pergunta_2 in enquetes.items():
    print(pergunta_1 + " gostaria de visitar " + pergunta_2 + ".")
