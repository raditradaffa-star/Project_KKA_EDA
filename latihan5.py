import pandas as pd 
df = pd.read_csv('data_kantin.csv')

print(df.duplicated().sum()) # jumlah baris duplikat
df = df.drop_duplicates()
df['harga'] = df['harga'].astype(int) # memastikan tipe data harga adalah integer
print(df.dtypes)