import nltk 
from nltk.corpus import stopwords 
nltk.download('stopwords')
f = open("passage.txt", "r")
text = f.read()
words = text.split()
stop_words = set(stopwords.words('english'))
result = [word for word in words if word.lower() not in stop_words]
print("Original Text:", text)
print("After Removing Stop Words:", " ".join(result))