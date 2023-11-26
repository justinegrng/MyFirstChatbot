from functions import *

if __name__ == "__main__":
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    clean_speeches(files_names)
    while 1:
        choice = str(input("Veux tu accéder aux choix du menu ?\n"))
        if choice == "Oui":
            menu()
        else:
            print("Vous êtes sorti ! Relancez le programme ;(")
            exit(0)

