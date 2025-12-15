import pandas as pd
import pandasql as ps

file_path = ('books_hdr.csv')
df=pd.read_csv(file_path)
print(df)

query="select * from df where price > 400"
result=ps.sqldf(query)
print(result)

