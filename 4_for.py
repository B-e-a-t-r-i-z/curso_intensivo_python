#EXERCÍCIO 4.1

pizzas=["calabresa","frango com catupiry","meio a meio"]
for pizza in pizzas:
	print("Gosto de pizza de " + pizza.title() + ".\n")
print("Eu realmente gosto de pizza!!!")

print("################################################")

#EXERCÍCIO 4.2

animais=["leão","onça","leopardo","tigre"]
for animal in animais:
	print("Um animal realmente perigoso é a/o: " + animal.title())
print("\n" + "E todos esses animais são felinos!!!")

print("################################################")

#EXERCÍCIO 4.3

for valores in range(1,21):
	print(valores)

print("################################################")

'''EXERCÍCIO 4.4 <<----NÚMERO MUITO GRANDE! bloco de código desabilitado temporariamente, PARA DESBLOQUEAR SELECIONAR E CTRL+E
numeros=list(range(1,1000001))
for numeros in list(range(1,1000001)):
    print(numeros)'''

print("################################################")

#EXERCÍCIO 4.5

number=list(range(1,1000001))
print(min(number))
print(max(number))
print(sum(number))

print("################################################")

#EXERCÍCIO 4.6

pares=list(range(1,21,2))
for numeros_pares in pares:
	print(numeros_pares)

print("################################################")

#EXERCÍCIO 4.7

três=list(range(3,30,3))
for numero_três in três:
	print(numero_três) 

print("################################################")

#EXERCÍCIO 4.8

resultados=[]
for cubo in range(1,11):
	resultado=cubo**3
	resultados.append(resultado)
print(resultados)

print("################################################")

#EXERCÍCIO 4.9

list_comprehension = [valor**3 for valor in range(1,11)]
print(list_comprehension) 

print("################################################")

#EXERCÍCIO 4.10

animais=["leão","onça","leopardo","tigre","leoa"]
print("Os três primeiros itens da lista são:")
for animal in animais[0:3]:
	print(animal.title())
print("Três itens do meio da lista são:")
for animal in animais[1:-1]:
	print(animal.title())
print("Os três últimos itens da lista são:")
for animal in animais[-3:]:
	print(animal.title())

print("################################################")

#EXERCÍCIO 4.11

pizzas=["calabresa","frango com catupiry","meio a meio"]

friend_pizza=pizzas[:]
pizzas.append("calacatu")
friend_pizza.append("portuguesa")

print("Minhas pizzas favoritas são:")
for sabores in pizzas[:1]:
	print(pizzas)

print("\n"+"As pizzas favoritas de meu amigo são:")
for amigo in friend_pizza[:1]:
	print(friend_pizza)

print("################################################")

#EXERCÍCIO 4.12

my_foods = ["pizza","falafel","carrot cake"]

friend_foods=my_foods[:]
my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
for comida in my_foods[:1]:
	print(my_foods)

print("\n"+"My friend's favorite foods are:")
for amigo_comida in friend_foods[:1]:
	print(friend_foods)

print("################################################")

#EXERCÍCIO 4.13

cardapios=("strogonoff","lasanha","picanha","brigadeiro","beijinho")
print("Esse é o cardapio do restaurante: ")
for cardapio in cardapios:
	print(cardapio)

print("\nO cardapio original é: ")
for cardapio in cardapios:
	print(cardapio)

cardapios=("arroz","feijão","carne_cozida","pudim","bolo")
print("\nNovo cardapio:")
for cardapio in cardapios:
	print(cardapio)

print("################################################")

#EXERCÍCIO 4.14
