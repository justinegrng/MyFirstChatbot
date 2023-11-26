import os
import math

# Fonctions de base

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
            elem.pop()
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
    if president == "Chirac":
        print("Jacques")
    if president == "Mitterand":
        print("François")


# Méthode TF-IDF
def count_occurrence(files_names):
    dict = {}
    for file in files_names:
        f = open("./cleaned/" + file, "r", encoding="utf-8")
        lines = f.readlines()
        for line in lines:
            for word in line.split():
                if word in dict:
                    dict[word] += 1
                else:
                    dict[word] = 1
    return (dict)


def print_idf(idf):
    for word in idf:
        print(word + " : " + str(idf[word]))


def print_tf_idf(tf_idf):
    for file in tf_idf:
        print(file + " : ")
        for word in tf_idf[file]:
            print(word + " : " + str(tf_idf[file][word]))


def idf(dir):
    nb_files = len(list_of_files(dir, "txt"))
    dict = count_occurrence(list_of_files(dir, "txt"))
    idf_dict = {}
    for word in dict:
        idf_dict[word] = math.log(1 + (nb_files / dict[word]))

    return idf_dict


def tf_idf(dir):
    idf_dict = idf(dir)
    tf_idf_dict = {}
    for file in list_of_files(dir, "txt"):
        tf_idf_dict[file] = {}
        f = open(dir + "/" + file, "r", encoding="utf-8")
        lines = f.readlines()
        for line in lines:
            for word in line.split():
                if word in tf_idf_dict[file]:
                    tf_idf_dict[file][word] += 1
                else:
                    tf_idf_dict[file][word] = 1
        for word in tf_idf_dict[file]:
            tf_idf_dict[file][word] = tf_idf_dict[file][word] * idf_dict[word]
    return tf_idf_dict


# Fonctionnalités avec la méthode TF-IDF
def non_important_word(tf_idf_dict):
    for file in tf_idf_dict:
        for word in tf_idf_dict[file]:
            if tf_idf_dict[file][word] < 0.5:
                print(word)


def important_word(tf_idf_dict):
    for file in tf_idf_dict:
        tf_idf_dict[file] = sorted(tf_idf_dict[file].items(), key=lambda x: x[1], reverse=True)
        print(file + " : ")
        for i in range(20):
            print(tf_idf_dict[file][i][0] + " : " + str(tf_idf_dict[file][i][1]))


def chirac_most_repeated(tf_idf_dict):
    print("Les 20 mots les plus répétés dans les discours de Jacques Chirac sont : ")
    tf_idf_chirac = {}
    for file in tf_idf_dict:
        if "Chirac" in extract_name(file):
            tf_idf_chirac[file] = tf_idf_dict[file]
    important_word(tf_idf_chirac)


def nation_word(tf_idf_dict):
    print("Les présidents qui ont parlé de la nation dans leur discours sont : ")
    talked_about = {}
    for file in tf_idf_dict:
        for word in tf_idf_dict[file]:
            if word == "nation":
                talked_about[extract_name(file)] = tf_idf_dict[file][word]
                print(extract_name(file))

    talked_about = sorted(talked_about.items(), key=lambda x: x[1], reverse=True)
    print("Les présidents qui ont le plus parlé de la nation sont : ")
    print(talked_about[0][0] + " : " + str(talked_about[0][1]))


def ecologie_word(tf_idf_dict):
    print("Les présidents qui ont parlé de l'écologie dans leur discours sont : ")
    talked_about = {}
    for file in tf_idf_dict:
        for word in tf_idf_dict[file]:
            if word == "climat" or word == "écologie":
                print(extract_name(file))
                return


def common_words(tf_idf_dict):
    print("Les mots les plus répétés dans les discours de tous les présidents sont : ")

    for file in tf_idf_dict:
        for word in tf_idf_dict[file]:
            if tf_idf_dict[file][word] > 0.5 and tf_idf_dict[file][word] < 1.0:
                print(word + " : " + str(tf_idf_dict[file][word]))