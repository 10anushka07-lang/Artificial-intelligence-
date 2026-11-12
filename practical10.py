import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
sentence = input("Enter a sentence: ")
words = nltk.word_tokenize(sentence)
result = nltk.pos_tag(words)
print("POS Tagging:", result)