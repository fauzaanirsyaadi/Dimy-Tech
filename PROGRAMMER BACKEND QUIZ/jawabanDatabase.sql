-- buatkan tabel-tabel sederhana untuk menyimpan data transaksi (order), dengan ketentuan sebagai berikut :
-- 1. Satu transaksi bisa memiliki banyak produk
-- 2. Satu transaksi bisa memiliki banyak payment method
-- 3. Customer address pada transaksi harus mereferensi ke tabel customer_address

-- Tabel "order":
-- id (PK)
-- customer_id (FK)
-- customer_address_id (FK)

-- Tabel "order_product":
-- id (PK)
-- order_id (FK)
-- product_id (FK)
-- quantity

-- Tabel "order_payment":
-- id (PK)
-- order_id (FK)
-- payment_method_id (FK)

-- Dalam tabel "order", kolom "customer_id" merupakan foreign key ke kolom "id" pada tabel "customer_address" sedangkan kolom "customer_address_id" merupakan foreign key ke kolom "id" pada tabel "customer_address".
-- Dalam tabel "order_product", kolom "order_id" merupakan foreign key ke kolom "id" pada tabel "order", dan kolom "product_id" merupakan foreign key ke kolom "id" pada tabel "product".
-- Dalam tabel "order_payment", kolom "order_id" merupakan foreign key ke kolom "id" pada tabel "order", dan kolom "payment_method_id" merupakan foreign key ke kolom "id" pada tabel "payment_method".

-- Pada database dalam gambar 1 data antar tabel saling berelasi. Bagaimana solusi anda untuk menghandle kasus penghapusan data yang berelasi dengan tetap menjaga relevansi relasi antar data ?. Sebagai contoh jika data customer dihapus maka hal itu akan mengganggu pada relasi dengan tabel lainnya

-- Untuk mengatasi kasus penghapusan data yang berelasi, dapat dilakukan beberapa solusi seperti:

-- Menggunakan fitur "CASCADE DELETE" pada foreign key constraint. Dengan menggunakan fitur ini, ketika data pada tabel induk dihapus, maka secara otomatis data pada tabel anak yang berelasi dengan data di tabel induk juga akan dihapus. Namun, solusi ini harus digunakan dengan hati-hati dan mempertimbangkan konsekuensi dari penghapusan data tersebut.

-- Menonaktifkan fitur "CASCADE DELETE" pada foreign key constraint, dan menambahkan kode program atau prosedur yang akan menangani penghapusan data secara manual. Dalam prosedur ini, data pada tabel anak yang berelasi dengan data di tabel induk akan dihapus terlebih dahulu sebelum data di tabel induk dihapus.

-- Menggunakan fitur "Soft Delete". Dalam fitur ini, data yang dihapus tidak benar-benar dihapus dari database, melainkan ditandai sebagai "dihapus" dengan menambahkan kolom "deleted_at" pada setiap tabel. Data yang sudah dihapus tidak akan muncul pada aplikasi, tetapi data tersebut masih dapat dipulihkan jika diperlukan.

-- Menggunakan fitur "Database Transaction". Dalam fitur ini, semua proses penghapusan data akan dilakukan dalam satu transaksi. Jika terdapat kesalahan pada salah satu proses penghapusan data, maka transaksi tersebut akan dibatalkan dan data tidak akan terhapus. Dengan menggunakan fitur ini, integritas data antar tabel dapat dijaga dengan baik.

-- Buatlah API sederhana yang berfungsi untuk membuat data transaksi dengan mengimplementasikan desain database pada soal no 1.

-- Install dependencies yang dibutuhkan dengan menjalankan perintah berikut di terminal:
-- pip install -r requirements.txt
-- Jalankan aplikasi dengan menjalankan perintah berikut di terminal:
-- uvicorn main:app --reload