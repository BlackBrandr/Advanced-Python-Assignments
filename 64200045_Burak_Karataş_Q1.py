import pandas as pd

# Part A

dataframe = pd.read_csv("Automobiles.csv")
head = dataframe.head(10)
print(head)

# Part B

s = dataframe['body-style']
print(s)

# Part C

dataframe['Company-Price'] = dataframe.company + ' - ' + dataframe.price.astype(str)
print(dataframe)

# Part D

sub_dataframe = dataframe[['body-style', 'engine-type', 'length']]
print(sub_dataframe)

# Part E

dataframe.sort_values("price")
dataframe.sort_values("price", ascending = False)
print(dataframe.sort_values("price"))
print(dataframe.sort_values("price", ascending = False))

# Part F

dataframe['price'] = dataframe['price'].fillna(dataframe.groupby('company')['price'].transform('mean'))

# Part G

Hatch = (dataframe["body-style"] == "hatchback")|(dataframe["body-style"] == "wagon")
print(dataframe.loc[Hatch])

# Part H

rows = dataframe.loc[[0, 5, 7], :]
print(rows)

# Part I

print(dataframe.memory_usage(index=False,deep=True))
print(f'Total memory usage: {dataframe.memory_usage(deep=True).sum()}')
dataframe.drop(["Company-Price","company","body-style"], axis=1, inplace=True)
print(dataframe.memory_usage(index=False,deep=True))
print(f'Total memory usage after deletion of 3 features: {dataframe.memory_usage(deep=True).sum()}')
