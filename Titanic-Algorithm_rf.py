#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Import Library
import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# In[ ]:





# ##### 訓練データとテストデータの読込

# In[6]:


dataset_train = pd.read_csv("./data/train.csv",encoding="utf-8")
dataset_test = pd.read_csv("./data/test.csv",encoding="utf-8")


# In[7]:


dataset_train.head()


# In[12]:


print(f"dataset(Train)'s shape:{dataset_train.shape}'")
print(f"dataset(Test)'s shape:{dataset_test.shape}'")


# ##### 訓練データXと教師ラベルyの設定(+不要特徴量の削除)

# In[14]:


X = dataset_train.iloc[:,2:].drop(["Name","Ticket","Cabin"],axis=1)
y = dataset_train.iloc[:,1]
X.head()


# In[ ]:





# ##### 前処理①(カテゴリ変数のOne-hotエンコーディング処理)

# In[10]:


ohe_columns = ["Pclass","Sex","Embarked"]
X_ohe = pd.get_dummies(X,columns=ohe_columns,dummy_na=True)
X_ohe.head()


# In[11]:


print(f"X_ohe's shape:{X_ohe.shape}")


# In[ ]:





# ##### 前処理②(数値変数の欠損補完)

# In[13]:


X_ohe.isnull().sum()


# In[16]:


imp = SimpleImputer()
imp.fit(X_ohe,y)

X_ohe2 = pd.DataFrame(imp.transform(X_ohe),columns=X_ohe.columns)
X_ohe2.head()


# In[17]:


X_ohe2.isnull().sum()


# In[28]:


print(f"X_ohe2's shape:{X_ohe2.shape}")


# In[ ]:





# ##### Build Model(Random Forest) +  Grid Search適用

# In[19]:


grid_params = {
    "n_estimators" : [50,100,200,300],
    "max_depth" : [3,4,8,10,20]
}

gs = GridSearchCV(
    estimator = RandomForestClassifier(),
    param_grid = grid_params,
    scoring="accuracy",
    cv= 10)

gs.fit(X_ohe2,y)


# In[21]:


print(gs.best_params_)
print(gs.best_score_)


# In[ ]:





# ##### テストデータの加工

# In[31]:


X_test = dataset_test.iloc[:,1:].drop(["Name","Ticket","Cabin"],axis=1)
passenger_id = dataset_test["PassengerId"]
X_test.head()


# In[24]:


X_test_ohe = pd.get_dummies(X_test,columns=ohe_columns,dummy_na=True)
X_test_ohe.head()


# In[25]:


X_test_ohe.isnull().sum()


# In[26]:


X_test_ohe2 = pd.DataFrame(imp.transform(X_test_ohe),columns=X_test_ohe.columns)
X_test_ohe2.isnull().sum()


# In[27]:


print(f"X_test's shape : {X_test_ohe2.shape}")


# In[ ]:





# ##### テストデータの予測

# In[36]:


y_test = gs.predict(X_test_ohe2)


# In[37]:


y_test


# In[ ]:





# ##### Preparation for Submit

# In[46]:


df = pd.DataFrame(y_test,columns=["Survived"])
df = pd.concat([passenger_id,df],axis=1)
df.to_csv("gender_submission_test.csv",index=False)


# In[ ]:




