#EXERCÍCIO 5.3

alien_color = ["green"]
if "green" in alien_color:
    print("Uhuuuuu!! Você acabou de ganhar 5 pontos!!!")

if "yellow" in alien_color:
    print("Buuuuhhhh, que pena não foi dessa vez..")
    
print("######################################################################")

#EXERCÍCIO 5.4
alien_color = "red"
if alien_color == "green":
    print("Uhuuuuu! Você acabou de ganhar 5 pontos por atingir o alienígena!")
else:
    print("Uhuuuuu! Você acabou de ganhar 10 pontos por atingir o alienígena!")

alien_color = "green"
if alien_color == "green":
    print("Uhuuuuu! Você acabou de ganhar 5 pontos por atingir o alienígena!")
else:
    print("Uhuuuuu! Você acabou de ganhar 10 pontos por atingir o alienígena!")

print("######################################################################")

#EXERCÍCIO 5.5

alien_color = "green"
if alien_color == "green":
    print("Parabéns! Você ganhou 5 pontos!!!")
elif alien_color == "yellow":
    print("Parabéns! Você ganhou 10 pontos!!!")
else:
    print("Parabéns! Você ganhou 15 pontos!!!")
    
alien_color = "yellow"
if alien_color == "green":
    print("Parabéns! Você ganhou 5 pontos!!!")
elif alien_color == "yellow":
    print("Parabéns! Você ganhou 10 pontos!!!")
else:
    print("Parabéns! Você ganhou 15 pontos!!!")

alien_color = "red"
if alien_color == "green":
    print("Parabéns! Você ganhou 5 pontos!!!")
elif alien_color == "yellow":
    print("Parabéns! Você ganhou 10 pontos!!!")
else:
    print("Parabéns! Você ganhou 15 pontos!!!")

print("######################################################################")

#EXERCÍCIO 5.6

age = 22
if age < 2:
    print("Aww..você é um bebê!")
elif age == 2 or age <= 4:
    print("Você ja é uma criança!!")
elif age == 4 or age <= 13:
    print("Como você cresceu! Já é uma garota!!!")
elif age == 13 or age <= 20:
    print("Nossa, você já é uma adolecente!")
elif age == 20 or age <= 65:
    print("Olha só..você já é um adulta!!")
else:
    print("Uau..você já é uma idosa..")

print("######################################################################")

#EXERCÍCIO 5.7

favorite_fruts = ["kiwi","melancia","abacaxi"]
if "abacaxi" in favorite_fruts:
    print("Você realmente gosta de Abacaxi!")
if "kiwi" in favorite_fruts:
    print("Você realmente gosta de Kiwi!")
if "melancia" in favorite_fruts:
    print("Você realmente gosta de Melancia!")
if "banana" in favorite_fruts:   
    print("Você realmente gosta de Banana!") 
if "laranja" in favorite_fruts:
    print("Você realmente gosta de Laranja!")

print("######################################################################")

#EXERCÍCIO 5.8/5.9

nomes = ['beatriz','mateus','josé','sheila','isolina','admin']
if nomes:
    for nome in nomes:
        if nome == 'admin':
            print("Olá Admin, gostaria de ver um relatório de status?")
        else:
            print("Olá " + nome.title() + " obrigado por fazer login novamente\
.")
else:
    print("Precisamos encontrar alguns usuários!")

print("######################################################################")

#EXERCÍCIO 5.9

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".") 
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?") 

print("######################################################################")

#EXERCÍCIO 5.10

current_users = ["mariana","ana","vitor","hector","marcia"]
new_users = ["VITOR","jack","Hector","marcia","ANA"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Nome de usuário indisponível, tente outro")
    else:
        print("Nome de usuário disponível. Bem-vindo(a)!!!")
    
print("######################################################################")

#EXERCÍCIO 5.11

numeros = ["1","2","3","4","5","6","7","8","9"]
for numero in numeros:
    if numero == "1":
        print("1st")
    elif numero == "2":
        print("2nd")
    elif numero == "3":
        print("3rd")
    else:
        print(numero + "th")

print("######################################################################")

#EXERCÍCIO 12/13 feitos!

print("######################################################################")

