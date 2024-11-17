import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud

# nltk.download('stopwords')
nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger_eng')

#Function to read text from file
def read_text_from_file(filepath):
    with open(filepath, 'r') as file:
        #text1 = file.readlines() ## Read the entire file content as a List
        text = file.read()  # Read the entire file content as a string
    return text

def check_text_type(text):
    print(f"The Text type is: {type(text)}")
    return type(text)

def check_length_of_text(text):
    length = len(text)
    print(f"The Length of text is: {length}")
    return length

# Tokenize the text by sentences
def tokenize_text_by_sentence(text):
    sentences = sent_tokenize(text)
    print(f"The Tokenized Sentences has a length of({len(sentences)}) and contains:\n {sentences}\n\n") # how many sentences are there?
    return sentences

# Tokenize the text by words
def tokenize_text_by_word(text):
    words = word_tokenize(text)
    print(f"Tokenized Words: ({len(words)}): {words}\n\n") #how many words are there?
    return words

# plot the most 10 frequent words
def plot_word_frequency(frequency_distribution):
    print("Plotting word frequency...\n")
    frequency_distribution.plot(10) #plot a word


# Remove punctuation marks
def remove_punc_marks(words):
    # Empty list to store non-punctual words
    words_no_punc = []

    # removing punctuation marks
    for word in words:
        if word.isalpha():
            words_no_punc.append(word.lower())

    # Print the words without punctuation marks
    print("There are:", len(words_no_punc), "non punctuation words\n\n")
    return words_no_punc

# Find the frequency from the no-punctuation-words
def find_word_frequency(words_no_punc):
    frequency_distribution = FreqDist(words_no_punc)
    #print(frequency_distribution.most_common(10)) # Print the 10 most frequent words
    return frequency_distribution

# Find the most common frequency from the no-punctuation-words
def find_most_common_word_frequency(words_no_punc, num):
    frequency_distribution = FreqDist(words_no_punc)
    most_common = frequency_distribution.most_common(num)
    print(f"Most Common Words: {most_common}")  # Print the 10 most frequent words
    return most_common

# Remove stopword from text
def remove_stopwords_from_word(words):
    # list of stopwords
    stopword_list = stopwords.words('english')

    # Empty list to store clean words
    clean_words = []
    for word in words:
        if word not in stopword_list:
            clean_words.append(word)

    # print("There are:", len(clean_words), "clean words") #print out the length of words from clean data
    return clean_words

# Find Parts-of-Speech of the words
def find_parts_of_speech(words_in_list, limit_words):

    pos_tags = pos_tag(words_in_list)

    if limit_words == 'all':
        limit_words = len(pos_tags) # No limit, process all words

    # Slice the list to include only the specified number of words
    limited_pos_tags = pos_tags[:limit_words]

    print("\nPoS Tagging Result:")
    for word, tag in limited_pos_tags:
        print(f"{word}: {tag}")

    return limited_pos_tags


#Visualization Analysis
##We'll be working with Word Clouds to Visualize the most frequent words in the text, Bar Charts to Visualize the distribution of word frequencies, sentence lengths, or part-of-speech tags. Network Graphs to Visualize the relationships between words, sentences, or topics

## Word Clouds Visualize the most frequent words in the text
def display_word_cloud(words):

    # Convert list of words to a single string if it's not already a string
    if isinstance(words, list):
        words = " ".join(words)

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          min_font_size=10).generate(words)
    # plot the WordCloud image

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

    return wordcloud

#Store file directory as TextFile
textfile = 'data/fruits.txt' # Global variable

## Main function to process the text
def text_preprocessing(textfile):
    # Step 1: Read the text file
    ## Read the text file
    text = read_text_from_file(textfile)

    # Step 2: Call all the processing functions #
    print("Processing.........")

    ## Check for the text file type
    text_type = check_text_type(text)
    print(text_type)

    #Check length of text file
    text_len = check_length_of_text(text)


    #Tokenize the text by sentence
    print("\nTokenizing text by sentences...")
    token_text_by_sent = tokenize_text_by_sentence(text)

    #Tokenize the text by words
    print("\nTokenizing text by word...")
    tokenized_text_by_word = tokenize_text_by_word(text)

    #Removing punctuation marks...
    words_no_punc = remove_punc_marks(tokenized_text_by_word)

    #Finding word frequency with punctuation marks
    word_frequency_with_punc = find_word_frequency(tokenized_text_by_word)

    #Finding word frequency without punctuation marks
    word_frequency_with_no_punc = find_word_frequency(words_no_punc)

    #Finding most common words
    most_common_word_frequency = find_most_common_word_frequency(words_no_punc, 20)

    # Plot the text by word_frequency
    show_plot_word_frequency = plot_word_frequency(word_frequency_with_no_punc)

    # Removing stopwords...
    word_without_stopwords = remove_stopwords_from_word(words_no_punc)

    parts_of_speech = find_parts_of_speech(word_without_stopwords, 10)

    show_word_cloud = display_word_cloud(word_without_stopwords)

    # Return multiple results
    return {
        "textType": text_type,
        "text_len": text_len,
        "token_text_by_sent": token_text_by_sent,
        "tokenized_text_by_word": tokenized_text_by_word,
        "words_no_punc": words_no_punc,
        "word_frequency_with_punc": word_frequency_with_punc,
        "word_frequency_with_no_punc": word_frequency_with_no_punc,
        "most_common_word_frequency": most_common_word_frequency,
        "show_plot_word_frequency": show_plot_word_frequency,
        "word_without_stopwords": word_without_stopwords,
        "parts_of_speech": parts_of_speech,
        "show_word_cloud": show_word_cloud
    }
# Process the text and print the result
result = text_preprocessing(textfile)
print(f'Here is detailed analysis of the fruits file;\n {result}')