Tugas 1 :
Operasi perkalian pada list biasa akan error karena list Python tidak mendukung operasi matematika langsung dengan bilangan desimal (float), berbeda dengan NumPy array yang mengalikan tiap elemennya secara otomatis.
Tugas 2 : 
Kolom menu dan terjual. Risikonya bisa menyebabkan hasil analisis data menjadi tidak akurat atau memicu error saat perhitungan statistik.
Tugas 3 :
Kolom terjual. Artinya terdapat data yang kosong atau hilang (missing values) pada baris di kolom tersebut.
Tugas 4 : 
Kolom terjual diisi 0 karena data kosong diasumsikan tidak ada penjualan, sedangkan baris menu yang kosong dihapus karena tanpa nama menu data tersebut tidak valid untuk dianalisis
Tugas 5 : 
Jumlah baris berkurang 1 baris (dari 5 menjadi 4) setelah duplikat dihapus. Memastikan tipe data benar penting agar operasi matematika dan analisis data berjalan akurat tanpa menimbulkan error.
Tugas 6 :
Menu dengan pendapatan tertinggi adalah Nasi Goreng. Informasi ini membantu pengelola kantin untuk menambah stok bahan baku menu favorit dan mengevaluasi menu yang kurang laku.

Perencanaan Proyek Dataset yang Dipilih: ☑ Data Penjualan Kantin/Toko Pertanyaan Analisis Awal
Menu apa yang menghasilkan pendapatan tertinggi?
Menu apa yang paling banyak terjual?
Berapa total pendapatan dari penjualan kantin? Dugaan Masalah Kualitas Data
☑ Missing value pada kolom: menu dan terjual
☑ Duplikat data
☑ Tipe data tidak sesuai pada kolom: harga
☑ Lainnya: Data penjualan tidak lengkap Rencana Teknik Pembersihan Mengisi data penjualan kosong dengan 0, menghapus baris yang nama menunya kosong, menghapus data duplikat, dan memperbaiki tipe data harga menjadi integer. Rencana Manipulasi Data Filter: Penjualan lebih dari 20 Sort: Jumlah terjual dari terbesar ke terkecil Kolom turunan: total_pendapatan = harga × terjual Groupby/agregasi: Total pendapatan berdasarkan menu. Jadwal Kerja
P3 (Loading & Inspection): Memuat dan memeriksa dataset.
P4 (Cleaning): Membersihkan data kosong dan duplikat.
P5 (Manipulation): Memfilter, mengurutkan, dan menghitung pendapatan.
P6 (Uji & Presentasi): Menguji hasil dan mempresentasikan temuan. Pembagian Peran
Angga: Loading, inspection, dan cleaning.
Daffa: Manipulation, analisis, dan presentasi.
Lembar Refleksi Proyek
Tahap mana yang paling menantang dan bagaimana mengatasinya? Tahap cleaning paling menantang karena harus menentukan cara menangani data kosong dan duplikat dengan tepat. Kami mengatasinya dengan memeriksa data terlebih dahulu.
Mengapa keputusan membersihkan data harus memiliki alasan yang jelas? Agar data tetap akurat dan hasil analisis tidak salah atau menyesatkan.
Apa hubungan dataset bersih dengan pekerjaan Data Analyst? Dataset bersih membantu Data Analyst menghasilkan analisis yang akurat sehingga dapat digunakan untuk mengambil keputusan yang tepat.
