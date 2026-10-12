import pandas as pd

# Load dataset terlebih dahulu
df = pd.read_csv('data_kantin.csv')

# Kode latihan4.py kamu
print(df.isnull().sum()) # jumlah data kosong tiap kolom
df['terjual'] = df['terjual'].fillna(0) # isi kekosongan dengan 0
df = df.dropna(subset=['menu']) # hapus baris jika kolom menu kosong