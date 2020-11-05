#!/usr/bin/env python
# coding: utf-8

# # Multiple Linear Regression

# ## Predict Profit using three input variables 

# In[74]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import this statsmodels library to performs LR
import statsmodels.formula.api as smf

#importing seaborn package
import seaborn as sns
import statsmodels.api as sm


# In[75]:


#read the data from startups.csv to data variable
data = pd.read_csv("C:\\Users\\yhari\\OneDrive\\Documents\\4. Github\\50_Startups.csv")


# In[76]:


#drop the state column and consider only the numerical data
start = data.drop(["State"], axis=1)


# In[77]:


#checking format of the dataset
type(start)


# In[78]:


# get the very first 5 rows of the dataset
start. head()


# In[79]:


sns.pairplot(start)


# In[80]:


start.columns


# In[81]:


#corelation b/n inputs
start.corr()


# In[82]:


#summary statistic
start.describe()


# In[83]:


start.columns


# In[84]:


#rename the columns 
#RD = R&D Spend, Admin=Administration, MS=Marketing Spend , Pft=Profit
col_names = ['RD', 'Admin', 'MS', 'Pft']
start.columns = col_names
start.head()


# In[85]:


#build model m1 using Ordinary Least Squares
m1 = smf.ols('Pft ~ RD+ Admin + MS' , data = start).fit()


# In[86]:


m1.summary()


# In[87]:


#parameters of model m1
m1.params


# In[88]:


#model mAD using only one input Adminstration
mAD = smf.ols('Pft ~ Admin', data=start).fit()


# In[89]:


#summary statistics of mAD model
mAD.summary()


# In[90]:


#build another model name mMS using one input Marketing Spend
mMS = smf.ols('Pft ~ MS', data=start).fit()


# In[91]:


#summary of Marketing Spend model
mMS.summary()


# In[97]:


#build final model using both Marketing Spend and Admin
final_model = smf.ols ('Pft ~ MS + RD', data=start).fit()
final_model.summary()


# In[98]:


#plot the influence plot of m1 model
import statsmodels.api as sm
sm.graphics.influence_plot(m1)


# In[93]:


#drop most influencial data from start dataframe
start_new = start.drop(start.index[[49,48,46]], axis=0)


# In[94]:


#last 5 records of strat_new dataframe without 46th, 48th, 49th indexes
start_new.tail()


# In[95]:


start.tail()


# In[99]:


#build a final better model name finalM without most influencial data
finalM = smf.ols('Pft ~ MS + RD ', data=start).fit()


# In[100]:


finalM.summary()


# In[ ]:




