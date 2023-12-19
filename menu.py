import os
from functions import *
from matrixfunctions import *

def menu():
    print("1.Utiliser les fonctions de base.\n2.Utiliser les fonctionnalités avec TF-IDF.\n3.Poser une question. ")
    user = int(input("Que voulez-vous faire ? Choisissez 1, 2 ou 3.\n"))

    while user !=1 and user !=2 and user !=3:
        user = int(input("Que voulez-vous faire ? Choisissez 1, 2 ou 3.\n"))

    if user == 1:
        print("1.Afficher la liste des présidents\n"
              "2.Afficher les prénoms des présidents associés à leurs noms\n"
              )
        choice = int(input("Que voulez vous faire ?\n"))
        while choice != 2 and choice != 1:
            choice = int(input("Que voulez vous faire ?\n"))

        if choice == 1:
            get_all_president_name(list_of_files("cleaned", "txt"))
        if choice == 2:
            president = input("De quel president veux-tu le prénom ?\n"
                              "Giscard d'Estaing\nMitterand\nMacron\nHollande\nSarkozy\nChirac\n")
            associate_president(president)

    elif user == 2:
        print("1. Afficher la liste des mots les moins importants\n"
              "2. Afficher les mots ayant le score TD-IDF le plus élevé\n"
              "3. Afficher les mots les plus répétés par le président Chirac\n"
              "4. Afficher les noms des présidents qui ont parlé de la « Nation » et celui qui l’a répété le plus de fois\n"
              "5. Afficher le premier président à parler du climat et/ou de l’écologie\n"
              "6. Afficher les mots que tous les présidents ont évoqués (hormis les mots dits non importants)")
        choice = int(input("Que voulez vous faire parmi ces 6 fonctionnalités ?\n"))
        while choice != 2 and choice != 1 and choice != 3 and choice != 4 and choice != 5 and choice != 6:
            choice = int(input("Que voulez vous faire ?\n"))

        if choice == 1:
            non_important_word(tf_idf("cleaned"))
        elif choice == 2:
            important_word(tf_idf("cleaned"))
        elif choice == 3:
            chirac_most_repeated(tf_idf("cleaned"))
        elif choice == 4:
            nation_word(tf_idf("cleaned"))
        elif choice == 5:
            ecologie_word(tf_idf("cleaned"))
        elif choice == 6:
            common_words(tf_idf("cleaned"))

    elif user == 3:
        choice = clean_question(str(input("Vous pouvez poser votre question.\n")))
        answer = extract_answer(choice, "cleaned")
        print("Voici ta réponse :", answer)

