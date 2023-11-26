from functions import *

if __name__ == "__main__":
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    clean_speeches(files_names)
    print("1.Utiliser les fonctions de base.\n2.Utiliser les fonctionnalités avec TF-IDF.")
    user=int(input("Que voulez-vous faire ? Choisis 1 ou 2."))

    while user !=2 and user !=1:
        user = int(input("Que voulez-vous faire ? Choisis 1 ou 2."))

    if user == 1 :
        print("1.Afficher la liste des présidents\n"
              "2.Afficher les prénoms des présidents associés à leurs noms\n"
              )
        choice = int(input("Que voulez vous faire ?"))
        while choice != 2 and choice != 1:
            choice = int(input("Que voulez vous faire ?"))
        if choice == 1 :
            get_all_president_name("cleaned")
        if choice == 2 :
            president= input("De quel president veux-tu le prénom ?\n"
                             "Giscard d'Estaing\nMitterand\nMacron\nHollande\nSarkozy\nChirac\n")
            associate_president(president)


    elif user == 2 :
        print("1. Afficher la liste des mots les moins importants dans le corpus de documents.\n"
               "2. Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé\n"
               "3. Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac\n"
               "4. Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois\n"
               "5. Indiquer le premier président à parler du climat et/ou de l’écologie\n"
               "6. Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués.")
        choice=int(input("Que voulez vous faire parmi ces 6 fonctionnalités"))
        while choice != 2 and choice != 1 and choice != 3 and choice != 4 and choice != 5 and choice != 6:
            choice = int(input("Que voulez vous faire ?"))
        if choice == 1 :
            non_important_word(tf_idf("cleaned"))
        elif choice == 2 :
            important_word(tf_idf("cleaned"))
        elif choice == 3 :
            chirac_most_repeated(tf_idf("cleaned"))
        elif choice == 4:
            nation_word(tf_idf("cleaned"))
        elif choice == 5:
            ecologie_word(tf_idf("cleaned"))
        elif choice == 6:
            common_words(tf_idf("cleaned"))

