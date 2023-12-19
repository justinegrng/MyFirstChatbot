import os
import math
from functions import *


def intersection(question, directory):
    common_words = []
    corpus = ""
    if directory[-1] != "/":
        directory += "/"
    for filename in os.listdir(directory):
        corpus += (open(directory + filename, "r", encoding="utf-8").read())
    question = clean_question(question)
    question = question.split(" ")
    corpus = corpus.split(" ")
    for i in range(len(corpus)):
        for j in range(len(question)):
            if corpus[i] == question[j] and corpus[i] != '':
                common_words.append(corpus[i])
    return common_words

def matrix_tf(question, directory):
    matrix = []
    corpus = []
    if directory[-1] != "/":
        directory += "/"
    for filename in os.listdir(directory):
        matrix.append([])
        corpus.append(open(directory + filename, "r", encoding="utf-8").read())
    question = clean_question(question)
    question = question.split(" ")
    for elem in question:
        if elem == '':
            question.remove(elem)
    for i in range(len(corpus)):
        corpus[i] = corpus[i].split(" ")
    cleaned_corpus = []
    for i in range(len(os.listdir(directory))):
        cleaned_corpus.append([])
        for j in range(len(corpus[i])):
            if cleaned_corpus[i].count(corpus[i][j]) == 0:
                cleaned_corpus[i].append(corpus[i][j])
    for i in range(len(os.listdir(directory))):
        matrix.append([])
        for j in range(len(corpus[i])):
            count = 0
            for k in range(len(question)):
                if corpus[i][j] == question[k]:
                    count += 1
            matrix[i].append(count)

    return matrix



def get_question_tfidf(question, directory):
    idfs = idf(directory)
    question = clean_question(question)
    question_words = question.split(" ")
    for elem in question_words:
        if elem == '':
            question_words.remove(elem)

    tf_scores = {}
    for word in question_words:
        tf_scores[word] = tf_scores.get(word, 0) + 1

    tfidf = []
    for word in question_words:
        tf = tf_scores[word]
        idf_score = idfs.get(word, 0)
        tfidf.append(tf * idf_score)

    return tfidf


def scalar_product(v1, v2):
    if len(v1) != len(v2):
        return 0
    else:
        scalar = 0
        for i in range(len(v1)):
            scalar += float(v1[i]) * float(v2[i])
        return scalar


def norm(v):
    return math.sqrt(scalar_product(v, v))

def similarity(v1, v2):
    if norm(v1) == 0 or norm(v2) == 0:
        return 0
    return scalar_product(v1, v2) / (norm(v1) * norm(v2))

def most_pertinent_dir(question, directory):
    matrix = matrix_tf(question, directory)
    tfidf = get_question_tfidf(question, directory)  # Correction ici
    similarities = []

    for i in range(len(matrix)):
        sim = similarity(tfidf, matrix[i])
        similarities.append(sim)

    max_similarity_index = similarities.index(max(similarities))
    most_pertinent_file = os.path.join(directory, os.listdir(directory)[max_similarity_index])
    most_pertinent_file_speeches = os.path.join("./speeches", most_pertinent_file)
    return most_pertinent_file_speeches

def extract_answer(question, directory):
    most_pertinent_file_speeches = most_pertinent_dir(question, directory)
    most_pertinent_file_cleaned = os.path.basename(most_pertinent_file_speeches)

    cleaned_file_path = os.path.join(directory, most_pertinent_file_cleaned)
    with open(cleaned_file_path, "r", encoding="utf-8") as file:
        answer = file.read()
    return answer
