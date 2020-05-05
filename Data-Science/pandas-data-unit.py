#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[72]:


#csvファイルの読み込み
data = pd.read_csv("./data/sell_prices.csv",encoding="utf-8")
display(data.head())

print(f"data's shape:{data.shape}")


# #### データサイズの確認方法

# In[3]:


#dfの全体像を把握
data.info()


# In[79]:


#dfの合計データサイズを確認
data.memory_usage().sum()


# In[5]:


#各カラムごとのデータサイズを確認
data.memory_usage()


# In[ ]:





# #### データ単位の変換方法

# In[85]:


#データサイズの単位変換方法
data_size = data.memory_usage().sum()

print(f"size:{data_size:.1f} Byte")
print(f"size:{data_size/1024:.1f} KB")
print(f"size:{data_size/1024**2:.1f} MB")
print(f"size:{data_size/1024**3:.1f} GB")


# In[13]:


#dfの合計データサイズの単位をBから「unit指定」に変換
def change_unit(df,unit="MB"):
    memory = df.memory_usage().sum()
    
    if unit == "MB":
        memory = memory / 1024**2
    elif unit == "GB":
        memory = memory / 1024**3
    else:
        memory = memory
    return memory


# In[28]:


data_mb = change_unit(data,unit="MB")
data_gb = change_unit(data,unit="GB")

print(f"Data-size:{data_mb:.1f} MB")
print(f"Data-size:{data_gb:.1f} GB")


# In[ ]:





# In[88]:


#各カラムのデータ単位を「MB」に変換して集計
def change_unit_cols(df,cols,unit="MB"):
    data_total = 0
    for col in cols:
        data_size = df[col].memory_usage()
        
        if unit == "MB":
            data_size_mb = data_size / 1024**2
            print(f"col:{col} | size:{data_size_mb:.1f} MB")
            data_total += data_size_mb
    print("------------")
    print(f"Data Total Size:{data_total:.1f} MB")


# In[89]:


cols = list(data.columns)
change_unit_cols(data,cols)


# In[ ]:




