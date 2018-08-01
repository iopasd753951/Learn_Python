
# coding: utf-8

# In[5]:


a = int(input())
b = int(input())
c = int(input())

total = (a + b + c) // 3 

print("점수 평균 :", total)


# In[6]:


a = 17 // 3
print(a)


# In[7]:


a = 17 % 3
print(a)


# In[ ]:


a = int(input())

if a % 2 == 0 :
    print("짝수")
elif a % 2 == 1 :
    print("홀수")
else :
    print("몰라")

