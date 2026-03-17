import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, ne_chunk

text = "Ravi works at Google in India. NLP is very interesting!!!"

# Lowercase
text = text.lower()

# Tokenization
tokens = word_tokenize(text)

# Remove punctuation
tokens = [word for word in tokens if word not in string.punctuation]

# Remove stopwords
tokens = [word for word in tokens if word not in stopwords.words('english')]

print("After Cleaning:", tokens)

# Stemming
ps = PorterStemmer()
stemmed = [ps.stem(word) for word in tokens]
print("Stemming:", stemmed)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
print("Lemmatization:", lemmatized)

# POS Tagging
pos_tags = pos_tag(tokens)
print("POS Tags:", pos_tags)

# NER (use original sentence)
tokens2 = word_tokenize("Ravi works at Google in India")
tags = pos_tag(tokens2)
ner = ne_chunk(tags)
print("NER:", ner)