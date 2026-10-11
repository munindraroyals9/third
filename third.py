import pandas as pd
import os

# Create a sample DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob', 'Eve'],
    'Age': [28, 24, 35, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# Add a new row using pd.concat()
new_row = pd.DataFrame([{
    'Name': 'Charlie',
    'Age': 30,
    'City': 'San Francisco'
}])

df=pd.concat([df,new_row],ignore_index=True)
# Add a new row using pd.concat() v3
new_row_v3 = pd.DataFrame([{
    'Name': 'Michael',
    'Age': 28,
    'City': 'New York'
}])
df=pd.concat([df,new_row_v3],ignore_index=True)

df=pd.concat([df,new_row],ignore_index=True)


# Add a new row using pd.concat() v3
new_row_v4 = pd.DataFrame([{
    'Name': 'MUNI',
    'Age': 26,
    'City': 'KNP'
}])


#make sure the directory      exists
data_dir= 'data'
os.makedirs(data_dir,exist_ok=True)

#Define the file path
file_path=os.path.join(data_dir,'data.csv')

#save the DataFrame tp a csv file
df.to_csv(file_path,index=False)
print(f'DataFrame saved to {file_path}')
print(df)