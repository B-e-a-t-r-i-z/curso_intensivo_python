import printing_functions 
from pizzas import *

print("######################################################################")

# EXERCICÍO 8.1

def display_message():
    """Exibe qual matéria estou estudando."""
    print("No momento estou estudando Funções !")

display_message() 
   
print("######################################################################")

#EXERCICÍO 8.2

def favorite_book(livro):
    """"Exibe meu livro favorito!!!"""
    print("Meu livro favorito é...", livro.title(),"!!!")

favorite_book("house of night")
    
print("######################################################################")

#EXERCICÍO 8.3

def make_shirt(estampa,tamanho):
    """Exibi insformações da camisa."""
    print("Estampa: ",estampa , "\nTamanho: ",tamanho)

make_shirt("I love Python","G\n")
make_shirt(tamanho="P",estampa="Python <3")

print("######################################################################")

#EXERCICÍO 8.4

def make_shirt(estampa,tamanho="g"):
    """Exibi insformações da camisa."""
    print("Estampa: ",estampa.title() , ". Tamanho: ",tamanho.title())

make_shirt(estampa = "eu amo python")
print("----------------------------------------------------------------------")

def make_shirt(tamanho,estampa="estou programando python"):
    """Exibi insformações da camisa."""
    print("Estampa: ",estampa.title(),". Tamanho: ",tamanho.title())

make_shirt(tamanho = "g")
make_shirt(tamanho = "m")
print("----------------------------------------------------------------------")

def make_shirt(tamanho,estampa="python->python--->>pythonnn"):
    """Exibi insformações da camisa."""
    print("Estampa: ",estampa.upper(),". Tamanho: ",tamanho.title())

make_shirt(tamanho = "p")

print("######################################################################")

#EXERCICÍO 8.5

def describe_city(cidade,pais="brasil"):
    """"Exibir cidades com o seu país."""
    print("A cidade do", cidade.title(), "está localizada no", pais.title())

describe_city (cidade = "rio de janeiro")
describe_city (cidade = "rio grande do sul")
describe_city (cidade = "alasca", pais = "e.u.a")
    
print("######################################################################")

#EXERCICÍO 8.6

def cidade_pais (cidade,pais):
    """Exibir as cidades e seus paises."""
    locais = cidade + ", " + pais
    return locais.title()
    
lugares = cidade_pais(cidade = "são paulo", pais = "brasil")
print(lugares)

print("----------------------------------------------------------------------")

def cidade_pais (cidade,pais):
    """Exibir as cidades e seus paises."""
    locais = cidade + ", " + pais
    return locais.title()
    
lugares = cidade_pais(cidade = "buenos aires", pais = "argentina")
print(lugares)

print("----------------------------------------------------------------------")

def cidade_pais (cidade,pais):
    """Exibir as cidades e seus paises."""
    locais = cidade + ", " + pais
    return locais.title()
    
lugares = cidade_pais(cidade = "londres", pais = "inglaterra")
print(lugares)

print("######################################################################")

#EXERCICÍO 8.7

def make_album(artista,album):
    """Devolver um dicionario sobre música."""
    informacoes = {"artista": artista, "album": album}
    return informacoes
    
rock = make_album("System of a down", "hypnotize")   
print(rock)

print("----------------------------------------------------------------------")

def make_album(artista,album):
    """Devolver um dicionario sobre música."""
    informacoes = {"artista": artista, "album": album}
    return informacoes
    
rock = make_album("linkin park", "in the end")   
print(rock)

print("----------------------------------------------------------------------")

def make_album(artista,album,faixa=""):
    """Devolver um dicionario sobre música."""
    informacoes = {"artista": artista, "album": album}
    if faixa: informacoes["faixa"] = faixa
    return informacoes
    
rock = make_album("decode", "paramore", "55")   
print(rock)

print("######################################################################")

#EXERCICÍO 8.8

def make_album(artista,album,faixa=""):
    """Devolver um dicionario sobre música."""
    informacoes = {"artista": artista, "album": album}
    if faixa: informacoes["faixa"] = faixa
    return informacoes.title()
while True:
    print("Preencha as informacões sobre a música")
    print("(Precione 'q' qualquer momento para sair do looping!)")
    artista = input("\nQuem é o artista da música? ")
    if artista == 'q':
        break
    album = input("Qual é o álbum da música? ")
    if album == 'q':
        break

print("######################################################################")

#EXERCICÍO 8.9

def show_magicians(magicos):
    """Passar uma lista de mágicos para uma função"""
    for magico in magicos:
        mensagem = magico
        print(mensagem)

lista_magicos = ["mágico_1", "mágico_2", "mágico_3"]

show_magicians(lista_magicos)

print("######################################################################")
'''
#EXERCICÍO 8.10 --FAZER MAIS TARDE!

def show_magicians(magicos,makes):
    """Passar uma lista de mágicos para uma função"""
    for magico in magicos:
        nomes = magicos
        print(nomes)

def make_great(makes):
    """Modificando uma lista."""
    print("\nLista modificada:")
    for make in makes:
        print(make)
        
magicos = ["mágico_1", "mágico_2", "mágico_3"]
makes = ["o Grande"]
show_magicians(magicos,makes)
make_great (makes)
'''
print("######################################################################")

#EXERCÍCIO 8.12

def make_sanduiche(*ingredientes):
    """Sanduíches"""
    print(ingredientes)

make_sanduiche("queijo")

make_sanduiche("hamburguer", "tomate", "alface")
    
make_sanduiche("queijo", "hamburguer", "tomate", "alface", "ketchup",\
"mostarda")

print("######################################################################")

#EXERCÍCIO 8.13

def build_profile(first,last,**user_info): 
    """Constrói um dicionário contendo tudo que sabemos sobre um usuário."""
    profile = {}
    profile['first_name'] = first 
    profile['last_name'] = last 
    for key,value in user_info.items(): 
        profile[key] = value
    return profile
    
user_profile = build_profile('beatriz', 'almeida', location = 'são paulo',\
field = 'tecnology') 
print(user_profile)

print("######################################################################")

#EXERCÍCIO 8.14

def car_info(nome_fabricante,nome_marca,**informacao):
    fabrica_info = {}
    fabrica_info ["nome"] = nome_fabricante
    fabrica_info ["marca"] =  nome_marca
    for key, value in informacao.items():
        fabrica_info[key] = value
    return fabrica_info
    
descricao_car = car_info ("civic", "honda", color = "black", year = "2010")
print(descricao_car)

print("######################################################################")

#EXERCÍCIO 8.15

import printing_functions # importado no início do arquivo 

print("######################################################################")

#EXERCÍCIO 8.16

from pizzas import * # importado no início do arquivo 

print("######################################################################")

#EXERCÍCIO 8.17 

# Estilizando funções - feito!
