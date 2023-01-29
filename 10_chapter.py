# EXERCÍCIO 10.1

filename = "learning_python.txt"

with open(filename) as file_object:
     lines = file_object.readlines()
     
for line in lines:
    print(line.rstrip())
    
print("######################################################################")

#EXERCÍCIO 10.2

filename = "learning_python.txt"

with open(filename) as file_object:
     lines = file_object.readlines()
     
for line in lines:
    print(line.replace("Python", "C").rstrip())

print("######################################################################")

#EXERCÍCIO 10.3
