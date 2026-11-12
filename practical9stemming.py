import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer()
sentence = input("Enter a sentence: ")
words = sentence.split()
result = [ps.stem(word) for word in words]
print("Original Sentence:", sentence)
print("After Stemming:", " ".join(result))