#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install PuLP


# In[2]:


import pulp as p


# ### Problem 1
#  
#  Maximization Problem

# In[3]:


Lp_prob=p.LpProblem('Problem1',p.LpMaximize)


# #### Decision Variable 

# In[4]:


x1=p.LpVariable("x1",lowBound=0)  # Create a variable x>=0
x2=p.LpVariable("x2",lowBound=0)  # Create a variable y>=0


# #### Objective Function

# In[5]:


Lp_prob+=5*x1+7*x2


# #### Constraints

# In[6]:


Lp_prob+=1*x1+0*x2<=6
Lp_prob+=2*x1+3*x2<=19
Lp_prob+=1*x1+1*x2<=8


# In[7]:


print(Lp_prob)


# #### Solving the LPP

# In[8]:


status=Lp_prob.solve()


# In[9]:


print(p.LpStatus[status])


# #### Solution

# In[10]:


print("x1=",p.value(x1))
print("x2=",p.value(x2))
print("objective=",p.value(Lp_prob.objective))


# In[ ]:





# ### Problem 2
# 
#     Minimization Problem
#     Daru cha problem

# In[11]:


Lp_prob=p.LpProblem('Problem1',p.LpMinimize)


# #### Decision Variable

# In[12]:


x1=p.LpVariable("Solan",lowBound=0)  # Create a variable x>=0
x2=p.LpVariable("Mohan Nagar",lowBound=0)  # Create a variable y>=0


# #### Objective Function

# In[13]:


Lp_prob+=600*x1+400*x2


# #### Constraints

# In[14]:


Lp_prob+=1500*x1+1500*x2>=20000
Lp_prob+=3000*x1+1000*x2>=40000
Lp_prob+=2000*x1+5000*x2>=44000
Lp_prob+=1*x1+0*x2<=30
Lp_prob+=0*x1+1*x2<=30


# In[15]:


print(Lp_prob)


# #### Solving the LPP

# In[16]:


status=Lp_prob.solve()
print(p.LpStatus[status])


# #### Solution 

# In[17]:


print("Solan=",p.value(x1))
print("Mohan Nagar=",p.value(x2))
print("objective=",p.value(Lp_prob.objective))


# In[ ]:





# ### Problem 3
#     
#        Maximum problem
#        Machanical 

# In[18]:


Lp_prob=p.LpProblem('Problem1',p.LpMinimize)


# In[28]:


x1=p.LpVariable("A ",lowBound=0)  # Create a variable x>=0
x2=p.LpVariable("B ",lowBound=0)  # Create a variable y>=0


# In[29]:


Lp_prob+=40*x1+10*x2


# In[30]:


Lp_prob+=12*x1+6*x2>=3000
Lp_prob+=4*x1+10*x2>=2000
Lp_prob+=2*x1+3*x2>=900


# In[31]:


print(Lp_prob)


# In[32]:


status=Lp_prob.solve()
print(p.LpStatus[status])


# In[34]:


print("A =",p.value(x1))
print("B =",p.value(x2))
print("objective=",p.value(Lp_prob.objective))


# In[ ]:





# In[ ]:




