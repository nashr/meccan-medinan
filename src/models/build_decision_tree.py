# import graphviz
import pandas as pd
from sklearn import tree

target = "is_meccan"
df = pd.read_csv("data/processed/feature.csv")
X = df.drop(columns=target)
y = df[target]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
print(clf.score(X, y))
# print(X.columns)
# print(clf.feature_importances_)
# print(tree.plot_tree(clf, feature_names=X.columns))
# dot_data = tree.export_graphviz(clf, out_file="src/models/tree.png")
