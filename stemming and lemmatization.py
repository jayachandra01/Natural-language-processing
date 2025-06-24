#!/usr/bin/env python
# coding: utf-8

# In[16]:


import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

raw = """Call me Ishmael. Some years ago nevermind how long precisely having
little or no money in my purse and nothing particular to interest me on shore,
I thought I would sail about a little and see the watery part of the world."""

tokens = word_tokenize(raw)

porter = nltk.PorterStemmer()  
lancaster = nltk.LancasterStemmer()

porter_stems = [porter.stem(t) for t in tokens]   
lancaster_stems = [lancaster.stem(t) for t in tokens]

print("Porter:", porter_stems)
print("Lancaster:", lancaster_stems)


#Stemming is a method to reduce words to their base form known as a stem
# In[17]:


tokens = nltk.word_tokenize(raw)


# In[18]:


wnl = nltk.WordNetLemmatizer()


# In[19]:


[wnl.lemmatize(t) for t in tokens]


# In[ ]:


#lemmatization however reduces words to their base dictionary form ulike stemming which can truncate words

