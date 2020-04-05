#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import time


# In[ ]:





# ###### リスト作成時間の比較

# In[37]:


iters = 100000000 #1億

time_start = time.time()
lis = [i for i in range(iters)]
time_end = time.time()
print("Time by using python list : {:.2f} second".format(time_end - time_start))


# In[38]:


time_start = time.time()
ary = np.arange(iters)
time_end = time.time()
print("Time by using numpy : {:.2f} second".format(time_end - time_start))


# In[ ]:





# ###### 要約統計量の算出時間の比較

# In[58]:


time_start = time.time()
lis_max = max(lis)
time_end = time.time()
print("Time by using python list : {:.2f} second".format(time_end - time_start))
print(lis_max)


# In[59]:


time_start = time.time()
ary_max = np.max(ary)
time_end = time.time()
print("Time by using numpy : {:.2f} second".format(time_end - time_start))
print(ary_max)

