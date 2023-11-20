import random
import pandas as pd
import pandas as df
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
categories = data['whoAmI'].unique()
for i in categories:
    data[i] = (data['whoAmI'] == i).astype(int)
data = data.drop('whoAmI', axis=1)
data.head()
print (data)