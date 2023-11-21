from functions import *

if __name__ == "__main__":
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    print_list(files_names)
    clean_speeches(files_names)