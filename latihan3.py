import pandas as pd

df = pd.read_csv('data_kantin.csv')
print(df.head()) # 5 baris pertama
print(df.info()) # tipe data & jumlah non-null tiap kolom
print(df.describe()) # statistik ringkas kolom numerik
print(df.shape) # jumlah (baris, kolom)