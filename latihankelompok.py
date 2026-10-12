import pandas as pd

# =========================
# 1. LOAD DATA
# =========================

data = pd.read_csv("dataset_penjualan_kantin - dataset_penjualan_kantin.csv")

print("DATA AWAL")
print(data.head())

print("\nINFO DATA")
print(data.info())

print("\nDESKRIPSI DATA")
print(data.describe())

print("\nUKURAN DATA")
print(data.shape)


# =========================
# 2. CEK DATA
# =========================

print("\nMISSING VALUE")
print(data.isnull().sum())

print("\nJUMLAH DUPLIKAT")
print(data.duplicated().sum())


# =========================
# 3. CLEANING DATA
# =========================

# Mengisi data yang kosong
data["jumlah_terjual"] = data["jumlah_terjual"].fillna(0)
data["harga_satuan"] = data["harga_satuan"].fillna(0)
data["nama_kasir"] = data["nama_kasir"].fillna("Tidak Diketahui")

# Menyamakan penulisan kategori
data["kategori"] = data["kategori"].str.title()

# Menghapus data duplikat
data = data.drop_duplicates()

print("\nDATA SETELAH CLEANING")
print(data.head())


# =========================
# 4. KOLOM TURUNAN
# =========================

data["total_penjualan"] = (
    data["jumlah_terjual"] * data["harga_satuan"]
)

print("\nTOTAL PENJUALAN")
print(data[[
    "nama_produk",
    "jumlah_terjual",
    "harga_satuan",
    "total_penjualan"
]].head())


# =========================
# 5. FILTER
# =========================

print("\nPENJUALAN DI ATAS 100.000")

filter_data = data[data["total_penjualan"] >= 100000]

print(filter_data[[
    "nama_produk",
    "total_penjualan"
]])


# =========================
# 6. SORTING
# =========================

print("\nPRODUK DENGAN JUMLAH TERJUAL TERBANYAK")

sort_data = data.sort_values(
    "jumlah_terjual",
    ascending=False
)

print(sort_data[[
    "nama_produk",
    "jumlah_terjual"
]].head(10))


# =========================
# 7. GROUPBY
# =========================

print("\nTOTAL PENJUALAN SETIAP PRODUK")

group_data = data.groupby(
    "nama_produk"
)["total_penjualan"].sum()

print(group_data.sort_values(ascending=False))


# =========================
# 8. KESIMPULAN
# =========================

produk_terlaris = data.groupby(
    "nama_produk"
)["jumlah_terjual"].sum().idxmax()

print("\nKESIMPULAN")
print("Produk yang paling banyak terjual adalah", produk_terlaris)


# =========================
# 9. SIMPAN DATA BERSIH
# =========================

data.to_csv(
    "dataset_bersih.csv",
    index=False
)

print("\nDataset bersih berhasil disimpan!")