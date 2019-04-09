import pandas as pd
import csv
from collections import defaultdict
import pandas as pd
import seaborn as sns
import sklearn
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
# from sklearn.model_slection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import tree
from sklearn.tree import export_graphviz


disease_list = []
print("bubu")
def return_list(disease):
    disease_list = []
    match = disease.replace('^','_').split('_')
    ctr = 1
    for group in match:
        if ctr%2==0:
            disease_list.append(group)
        ctr = ctr + 1

    return disease_list

with open("Scraped-Data/dataset_uncleaned.csv") as csvfile:
    reader = csv.reader(csvfile)
    disease=""
    weight = 0
    disease_list = []
    dict_wt = {}
    dict_=defaultdict(list)
    for row in reader:

        if row[0]!="\xc2\xa0" and row[0]!="":
            disease = row[0]
            disease_list = return_list(disease)
            weight = row[1]

        if row[2]!="\xc2\xa0" and row[2]!="":
            symptom_list = return_list(row[2])

            for d in disease_list:
                for s in symptom_list:
                    dict_[d].append(s)
                dict_wt[d] = weight

    #print (dict_)
with open("Scraped-Data/dataset_clean.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    for key,values in dict_.items():
        for v in values:
            #key = str.encode(key)
            key = str.encode(key).decode('utf-8')
            #.strip()
            #v = v.encode('utf-8').strip()
            #v = str.encode(v)
            writer.writerow([key,v,dict_wt[key]])
columns = ['Source','Target','Weight']
data = pd.read_csv("Scraped-Data/dataset_clean.csv",names=columns, encoding ="ISO-8859-1")
data.head()
data.to_csv("Scraped-Data/dataset_clean.csv",index=False)
slist = []
dlist = []
with open("Scraped-Data/nodetable.csv","w") as csvfile:
    writer = csv.writer(csvfile)

    for key,values in dict_.items():
        for v in values:
            if v not in slist:
                writer.writerow([v,v,"symptom"])
                slist.append(v)
        if key not in dlist:
            writer.writerow([key,key,"disease"])
            dlist.append(key)
nt_columns = ['Id','Label','Attribute']
nt_data = pd.read_csv("Scraped-Data/nodetable.csv",names=nt_columns, encoding ="ISO-8859-1",)
nt_data.head()
nt_data.to_csv("Scraped-Data/nodetable.csv",index=False)
data = pd.read_csv("Scraped-Data/dataset_clean.csv", encoding ="ISO-8859-1")
data.head()
len(data['Source'].unique())
len(data['Target'].unique())
df = pd.DataFrame(data)
df_1 = pd.get_dummies(df.Target)
df_1.head()
df.head()
df_s = df['Source']
df_pivoted = pd.concat([df_s,df_1], axis=1)
df_pivoted.drop_duplicates(keep='first',inplace=True)
df_pivoted[:5]
len(df_pivoted)
cols = df_pivoted.columns
cols = cols[1:]
df_pivoted = df_pivoted.groupby('Source').sum()
df_pivoted = df_pivoted.reset_index()
df_pivoted[:5]
len(df_pivoted)
df_pivoted.to_csv("Scraped-Data/df_pivoted.csv")
x = df_pivoted[cols]
y = df_pivoted['Source']
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.33, random_state=42)
mnb = MultinomialNB()
mnb = mnb.fit(x_train, y_train)
mnb.score(x_test, y_test)
mnb_tot = MultinomialNB()
mnb_tot = mnb_tot.fit(x, y)
mnb_tot.score(x, y)
disease_pred = mnb_tot.predict(x)
disease_real = y.values
for i in range(0, len(disease_real)):
    if disease_pred[i]!=disease_real[i]:
        print ('Pred: {0} Actual:{1}'.format(disease_pred[i], disease_real[i]))

print ("DecisionTree")
dt = DecisionTreeClassifier()
clf_dt=dt.fit(x,y)
print ("Acurracy: ", clf_dt.score(x,y))
export_graphviz(dt,
                out_file='DOT-files/tree.dot',
                feature_names=cols)
