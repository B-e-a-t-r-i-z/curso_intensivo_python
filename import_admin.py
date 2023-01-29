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

class Privileges(Admin):
    def __init__(self,show_privileges,privileges):
        super().__init__(show_privileges)
        self.privileges = []
    def show(self):
        lista = ["a","b", "c"]
        print("Os privilégios de um adminstrador são:" + str(lista))
                



