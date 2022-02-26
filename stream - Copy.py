import streamlit as st
from sklearn import datasets
import pandas
import numpy as np
from sklearn.utils import Bunch
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import  RandomForestClassifier
from sklearn.svm import SVC
import sklearn as sk
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns



# we can cache the data need to check that out
# we can refer this website https://docs.streamlit.io/en/stable/ for the data
st.title("First Streamlit App")
# with # in the write the font size increases
st.write("""
# Explore the classifier 
Which is best?""") # for writing on the page

# to give a textbox
dataset_name = st.sidebar.selectbox("Select Dataset",("Iris", "Breast Cancer", "Wine dataset", "Drug"))

# and to write we
# st.write(dataset)

classifier_name = st.sidebar.selectbox("Select Classifier", ("KNN", "Decision Trees", "Random Forest", "SVM"))

def get_dataset(dataset_name):
    if dataset_name == "Iris":
        data = datasets.load_iris()

    elif dataset_name =="Breast Cancer":
        data = datasets.load_breast_cancer()

    elif dataset_name == "Wine dataset":
        data = datasets.load_wine()

    else:
        datas = pandas.read_csv('C:\\Datasets\\drugs.csv')

        x = datas[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values

        # In order to apply our model we need to encode the data   for the columns with categorical data
        # We can convert continuous data to categorical using pd.cut as shown below
        # result_labels = pd.cut(data1.Age, bins=[2,5,17, 65, 99] labels=['Baby', 'Child', 'Adult', 'Elder])
        # data1.insert(5, 'Result_labels', result_labels)  to insert the column
        # make sure that the bin can only in int or floats


        # steps to convert categorical to continuous data
        unique = datas['Drug'].unique()
        datas['Sex'] = pandas.factorize(datas.Sex)[0] # indicating to begin with 0 num
        datas['BP'] = pandas.factorize(datas.BP)[0]
        datas['Cholesterol']= pandas.factorize(datas.Cholesterol)[0]
        datas['Drug']= pandas.factorize(datas.Drug)[0]
        # whenever a new dataset is imported then bunch up using sklearn.utils.bunch which makes keys computable


        data =Bunch(data =datas[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values, target = datas[['Drug']].values,
                    target_names=unique)

    # splitting the data
    x = data.data
    y = data.target
    names = data.target_names
    return x, y, names





X, y, names = get_dataset(dataset_name)
st.write("Shape of the dataset", X.shape)
st.write("Number of classes :", len(np.unique(y)))
st.text(" ") # for giving space
df = pandas.DataFrame({'Class Names':names})
df.index+=1
st.write(" Target classes:",df)

# tes = [st.write(i) for i in names]
def add_parameter_ui(clf_name):
    params = dict()
    if clf_name=="KNN":
        K = st.sidebar.slider("K", 1, 30)
        params["K"] = K

    elif clf_name=="SVM":
        C = st.sidebar.slider("C", 0.01, 10.0)
        params["C"] = C

    elif clf_name=="Decision Trees":
        criterion = st.sidebar.selectbox("criterion",('gini', 'entropy'))
        splitter = st.sidebar.selectbox("splitter", ('best', 'random'))
        max_depth = st.sidebar.slider("max_depth",2, 15)
        min_samples_split = st.sidebar.slider("min_samples_split", 2, 15)
        min_samples_leaf = st.sidebar.slider("min_samples_leaf", 2, 15)

        params["criterion"] = criterion
        params["splitter"] = splitter
        params["max_depth"] = max_depth
        params["min_samples_split"] = min_samples_split
        params["min_samples_leaf"] = min_samples_leaf
    else :
        max_depth = st.sidebar.slider("max_depth",2, 15)
        n_estimators = st.sidebar.slider("n_estimators", 1, 100)
        params["max_depth"] = max_depth
        params["n_estimators"] = n_estimators

    return params

params = add_parameter_ui(classifier_name)

def get_classifier(clf_name, params):
    if clf_name == "KNN":
        clf = KNeighborsClassifier(n_neighbors=params["K"])

    elif clf_name == "SVM":
        clf = SVC(C=params["C"])

    elif clf_name == "Decision Trees":
        clf = DecisionTreeClassifier(criterion=params["criterion"],
        splitter=params["splitter"], max_depth=params["max_depth"],
         min_samples_split=params["min_samples_split"], min_samples_leaf=params["min_samples_leaf"])
    else:
        clf = RandomForestClassifier(n_estimators=params["n_estimators"], max_depth=params["max_depth"])

    return clf

classi = get_classifier(classifier_name, params)

# splitting the data

x_train, x_test, y_train, y_test = sk.model_selection.train_test_split(X, y, test_size=0.2, random_state=42)

classi.fit(x_train, y_train)

y_pred = classi.predict(x_test)

acc = accuracy_score(y_test, y_pred)

st.write("Classifier =",classifier_name)
st.write("Accuracy =",acc)
tes = [str(i) for i in names]
# Plots
pca = PCA(2) #  2 for dimension

x_projection = pca.fit_transform(X) # this is a transformer  like StandardScalar, MinMax

x1 = x_projection[:, 0] # THERE ARE TWO COLUMNS AND THIS IS THE FIRST ONE

x2 = x_projection[:, 1]

fig = plt.figure(figsize=(10, 10))
plt.scatter(x1, x2, c=y, alpha=0.8, cmap="viridis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar()
plt.legend( [names[y] for  y in range(len(names))],loc="upper right")

#plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False) #this line is highly important
st.pyplot()


# fix the drug related problem


