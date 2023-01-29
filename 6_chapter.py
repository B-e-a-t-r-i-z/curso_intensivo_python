#EXERCÍCIO 6.1

pessoa = {}
pessoa["first_name"] = "Beatriz"
pessoa["last_name"] = "De Almeida"
pessoa["age"] = 22
pessoa["city"] = "São Paulo"
print(pessoa)

print("#####################################################################")

#EXERCÍCIO 6.2

favority_number = {}
favority_number["Vitória"] = 2
favority_number["Sabrina"] = 7
favority_number["Thainara"] = 9
favority_number["Alan"] = 5
favority_number["Evelyn"] = 15
print(favority_number)

print("#####################################################################")

#EXERCÍCIO 6.3/   

glossario = {}
glossario["chapter_1"] = "numbers"  
glossario["chapter_2"] = "names_cases"
glossario["chapter_3"] = "list"
glossario["chapter_4"] = "for"
glossario["chapter_5"] = "if"
print("Eu aprendi "+ 
    glossario["chapter_1"].title() +
    " no 1° capitilo do livro")

print("#####################################################################")

# EXERCÍCIO 6.4

glossario = {"chapter_1": "numbers","chapter_2": "names_cases", "chapter_3": 
    "list", "chapter_4": "for", "chapter_5": "if", "chapter_6": "dicionário", 
    "chapter_7": "while", "chapter_8": "funções", "chpater_9": "classes", 
    "chapter_10": "arquivos"}

for key, value in glossario.items():
    print("\nKey: " + key)
    print("Value: " + value)

print("#####################################################################")

# EXERCÍCIO 6.5

rios = {"amazonas": "brasil", "mississipi": "E.U.A.", "nilo": "egito"}

for rio, pais in rios.items():
    print("O rio "+ rio.title() + " corre pelo " + pais.title())

print("\n________________________________________________________________\n")

for rio in rios.keys():
    print(rio.title())

print("\n________________________________________________________________\n")

for pais in rios.values():
    print(pais.title())
    
print("#####################################################################")

# EXERCÍCIO 6.6

enquete = {"jon": "python", "sansa": "java", "sarah": "c", "edward": "ruby"}
participantes = ["jon", "sansa", "sarah", "edward"]

for name in enquete.keys():
    if name in participantes:
        print("\nObrigado(a) por participar de nossa enquete, " + name.title()
        + " !!!")
if "sandor" not in enquete.keys():
    print("\nsandor".title() + " venha participar de nossa enquete!")

print("#####################################################################")

# EXERCÍCIO 6.7

pessoa_1 = {}
pessoa_1["first_name"] = "Beatriz"
pessoa_1["last_name"] = "De Almeida"
pessoa_1["age"] = 22
pessoa_1["city"] = "São Paulo"

pessoa_2 = {}
pessoa_2 ["first_name"] = "Sara"
pessoa_2 ["last_name"] = "De Souza"
pessoa_2 ["age"] = 48
pessoa_2 ["city"] = "São Paulo" 

pessoa_3 = {}
pessoa_3 ["first_name"] = "Ronaldo"
pessoa_3 ["last_name"] = "Da Silva"
pessoa_3 ["age"] = 56
pessoa_3 ["city"] = "São Paulo"

peoples = [pessoa_1, pessoa_2, pessoa_3]

for people in peoples:
    print(people)

print("#####################################################################")

# EXERCÍCIO 6.8

ravi = {"tipo": "Jabuti", "dono(a)": "Bia"}
dino = {"tipo": "Gato", "dono(a)": "Thainara"}
fantasma = {"tipo": "Lobo", "dono(a)": "Jon Snow"}

pets = [ravi, dino, fantasma]

for pet in pets:
    print(pet)

print("#####################################################################")

# EXERCÍCIO 6.9

favority_places = {"beatriz": "cinema","gabrila": "parque","vitor": "circo"}
favority_places = [favority_places]
for places in favority_places:
    print (places)

print("#####################################################################")

# EXERCÍCIO 6.10

favority_number = {}
favority_number["Vitória"] = 2, 9
favority_number["Sabrina"] = 7, 8
favority_number["Thainara"] = 9,4
favority_number["Alan"] = 5,2
favority_number["Evelyn"] = 15,7
print(favority_number)

print("#####################################################################")

# EXERCÍCIO 6.11 

citties = {"São Paulo":{"country": "Brasil","population": "12.325.232","fact":\
"São Paulo é uma metrópole multifacetada",},"Texas":{"country": "E.U.A.",\
"population": "28 milhões","fact": "Você não pode montar o seu cavalo no Texas\
à noite sem cauda lights",},"Tokyo":{"country": "Japão", "population": "9 \
milhões de habitantes","fact": "Tóquio foi fundada em 1457 e chamava-se Edo"},}

for key in citties.items():
    print(f"\n{key}")

print("#####################################################################")

# EXERCÍCIO 6.12

citties = {"são paulo":{"country": "brasil","population": "12.325.232","fact":\
"são Paulo é uma metrópole multifacetada",},\

"texas":{"country": "e.u.a.","population": "28 milhões","fact": "você não pode\
montar o seu cavalo no Texas à noite sem cauda lights",},\

"tokyo":{"country": "japão", "population": "9 milhões","fact": \
"tóquio foi fundada em 1457 e chamava-se Edo",},\

"buenos aries":{"country": "argentina", "population": "13 milhões","fact": \
"sabe a Casa Branca dos EUA? Em Buenos Aires é Casa Rosada"},}

for key in citties.items():
    print(f"\n{key}".title()) 
 
