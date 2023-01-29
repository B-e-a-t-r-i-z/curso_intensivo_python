# EXERCÍCIO 3.1

names=['Thainara','Davison','Isabel']
print(names[0])
print(names[1])
print(names[2])

print('#######################################')

# EXERCÍCIO 3.2

print("Olá "+names[0].title()+" vamos ir no shopping ?")
print("Olá "+names[1].title()+" vamos ir no shopping ?")
print("Olá "+names[2].title()+" vamos ir no shopping ?")

print('#######################################')

# EXERCÍCIO 3.3

transportes=['bike','trem']
print("Gostaria de pintar a minha "+transportes[0]+"!")
print("Quando vou para a cidade prefero ir de "+transportes[1]+"! kkk")

print('#######################################')

# EXERCÍCIO 3.4

convidados=['comandante spook','capitão jim','tenente urura']
print("Boa noite "+convidados[0].title()+"!"+" gostaria de ir jantar hoje ?")
print("Ei! "+convidados[1].title()+" !!!"+" Quer ir jantar comigo hoje?")
print("Oi "+convidados[2].title()+" vamos ir jantar hoje?")

print('#######################################')

# EXERCÍCIO 3.5

convidados[0]="Doutor Bones"
print(convidados[0].title()+" quer vir jantar hoje?")
print(convidados[1].title()+" quer vir jantar hoje?")
print(convidados[2].title()+" quer vir jantar hoje?")

print('#######################################')

# EXERCÍCIO 3.6

convidados.insert(0,"luffy")
convidados.insert(3,"zoro")
convidados.append("sanji")
print(convidados[0].title()+" quer vir jantar hoje?")
print(convidados[1].title()+" quer vir jantar hoje?")
print(convidados[2].title()+" quer vir jantar hoje?")
print(convidados[3].title()+" quer vir jantar hoje?")
print(convidados[4].title()+" quer vir jantar hoje?")
print(convidados[5].title()+" quer vir jantar hoje?")

print('#######################################')

# EXERCÍCIO 3.7

print("Informamos que infelismente somente duas pessoas poderam vir jantar \
hoje")
convidados.pop()
print("Sanji, sinto muito pelo transtorno!!! mas, hoje não vou poder jantar \
com você")
convidados.pop()
print("Tenente Uhura, sinto muito pelo transtorno!!! mas, hoje não vou poder \
jantar com você")
convidados.pop()
print("Zoro, sinto muito pelo transtorno!!! mas, hoje não vou poder jantar \
com você")
convidados.pop()
print("Capitão Jim, sinto muito pelo transtorno!!! mas, hoje não vou poder \
jantar com você")
print(convidados[0].title()+" você ainda está convidado para vir jantar aqui\
!!!")
print(convidados[1].title()+" você ainda está convidado para vir jantar aqui\
!!!")

print('#######################################')

#EXERCÍCIO 3.8

lugares=["Itália","Japão","Horlanda","Campos do Jordão","Londres"]
print(lugares)
print(sorted(lugares))
print(lugares)
reversed(lugares)
print(lugares)
reversed(lugares)
print(lugares)
lugares.sort()
print(lugares)
lugares.sort(reverse=True)
print(lugares)

print('#######################################')

#EXERCÍCIO 3.9

print(len(convidados))

print('#######################################')

#EXERCÍCIO 3.11

print(convidados[0])

print('#######################################')

