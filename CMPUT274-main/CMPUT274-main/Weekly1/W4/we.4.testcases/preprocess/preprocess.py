#--------------------------------------------
#   Name: 
#   ID: 
#   CMPUT 274, Fall 2021
#
#   Weekly Exercise #4: Text Preprocessor
#-------------------------------------------- 
import re
import sys

def mode():
    if len(sys.argv) != 1:
        modename = sys.argv[1]
        if modename == 'keep-digits':
            keepdigits()
            sys.exit()
        if modename == 'keep-stops':
            keepstops()
            sys.exit()
        if modename == 'keep-symbols':
            keepsymbols()
            sys.exit()
    if len(sys.argv) == 1:
        preprocess()
        sys.exit()
    else:
        print('error input, please enter keep-digits, keep-stops, keep-symbols')
        sys.exit()
    

def keepdigits():
    stopword = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which","who", "whom", "this", "that", "these", "those","am", "is", "are", "was", "were", "be","been", "being", "have", "has", "had","having", "do", "does", "did", "doing", "a", "an","the", "and", "but", "if","or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    text = input('').split()

    for i in range(0,len(text)):
        text[i] = str.lower(text[i])

    for i in range(0,len(text)):
        text[i] = ''.join(filter(str.isalnum, text[i]))

    while '' in text:
        text.remove('')

    for i in range(0,len(stopword)):
        for word in text:
            if word == stopword[i]:
                text.remove(word)
            else:
                pass
    print(' '.join(text))

def keepstops():
    text = input('').split()

    for i in range(0,len(text)):
        text[i] = str.lower(text[i])

    for i in range(0,len(text)):
        text[i] = ''.join(filter(str.isalnum, text[i]))

    while '' in text:
        text.remove('')

    for i in range(0,len(text)):
        if text[i].isdigit():
            pass
        else:
            text[i] = re.sub(r'[0-9]+','',text[i])

    print(' '.join(text))

def keepsymbols():
    stopword = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which","who", "whom", "this", "that", "these", "those","am", "is", "are", "was", "were", "be","been", "being", "have", "has", "had","having", "do", "does", "did", "doing", "a", "an","the", "and", "but", "if","or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    text = input('').split()

    for i in range(0,len(text)):
        text[i] = str.lower(text[i])

    while '' in text:
        text.remove('')

    for i in range(0,len(text)):
        if text[i].isdigit():
            pass
        else:
            text[i] = re.sub(r'[0-9]+','',text[i])

    for i in range(0,len(stopword)):
        for word in text:
            if word == stopword[i]:
                text.remove(word)
            else:
                pass

    print(' '.join(text))



def preprocess():
    stopword = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which","who", "whom", "this", "that", "these", "those","am", "is", "are", "was", "were", "be","been", "being", "have", "has", "had","having", "do", "does", "did", "doing", "a", "an","the", "and", "but", "if","or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    text = input('').split()

    for i in range(0,len(text)):
        text[i] = str.lower(text[i])

    for i in range(0,len(text)):
        text[i] = ''.join(filter(str.isalnum, text[i]))

    while '' in text:
        text.remove('')

    for i in range(0,len(text)):
        if text[i].isdigit():
            pass
        else:
            text[i] = re.sub(r'[0-9]+','',text[i])

    for i in range(0,len(stopword)):
        for word in text:
            if word == stopword[i]:
                text.remove(word)
            else:
                pass

    print(' '.join(text))

if __name__ == "__main__":
    mode()
