# Here are all the installs and imports you will need for your word cloud script and uploader widget
'''
!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
'''
# A file was uploaded with some random paragraphs copied from Project Gutenburg

def calculate_frequencies(file_contents):
    punctuations = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''

    # For testing file_contents is the text below
    file_contents = "But just here there was a weakness in the! system. Theologians and preachers' like her father boldly {declared the contrary, and asserted that@ the just here there was a weakness in the! system. Theologians and preachers' like her"

    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
        "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
        "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
        "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
        "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    # Initialize variables and lists
    inputWords = file_contents.split(" ")  # splits the file content in a list of words
    wordsList = [] #List to collect words without punctuation
    countable_Words = [] # list to collect only interesting words
    word_frequency = {}
    
    # Collect words by removing punctuations
    for word in inputWords:
        if not word.isalpha():
            for punc in punctuations:
                word = word.replace(punc, "") # replaces any words with any punctuation symbols
            wordsList.append(word)
        else:
            wordsList.append(word)
    
    # Collect only interesting words
    for word in wordsList:
        if word not in uninteresting_words:
            countable_Words.append(word)
            
    # Count the frequency of the words in countable_Words list
    for word in countable_Words:
        if word not in word_frequency.keys():
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1

    '''         
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_frequency)
    return cloud.to_array()
    '''
'''
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
'''