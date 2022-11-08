import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.datasets import load_iris

iris = sns.load_dataset("iris")
print(iris)
print("=" * 30)

# 그래프 표시 
sns.set(style="ticks", color_codes=True)
g = sns.pairplot(iris, 
                 hue="species", 
                 palette="husl")

# 붓꽃 데이터 세트를 로딩합니다. 
iris = load_iris()

# iris.data는 Iris 데이터 세트에서 
# 피처(feature)만으로 된 데이터를 
# numpy로 가지고 있습니다. 
iris_data = iris.data
#print(iris_data)

# iris.target은 붓꽃 데이터 
# 세트에서 레이블(결정 값) 
# 데이터를 numpy로 가지고 있습니다. 
iris_label = iris.target
print('iris target값:', list(set(iris_label)))
print('iris target명:', iris.target_names)

# 붓꽃 데이터 세트를 자세히 보기 위해 
# DataFrame으로 변환합니다. 
iris_df = pd.DataFrame(data=iris_data, 
                       columns=iris.feature_names)
iris_df['label'] = iris.target
print(iris_df.head(10))

#훈련 데이터 / 테스트 데이터 나누기
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_data,iris_label, test_size=0.2,random_state=11)
    

# KNN을 이용한 품종 분류 
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1) 

