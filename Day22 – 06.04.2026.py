import pandas as pd
import numpy as np

# pandas
import pandas as pd
import numpy as np

## pandas Series
ser = pd.Series(data=[4, 5, 6], index=[0, 1, 2])

### Selection
ser[0]            # by index
ser.iloc[0]       # by position
ser[ser == 4]     # boolean filtering


## pandas DataFrame
df = pd.DataFrame(
    data=np.random.randn(3, 3),
    index=[1, 2, 3],
    columns=['a', 'b', 'c']
)

### Selection
df['a']                      # single column
df[['a', 'b']]              # multiple columns
df.loc[1]                   # single row (by index)
df.loc[[1, 2]]              # multiple rows
df.loc[1, 'a']              # single value
df.loc[[1, 2], ['a', 'b']]  # sub-dataframe
df.head(2)                  # first n rows


### Row & Column Operations
df['d'] = df['a'] + df['b']     # create new column
df['d'] = [1.2, 1.3, 1.4]       # assign column directly

df.loc[4] = df.loc[1] + df.loc[2]  # create new row (calculated)
df.loc[4] = [1, 1, 1, 1]           # assign row directly

df.drop('d', axis=1, inplace=True)  # drop column (axis=1 = column)
df.set_index('a', inplace=False)    # set column as index
df.reset_index()                    # reset index


### Filtering (Single Level)
df['a'] > 0
(df['a'] > 0).sum()              # count True values
df[df['a'] > 0]                  # filter rows

df['a'].unique()                 # unique values
df['a'].nunique()                # number of unique values
df['a'].value_counts()           # frequency count

df.dropna(axis=1, thresh=1)      # keep columns with >=1 non-NaN
df.fillna(value=1)               # fill NaN
df.isnull()                      # detect NaN


### MultiIndex
df.index.names = ['A', 'B']      # name index levels

df.loc[('g1', 1), 'a']           # access one element
df.xs(1, level='B')              # cross-section by level


### Table Operations
# Grouping
df.groupby('a').mean()
df.groupby('a').size()           # count

# Combining
pd.concat([df1, df2, df3], axis=1)#type:ignore
pd.merge(left, right, on='key', how='inner')
left.join(right)                 # join on index

# Sorting
df.sort_values(by='a')

# Apply function
df.apply(lambda x: x * 2)

# Basic stats
df.count()
df.describe()


### Data Input / Output

#### Input
pd.read_csv('example.csv')
pd.read_excel('excel.xlsx', sheet_name='sheet1')
pd.read_html('http://example.com')

from sqlalchemy import create_engine
engine = create_engine('your_database_connection_string')

#### Output
pd.read_sql('SQL query', con=engine)
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', sheet_name='sheet1')
df.to_sql('table_name', engine)