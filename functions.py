import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def extractname():
def associerprésident (president):
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

