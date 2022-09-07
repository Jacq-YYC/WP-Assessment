import json
import pandas as pd

with open("sample_data.json") as data_file:
    data = json.load(data_file)

df = pd.json_normalize(data, 'Employees' )
print(df)

df['salary'] = df['salary'].str.replace(',', '').astype(float)
result = df.groupby(['region', 'jobTitleName'])['salary'].mean()

# to generate output file with the result
result.to_json('average_salary.json')
