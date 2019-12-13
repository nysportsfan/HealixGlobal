#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd


# In[36]:


dcm = pd.read_excel(r'G:\Market response\Vyleesi\Consumer\DTC October 2019\Data\October Master GA DCM Worksheet 11.19.xlsx',
                    sheet_name='Formatted Data'
                    )


# In[37]:


dcm.columns


# In[38]:


dcm.columns[0:14]


# In[39]:


dcm = dcm[dcm.columns[0:14]]


# In[40]:


dcm


# In[41]:


ga = pd.read_excel(r'G:\Market response\Vyleesi\Consumer\DTC October 2019\Data\October Master GA DCM Worksheet 11.19.xlsx',
                    sheet_name='GA Data'
                    )


# In[42]:


ga.columns


# In[43]:


join = pd.merge(dcm,ga,on=['Placement ID','Creative ID', 'Month of the year'])


# In[44]:


join[0:9]


# In[ ]:




