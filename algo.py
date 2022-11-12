import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
import pickle

def clean(x):
    x = x.lower()
    x = x.strip('.')
    x = x.strip(' ')
    return x

df = pd.read_csv('chatbot_data.csv')
df.head()
df = df.loc[:,['Company Address','Business Nature','Item Code']]
df.head()
a = list(np.random.randint(5, size=583))
df['Business product'] = a
df['Company Address'] = df['Company Address'].apply(clean)
df['Business Nature'] = df['Business Nature'].apply(clean)
unique_business_nature = df['Company Address'].unique()
unique_company_address = df['Company Address'].unique()
df.head()

for elem in df['Company Address'].unique():
    df[str(elem)] = df['Company Address'] == elem
for elem in df['Business Nature'].unique():
    df[str(elem)] = df['Business Nature'] == elem
df.head()
df = df.drop(['Company Address','Business Nature'],axis=1)
df_temp = df[df.columns.difference(['Item Code','Business product'])]
df_temp = df_temp.astype(int)

df1 = df_temp
df1['Business product'] = df['Business product']

y = df['Item Code']
df = df.drop('Item Code',axis=1)
X = df1

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1, random_state=42,shuffle=True)
print('Train test split done!')
import joblib

print('Training')
clf = GradientBoostingClassifier(n_estimators=20, learning_rate=0.01,max_depth=5, random_state=0).fit(X_train, y_train)
print('Testing')
filename = 'model.sav'
# pickle.dump(clf, open(filename, 'wb'))
joblib.dump(clf, filename)

loaded_model = joblib.load(filename)
print('done loading!')