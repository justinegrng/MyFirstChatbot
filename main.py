from functions import *

if __name__ == "__main__":
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    extract_name()
    print_list(files_names)
    clean_speeches(files_names)
    president = input("Quel président ?")
    print(associate_president(president))
