# ## Problem Set 4
# Zehua Wang wangzeh@umich.edu

# ## Imports

import pandas as pd

# ## Question 0 - Topics in Pandas [25 points]

# ## Data Cleaning

# Create sample data
df = pd.DataFrame(
    {
        'col1': range(5),
        'col2': [6, 7, 8, 9, np.nan],
        'col3': [("red", "black")[i % 2] for i in range(5)],
        'col4': [("x", "y", "z")[i % 3] for i in range(5)],
        'col5': ["x", "y", "y", "x", "y"]
    }
)
df

# ### Duplicated Data
# - Find all values without duplication
# - Check if there is duplication using length comparison
# - return true if duplication exists

df['col3'].unique()
len(df['col3'].unique()) < len(df['col3'])

# ### Duplicated Data
# - Record duplication
# - subset: columns that need to remove duplication. Using all columns
#   if subset is None.
# - keep: Determine which duplicates to keep (if any), 'first' is default
#     - 'first': drop duplications except the first one
#     - 'last': drop duplications except the last one
#     - False: drop all duplications
# - inplace: return a copy (False, default) or drop duplicate (True)
# - ignore_index: return series label 0, 1, ..., n-1 if True, default is False

df.drop_duplicates()
df.drop_duplicates(subset=['col3'], keep='first', inplace=False)
df.drop_duplicates(subset=['col4', 'col5'], keep='last')

# ### Missing Data
# - Check if there is missing value
# - Delete missing value: pd.dropna
#     - axis: 0, delete by row; 1, drop by column
#     - how: any, delete if missing value exist; all, delete if 
#         all are missing values
#     - inplace: return a copy (False, default) or drop duplicate (True)    

df.isnull().any() # pd.notnull for selecting non-missing value
df.dropna(axis=0, how='any')

# ### Missing Data
# - Replcae missing value: pd.fillna
#     - value: the value filled up for missing value
#     - method: how to fill up the missing value
#         - 'backfill'/'bfill': using next valid observation
#         - 'pad'/'ffill': using previous valid observation
#         - None is by default
# - Generally, we could fill up the missing value with mean or median
#     for numeric data, and mode in categorical data.

df.fillna(method='ffill')
df.fillna(value=np.median(df[df['col2'].notnull()]['col2']))
