# My First ChatBot 💻
![MyFirstChatBot](https://github.com/user-attachments/assets/9cd92d92-c1ae-49e1-8063-fd137ba48fcd)

## Pour commencer ...
[Lien vers le dépôt GitHub](https://github.com/justinegrng/MyFirstChatbot.git) 

### Instructions d'éxécution du code
Exécuter le programme ```main.py```, puis accéder au menu avec "Oui" puis sélectionner les fonctions à utiliser avec 1 *(Fonctions de base)*, 2 *(Fonctionnalités avec TF-IDF)* ou 3 *(Poser une question)*.  
Ensuite si 1 est séléctionné (on doit rechoisir un chiffre), on a :  
↪ 1. La liste de tous les présidents  
↪ 2. Le prénom du président associé à son nom demandé par l'utilisateur  
Si 2 sélectionné (on doit rechoisir un chiffre), on a :  
↪ 1. La liste des mots les moins importants  
↪ 2. Le(s) mot(s) ayant le score TD-IDF le plus élevé  
↪ 3. Le(s) mot(s) le(s) plus répété(s) par Chirac  
↪ 4. Le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus  
↪ 5. Le premier président à parler du climat  
↪ 6. Le(s) mot(s) que tous les présidents ont évoqués  

## Fonctionnalités principales 
### Liste des fonctions :
#### Fonctions de base
- `printlist`  → *Affiche tous les éléments d'une liste*
- `list_of_files`  → *Parcourir la liste des fichiers d’une extension donnée et dans un répertoire donné*
- `extractname`  → *Extraire les noms des présidents à partir des noms des fichiers texte fournis*
- `associate_president`  → *Associer à chaque président un prénom* 
- `get_all_president_name`  → *Afficher la liste des noms des présidents*
- `clean_speeches`  → *Convertir les textes des 8 fichiers en minuscules et stocker les contenus dans de nouveaux fichiers dans un nouveau dossier appelé « cleaned » puis parcourir son texte et supprimer tout caractère de ponctuation*
- `clean_question`  → *Prend en paramètre le texte de la question, et qui retire la ponctuation*

#### Fonctions pour la méthode TF-IDF
- `count_occurrence`  → *Prend en paramètre une chaine de caractères et retourne un dictionnaire associant à chaque mot le nombre de fois qu’il apparait dans la chaine de caractères*
- `idf`  → *Prend en paramètre le répertoire où se trouve l’ensemble des fichiers du corpus et retourne un dictionnaire associant à chaque mot son score IDF*
- `tf_idf`  → *Prend en paramètre le répertoire où se trouvent les fichiers à analyser et retourne au minimum la matrice TF-IDF*
- `print_idf`  → *Pour chaque mot dans un fichier, il applique la fonction idf et affiche*
- `print_tf_idf`  → *Pour chaque mot de chaque fichier, il applique la fonction tf_idf et affiche*

#### Fonctionnalités avec la méthode TF-IDF
- `non_important_word`  → *Afficher la liste des mots les moins importants dans le corpus de documents*
- `important_word`  → *Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé*
- `chirac_most_repeated`  → *Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac*
- `nation_word`  → *Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois*
- `ecologie_word`  → *Indiquer le premier président à parler du climat et/ou de l’écologie*
- `common_words`  → *Indiquer hormis les mots dits « non importants », le(s) mot(s) que tous les présidents ont évoqués*

#### Fonctions pour la matrice
- `intersection`  → *Identifier les termes de la question qui sont également présents dans le corpus de documents*
- `matrix_tf`  → *Calcul du vecteur TF-IDF pour les termes de la question*
- `scalar_product`  → *Calcul du produit scalaire*
- `norm`  → *Calcul de la norme*
- `similarity`  → *Calcul de la similarité*
- `most_pertinent_dir`  → *Calcul du document le plus pertinent*
- `extract_answer`  → *Génération d’une réponse* 
- `get_question_tfidf`  → *Permet d'obtenir le score TF-IDF de la question avec le même principe que celui pour les textes du corpus*

## Contributeurs
> 📚 Justine GARNUNG  
> 🧠 Yéléna SAINTE-ROSE BRUNY  
