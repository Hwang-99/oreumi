from sklearn.datasets import load_iris
import pandas as pd
import mglearn

iris_dataset = load_iris()

from sklearn.model_selection import train_test_split #학습과 테스트 분리
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)

iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
hist_kwds={'bins: 20'}, s=60, alpha=8, cmap=mglearn.cm3)

