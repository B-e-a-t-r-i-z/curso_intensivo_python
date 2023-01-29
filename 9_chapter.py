#EXERCÍCIO 9.1

class Restaurant():
    """Primeira tentativa da criação de uma classe."""
    def __init__(self,restaurant_name,cuisine_type):
        """Atributos da classe Restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Descrição do Restaurant"""
        print("O nome do meu restaurante é ",self.restaurant_name.title())
        print("Meu tipo de cozinha é ",self.cuisine_type.title())
        
    def  open_restaurant(self):
        """Mensagem informando se o restaurante está aberto ou não."""
        print("O ",self.restaurant_name.title(), "está aberto agora!!!" )
    
my_restaurant = Restaurant("bia's food","brazilian food")

my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()


print("#####################################################################")

#EXERCÍCIO 9.2

restaurant_maria = Restaurant("restaurante da dona maria","comida bahiana")
restaurant_marcos = Restaurant("cantinho do marcos","gaúcha")
restaurant_lucas = Restaurant("rio's food","carioca")
print("\nO nome do restaurante é",restaurant_maria.restaurant_name.title())
print("O tipo de cozinha é",restaurant_maria.cuisine_type.title())

print("\nO nome do restaurante é",restaurant_marcos.restaurant_name.title())
print("O tipo de cozinha é",restaurant_marcos.cuisine_type.title())

print("\nO nome do restaurante é",restaurant_lucas.restaurant_name.title())
print("O tipo de cozinha é",restaurant_lucas.cuisine_type.title())

print("#####################################################################")

#EXERCÍCIO 9.3

class User():
    """Criar uma classe para o usuário."""
    def __init__(self,first_name,last_name,idade,cpf,email,senha):
        """Atributos da classe User."""
        self.first_name = first_name
        self.last_name = last_name
        self.idade =idade
        self.cpf = cpf
        self.email = email
        self.senha = senha
        
    def describe_user(self):
        """Resumo das informações do usuário."""
        print("Primeiro nome: "+self.first_name.title())
        print("Último nome: "+self.last_name.title())
        print("Idade: "+self.idade)
        print("CPF: "+self.cpf)
        print("E-mail: "+self.email)
        print("Senha: "+self.senha)
        
    def  greet_user(self):
        """Mensagem de cumprimento para o usuário."""
        print("Cadastro finalizado!\nBem-vindo(a) ",self.first_name.title(),\
        "\n")
    
usuario_1 = User("Beatriz","Almeida","22","000.000.000-00",\
"beatriz.almeida@gmail.com","almeidabia")
usuario_2 = User("Anna","Silva","20","000.000.000-00","ana.silva@gmail.com",\
"anaSilva")
usuario_3 = User("Pedro","Souza","21","000.000.000-00","pedro@gmail.com",\
"pedrolegal")

usuario_1.greet_user()
usuario_1.describe_user()
print("\n")
usuario_2.greet_user()
usuario_2.describe_user()
print("\n")
usuario_3.greet_user()
usuario_3.describe_user()

print("#####################################################################")

#EXERCÍCIO 9.4

class Restaurant():
    """Primeira tentativa da criação de uma classe."""
    def __init__(self,restaurant_name,cuisine_type):
        """Atributos da classe Restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served = 0
        
    def describe_restaurant(self):
        """Descrição do Restaurant"""
        print("O nome do meu restaurante é "+ self.restaurant_name.title())
        print("Meu tipo de cozinha é "+ self.cuisine_type.title())
        
    def  open_restaurant(self):
        """Mensagem informando se o restaurante está aberto ou não."""
        print("O "+self.restaurant_name.title()+ "está aberto agora!!!" )
    
    def numero_servido(self):
        """Números servidos."""
        print("Os pedidos atendidos são de: "+ str(self.number_served))
        
    def set_number_served(self,pedidos):
        """Definir o número de clientes atendidos."""
        self.number_served = pedidos
        
        
    def increment_number_served(self,clientes):
        """Incrementar o número de clientes servidos."""
        self.number_served += clientes
        
restaurant = Restaurant("bia's food","brazilian food")

restaurant.open_restaurant()
restaurant.describe_restaurant()

restaurant.numero_servido()#Acrescente um atributo chamado number_served cujo \
#valor default é 0.

restaurant.set_number_served(23)#Adicione um método chamado \
#set_number_served() que permita definir o número de clientes atendidos
restaurant.numero_servido()

restaurant.increment_number_served(100)#Acrescente um método chamado \
#increment_number_served() que permita incrementar o n° de clientes servidos. 
restaurant.numero_servido()

print("#####################################################################")

#EXERCÍCIO 9.5

class User():
    """Criar uma classe para o usuário."""
    def __init__(self,first_name,last_name,idade,cpf,email,senha,\
    login_attempts = 0):
        """Atributos da classe User."""
        self.first_name = first_name
        self.last_name = last_name
        self.idade =idade
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.login_attempts = login_attempts
        
    def describe_user(self):
        """Resumo das informações do usuário."""
        print("Primeiro nome: "+self.first_name.title())
        print("Último nome: "+self.last_name.title())
        print("Idade: "+self.idade)
        print("CPF: "+self.cpf)
        print("E-mail: "+self.email)
        print("Senha: "+self.senha)
        
    def  greet_user(self):
        """Mensagem de cumprimento para o usuário."""
        print("Cadastro finalizado!\nBem-vindo(a) ",self.first_name.title(),\
        "\n")
        
    def increment_login_attempts(self):
        """Incremente o valor de login_attempts em 1."""
        self.login_attempts += 1
        
    def  reset_login_attempts(self):
        """Reinicie o valor de login_attempts com 0 """
        self.login_attempts -= self.login_attempts    
        print("Resertado, o números de login é de: "+ str(self.login_attempts))
           
usuario_1 = User("Beatriz","Almeida","22","000.000.000-00",\
"beatriz.almeida@gmail.com","almeidabia")
usuario_2 = User("Anna","Silva","20","000.000.000-00","ana.silva@gmail.com",\
"anaSilva")
usuario_3 = User("Pedro","Souza","21","000.000.000-00","pedro@gmail.com",\
"pedrolegal")

usuario_1.greet_user()
usuario_1.describe_user()
usuario_1.increment_login_attempts()
print("O números de login é de: "+ str(usuario_1.login_attempts))
usuario_1.reset_login_attempts()

print("\n")

usuario_2.greet_user()
usuario_2.describe_user()

print("\n")

usuario_3.greet_user()
usuario_3.describe_user()
usuario_3.increment_login_attempts()
usuario_3.increment_login_attempts()
usuario_3.increment_login_attempts()
usuario_3.increment_login_attempts()
print("O números de login é de: "+ str(usuario_3.login_attempts))
usuario_1.reset_login_attempts()

print("#####################################################################")

#EXERCÍCIO 9.6

class Restaurant():
    """Primeira tentativa da criação de uma classe."""
    def __init__(self,restaurant_name,cuisine_type):
        """Atributos da classe Restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served = 0
        
    def describe_restaurant(self):
        """Descrição do Restaurant"""
        print("O nome do meu estabelecimento é "+ self.restaurant_name.title())
        print("Meu especialização é "+ self.cuisine_type.title())
        
    def  open_restaurant(self):
        """Mensagem informando se o restaurante está aberto ou não."""
        print("O "+self.restaurant_name + " está aberto agora!!!" )
    
    def numero_servido(self):
        """Números servidos."""
        print("Os pedidos atendidos são de: "+ str(self.number_served))
        
    def set_number_served(self,pedidos):
        """Definir o número de clientes atendidos."""
        self.number_served = pedidos
        
        
    def increment_number_served(self,clientes):
        """Incrementar o número de clientes servidos."""
        self.number_served += clientes

class IceCreamStand(Restaurant):
    """Criação de uma classe-filha."""
    def __init__(self,restaurant_name,cuisine_type,flavors=" "):
        """Armazenar uma lista de sabores de sorvete"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors 
    def sabores(self):
        """Lista de sabores dos sorvetes."""
        self.sabores = self.flavors
        lista = ["maracuja","chocolate","morango"]
        print("Lista de sabores: "+ str(lista))

sorveteria = IceCreamStand("bia's Sorvetes","sorvetes")

sorveteria.open_restaurant()
sorveteria.describe_restaurant()
sorveteria.sabores()

print("#####################################################################")

#EXERCÍCIO 9.7

class User():
    """Criar uma classe para o usuário."""
    def __init__(self,first_name,last_name,idade,cpf,email,senha,\
    login_attempts = 0):
        """Atributos da classe User."""
        self.first_name = first_name
        self.last_name = last_name
        self.idade =idade
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.login_attempts = login_attempts
        
    def describe_user(self):
        """Resumo das informações do usuário."""
        print("Primeiro nome: "+self.first_name.title())
        print("Último nome: "+self.last_name.title())
        print("Idade: "+self.idade)
        print("CPF: "+self.cpf)
        print("E-mail: "+self.email)
        print("Senha: "+self.senha)
        
    def  greet_user(self):
        """Mensagem de cumprimento para o usuário."""
        print("Cadastro finalizado!\nBem-vindo(a) ",self.first_name.title(),\
        "\n")
        
    def increment_login_attempts(self):
        """Incremente o valor de login_attempts em 1."""
        self.login_attempts += 1
        
    def  reset_login_attempts(self):
        """Reinicie o valor de login_attempts com 0 """
        self.login_attempts -= self.login_attempts    
        print("Resertado, o números de login é de: "+ str(self.login_attempts))
           
usuario_1 = User("Beatriz","Almeida","22","000.000.000-00",\
"beatriz.almeida@gmail.com","almeidabia")
usuario_2 = User("Anna","Silva","20","000.000.000-00","ana.silva@gmail.com",\
"anaSilva")
usuario_3 = User("Pedro","Souza","21","000.000.000-00","pedro@gmail.com",\
"pedrolegal")

usuario_1.greet_user()
usuario_1.describe_user()
usuario_1.increment_login_attempts()
print("O números de login é de: "+ str(usuario_1.login_attempts))
usuario_1.reset_login_attempts()

print("\n")

usuario_2.greet_user()
usuario_2.describe_user()

print("\n")

usuario_3.greet_user()
usuario_3.describe_user()
usuario_3.increment_login_attempts()
usuario_3.increment_login_attempts()
usuario_3.increment_login_attempts()
usuario_3.increment_login_attempts()
print("O números de login é de: "+ str(usuario_3.login_attempts))
usuario_3.reset_login_attempts()

class Admin(User):
    def __init__(self,first_name,last_name,idade,cpf,email,senha,privileges = \
    " ",login_attempts = 0):
        super().__init__(first_name,last_name,idade,cpf,email,senha,\
        login_attempts = 0)
        self.privileges = privileges
    def show_privileges(self):
        """"Listar os privilégios de um administrador."""
        self.show_privileges = self.privileges
        lista = ["can add post","can delete post", "can ban user"]
        print("Os privilégios de um adminstrador são:" + str(lista))

admin_1 = Admin ("Izuku","Midorya","18","000.000.000-00","deku@gmail.com",\
"allmight4Ever")

print("\n")

admin_1.greet_user()
admin_1.describe_user()
admin_1.increment_login_attempts()
admin_1.increment_login_attempts()
admin_1.increment_login_attempts()
admin_1.increment_login_attempts()
print("O números de login é de: "+ str(admin_1.login_attempts))
usuario_1.reset_login_attempts()
admin_1.show_privileges()

print("#####################################################################")

#EXERCÍCIO 9.8

class Privileges(Admin):
    def __init__(self,show_privileges,privileges):
        super().__init__(show_privileges)
        self.privileges = []
    def show(self):
        lista = ["a","b", "c"]
        print("Os privilégios de um adminstrador são:" + str(lista))
                
admin_2 = Privileges

admin_2.show("")

print("#####################################################################")

#EXERCÍCIO 9.9 #FAZER DEPOIS!!!

print("#####################################################################")

#EXERCÍCIO 9.10

from restaurant import*

teste1 = IceCreamStand ("sorvetes de teste", "sabor teste")
print("\n")
teste1.open_restaurant()
teste1.describe_restaurant()
teste1.sabores()

print("#####################################################################")

#EXERCÍCIO 9.11

from import_admin import Admin

testando = Admin("Katsuki","Bakugou","19","123.000.123-00","kachan@gmail.com",\
"DieEE")

testando.show_privileges()

print("#####################################################################")

#EXERCÍCIO 9.12

from import_user import User
from import_admin_2 import Admin#tem que fazer a importação do User no arquivo.

testando2 = Admin("Katsuki","Bakugou","19","123.000.123-00","kachan@gmail.com",\
"DieEE")

testando2.show_privileges()

print("#####################################################################")

#EXERCÍCIO 9.13

from collections import OrderedDict

glossario = OrderedDict()

glossario["chapter_1"] = "numbers"
glossario["chapter_2"] = "names_cases"
glossario["chapter_3"] = "list"
glossario["chapter_4"] = "for"
glossario["chapter_5"] = "if"
glossario["chapter_6"] = "dicionário"
glossario["chapter_7"] = "while"
glossario["chapter_8"] = "funções"
glossario["chpater_9"] = "classes"
glossario["chapter_10"] = "arquivos"   

for key, value in glossario.items():
    print("No " + key.title() + " estudamos " +value.title() + "!")

print("#####################################################################")

#EXERCÍCIO 9.14 - FAZER OUTRA HORA!!!
'''
class Die():
	"""capitulo 9, exercício 14"""
	def __init__(self,sides=6):
		"""função."""
		self.sides = sides
	
	def roll_die(self):
		from random import randint
		x = randint(1, self.sides)
		print(x)
        
    def dado_6():
        from random import randint
        for i in range(6):
            list.append(i)
            print(list)
    
		
dado = Die()

dado.roll_die()
dado.dado6()
'''
print("#####################################################################")

#EXERCÍCIO 9.15 - FEITO!
