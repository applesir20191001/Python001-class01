import pandas as pd
import numpy as np
# 1. SELECT * FROM data;
group = ['x', 'y', 'z']
data = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 20)],
    "salary": np.random.randint(5, 50, 20),
    "age": np.random.randint(15, 50, 20)
})
data1 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 10)],
    "salary": np.random.randint(5, 50, 10),
    "age": np.random.randint(15, 50, 10)
})
print(data)
print(data1)

# 2. SELECT * FROM data LIMIT 10;
df2 = data.head(10)
print(df2)

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
df3 = data['group']
print(df3)

# 4. SELECT COUNT(id) FROM data;
df4 = data['salary'].count()
print(df4)

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
df5 = data[(data['salary'] < 45) & (data['age'] > 20)]
print(df5)

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
df6 = data.drop_duplicates(['group', 'salary']).groupby(
    'group').agg({'salary': pd.Series.nunique})
print(df6)
df6 = data.groupby('group')['salary'].nunique()
print(df6)

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
df7 = pd.merge(data, data1, on='group', how='inner')
print(df7)

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
df8 = pd.concat([data, data1])
print(df8)

# 9. DELETE FROM table1 WHERE id=10;
df9 = data.drop(data[data['group'] == 'y'].index, axis=0)
print(df9)

# 10. ALTER TABLE table1 DROP COLUMN column_name;
df10 = data.drop('group', 1)
print(df10)
print(data)
data.drop('group', axis=1, inplace=True)
print(data)
