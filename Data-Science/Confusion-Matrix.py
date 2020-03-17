#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Import Library
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_breast_cancer

#ロジスティック回帰モデルを使用
from sklearn.linear_model import LogisticRegression

#Pipelineに組み込む用
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#ホールドアウト法により分割
from sklearn.model_selection import train_test_split

#Confusion Matrixを評価指標として設定
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score,recall_score,f1_score


# In[5]:


#データセットの読込
dataset = load_breast_cancer()
X = pd.DataFrame(data=dataset.data,columns=dataset.feature_names)
t = pd.Series(data=dataset.target,name="t")

#特徴量の確認
print(f"X's shape:{X.shape}")
print(f"t's shape:{t.shape}")


# In[11]:


from IPython.core.display import display
display(X.join(t).head())


# In[12]:


#ホールドアウト法による分割
X_train,X_test,t_train,t_test = train_test_split(X,t,test_size=0.2,random_state=1)

#訓練データの確認
print(f"X-train's shape : {X_train.shape}")
print(f"t-train's shape : {t_train.shape}")

#検証データの確認
print(f"X-test's shape : {X_test.shape}")
print(f"t-test's shape : {t_test.shape}")


# In[13]:


#モデル学習
pipe_line = Pipeline([("scl",StandardScaler()),
                      ("pca",PCA(n_components=2)),
                      ("est",LogisticRegression())
                      ])

pipe_line.fit(X_train,t_train)


# In[49]:


#予測値の算出
y_pred = pipe_line.predict(X_test)

#Confusion Matrixの作成
labels = [1,0]
confmat = confusion_matrix(y_true=t_test,y_pred=y_pred,labels=labels)
print(confmat)
print("-------実際クラス--------")
print(t_test.value_counts())
print("-------予測クラス--------")
print(pd.Series(y_pred).value_counts())


# In[45]:


confmat2 = confusion_matrix(y_true=t_test,y_pred=y_pred)
confmat2


# In[77]:


confmat[0] #class1


# In[108]:


#Confusion Matrixのヒートマップ化
fig,ax = plt.subplots(figsize=(3,3))

ax.matshow(confmat,cmap=plt.cm.Blues,alpha=0.7)
for i in range(confmat.shape[1]):
    for k in range(confmat.shape[0]):
        ax.text(x=k,y=i,s=confmat[i,k],va="center",ha="center")

ax.set_xticklabels([""]+labels)
ax.set_yticklabels([""]+labels)
plt.xlabel("Predicted Class")
plt.ylabel("Actual Class")
plt.tight_layout()
plt.show()


# In[16]:


#Accuracy Scoreを用いた場合
score_accuracy = accuracy_score(t_test,y_pred)
print(f"ACC：{score_accuracy*100:.2f}%")

#Presicionを用いた場合
score_pre = precision_score(t_test,y_pred)
print(f"PRE：{score_pre*100:.2f}%")

#Recallを用いた場合
score_rec = recall_score(t_test,y_pred)
print(f"REC：{score_rec*100:.2f}%")

#F-Measureを用いた場合
score_f1 = f1_score(t_test,y_pred)
print(f"F-score：{score_f1*100:.2f}%")

