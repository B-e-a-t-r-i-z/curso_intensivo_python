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
