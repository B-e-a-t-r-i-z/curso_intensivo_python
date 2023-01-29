from import_user import User

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

