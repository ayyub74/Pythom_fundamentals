#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Introduction to f string in python


# In[ ]:


first_name='ayyub'
last_name='sayyed'


# In[ ]:


# requirement is print full name


# In[ ]:


# general syntax of the strings -----> f "(placeholder1{placeholder2})" ===> referance variable


# In[8]:


first_name='ayyub'
last_name='sayyed'
full_name = f"{first_name} {last_name}"
print (full_name)


# In[9]:


print (full_name.upper())


# In[10]:


print (full_name.title())


# In[11]:


print (full_name.lower())


# In[ ]:


# custom greeting message "keep up the good work"


# In[18]:


print (f"Keep up the good work, {full_name.title()}")


# In[21]:


#Adding whitespace to strings


# In[22]:


print ('fav.iang:pythoncjavac++swipt')


# In[ ]:


# \n is delimiter for new line


# In[25]:


print ('fav_long:\npython\nc\njave\nc++\nswipt')


# In[ ]:


# t delimeter is for tab


# In[30]:


print('fav_long:\n\tpython\n\tc\n\tjava\n\tc++\n\tswipt')


# In[ ]:


# removing whitepace


# In[32]:


favlang='     ayyub'
print(favlang)


# In[34]:


favlang.lstrip() # left side striping (removing whitespace from left)


# In[36]:


favlang2='python'
print(favlang2)


# In[37]:


print(favlang2.rstrip()) # right side stripping


# In[39]:


language = '   python   '
print(language)


# In[40]:


language.strip() # search opertaion () and removed will be happening


# In[ ]:





# In[ ]:




