#!/usr/bin/env python
# coding: utf-8

# In[2]:


#introductions for for loop


# In[30]:


bank_customers= ['ayb', 'anwar', 'Anees', 'sayyed', 'hamza', 'Kausar']
print (bank_customers[5])


# In[31]:


#requirement: greeting the customers


# In[32]:


print(f"Chase customers Good morning, {bank_customers[4].title()}")


# In[33]:


# to automate the solution


# In[35]:


for customers in bank_customers:
    print(f"Chase customers Good morning, {customers}")


# In[40]:


print(f"Chase customers Good morning, {customers.upper()}")


# In[41]:


#general syntax for a for loop: for temp in manner


# In[45]:


for x in bank_customers:
    print(f"HELLO, {x}")


# In[46]:


for x in bank_customers:
    print(f"HELLO, {x.upper()}")


# In[52]:


for y in bank_customers:
    print(f"HELLO, {y.title()}")
    print(f"Nice work, {y.title()}")
    print(f"Thank you all!.\n")


# In[ ]:




