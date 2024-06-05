#!/usr/bin/env python
# coding: utf-8

# In[1]:


data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
print(data)


# In[2]:


import numpy as np

grades = np.array(data)
print(grades)


# In[3]:


print (type(data),'x 2:', data * 2)
print('---')
print (type(grades),'x 2:', grades * 2)


# In[4]:


grades.shape


# In[5]:


grades[0]


# In[6]:


# Define an array of study hours
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

# Create a 2D array (an array of arrays)
student_data = np.array([study_hours, grades])

# display the array
student_data


# In[7]:


# Show shape of 2D array
student_data.shape


# In[8]:


# Get the mean value of each sub-array
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()

print('Average study hours: {:.2f}\nAverage grade: {:.2f}'.format(avg_study, avg_grade))


# In[9]:


import pandas as pd

df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1]})

df_students 


# In[10]:


# Get the data for index value 5
df_students.loc[5]


# In[11]:


# Get the rows with index values from 0 to 5
df_students.loc[0:5]


# In[ ]:





# In[ ]:




