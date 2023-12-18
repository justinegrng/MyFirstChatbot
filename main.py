from functions import *
from menu import *

if __name__ == "__main__":
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    clean_speeches(files_names)
    while 1:
        choice = str(input("Voulez-vous accéder aux choix du menu ?\n"))
        if choice.lower() == "oui":
            menu()
        else:
            print("Vous êtes sortis ! ;( Vous pouvez relancer le programme.")
            exit(0)