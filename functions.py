import os

#Fonctions de base

def print_list(list):
    for element in list:
        print(element)

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def extract_name(file_name):
    return (file_name.split("_")[1]).split(".txt")[0]

def get_all_president_name(files_names):
    list = []
    for presidents in files_names:
        list.append(extract_name(presidents))
    for elem in list:
        try:
            if int(elem[:-1]) != 1:
                list.remove(elem)
                continue
            elem.erase[:-1]
            print(elem)
        except:
            print(elem)
            continue

def clean_speeches(files_names):
    for file in files_names:
        f = open("./speeches/" + file, "r", encoding="utf-8")
        lines = f.readlines()
        f.close()
        lines = [line.lower() for line in lines]
        if not os.path.exists("./cleaned"):
            os.makedirs("./cleaned")
        f = open("./cleaned/" + file, "w", encoding="utf-8")
        for line in lines:
            if line != "\n":
                for char in line:
                    if char == '.' or char == ',' or char == '!' or char == '?' or char == ';' or char == ':':
                        line = line.replace(char, "")
                    elif char == '-' or char == "'":
                        line = line.replace(char, " ")
                f.write(line)
        f.close()

def associate_president(president):
    if president == "Giscard d'Estaing":
        print("Valéry")
    if president == "Macron":
        print("Emmanuel")
    if president == "Hollande":
        print("François")
    if president == "Sarkozy":
        print("Nicolas")
    if president=="Chirac":
        print("Jacques")
    if president == "Mitterand":
        print("François")

# Méthode TF-IDF
def count_occurrence(files_names):
    for file in files_names:
        f = open("./cleaned/" + file, "r", encoding="utf-8")
        lines = f.readlines()
        for line in lines :
            for char in line :
                print ()


def tf_idf ():




#Fonctionnalités à développer
