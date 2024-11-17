import nltk
import matplotlib.pyplot as plt

nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

#Store file directory as TextFile
TextFile = 'data/fruits.txt'

#Function to read text from file
def read_text_from_file(filename):
    with open(filename, 'r') as file:
        #text1 = file.readlines() ## Read the entire file content as a List
        text = file.read()  # Read the entire file content as a string
    return text

def check_text_type(filename):
    return type(read_text_from_file(filename))

def check_length_of_text(filename):
    return len(read_text_from_file(filename))

# Tokenize the text by sentences
def tokenize_text_by_sentence(filename):
    sentences = sent_tokenize(filename)
    # how many sentences are there?
    # return print("There are:", len(sentences), "sentences")
    return sentences

text = read_text_from_file(TextFile)
print(text)
# print(tokenize_text_by_sentence(text[0]))




