#!/usr/bin/env python
# coding: utf-8

# In[5]:


lst = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
    
print("Sum of elements in given list is :", sum(lst))


# In[3]:


def revString(st): #str-formal variable
    #wel12come 
    char="" 
    dig='' 
    for i in range(0,len(st),1): 
        if(ord(st[i])>=48 and ord(st[i])<=57): 
            dig=dig+st[i] 
        else: 
            char=char+st[i]
    return char+dig

s=input() 
print(revString(s))


# In[ ]:




