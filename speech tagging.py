#!/usr/bin/env python
# coding: utf-8

# In[2]:


from nltk.tokenize import sent_tokenize, word_tokenize


# In[6]:


ex = "Time to get started with natural language processing. Python will make it easy!"
sent_tokens = sent_tokenize(ex)


# In[7]:


sent_tokens


# In[8]:


word_tokens = word_tokenize(ex)
word_tokens


# In[10]:


from nltk.tag import pos_tag


# In[11]:


tags = pos_tag(word_tokens)


# In[12]:


tags


# In[13]:


import nltk


# In[15]:


nltk.help.upenn_tagset('VB')


# In[16]:


list_of_tags = []


# In[17]:


for pair in tags:
    list_of_tags.append(pair[1])


# In[19]:


list_of_tags = list(set(list_of_tags))
list_of_tags


# In[21]:


for pos in list_of_tags:
    print(nltk.help.upenn_tagset(pos))


# In[ ]:




