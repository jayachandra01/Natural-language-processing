#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1: Import nltk
import nltk

# Step 2: Download the 'book' dataset (contains text1 to text9)
nltk.download('book')

# Step 3: Import all book texts
from nltk.book import *


# In[2]:


texts()


# In[3]:


text1


# In[4]:


text2


# In[5]:


text3


# In[7]:


from nltk.corpus import brown


# In[8]:


brown.categories()


# In[9]:


brown.words(categories='adventure')


# In[10]:


brown.sents(categories=['adventure','editorial','news'])


# In[14]:


from nltk.corpus import webtext
nltk.download('webtext')  

for fileid in webtext.fileids(): 
    print(fileid, webtext.raw(fileid)[:20], '...')


# In[15]:


from nltk.corpus import inaugural


# In[16]:


inaugural.fileids()


# In[ ]:




