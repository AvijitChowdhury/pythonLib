import numpy as np
from sklearn.datasets import load_boston

import pandas as pd

boston_dataset = load_boston()

type(boston_dataset)

print(boston_dataset)

boston_df = pd.DataFrame(boston_dataset.data,columns=boston_dataset.feature_names)

boston_df.head()
