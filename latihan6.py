import pandas as pd
df = pd.read_csv('data_kantin.csv')

laris = df[df['terjual'] > 20] # filtering
urut = df.sort_values(by='terjual', ascending=False) # sorting
df['total_pendapatan'] = df['harga'] * df['terjual'] # kolom turunan
ringkasan = df.groupby('menu')['total_pendapatan'].sum() # agregasi
print(ringkasan)