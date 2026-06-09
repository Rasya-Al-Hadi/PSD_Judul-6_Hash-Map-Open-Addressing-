Judul Program : Sistem Pencarian Buku di Perpustakaan

Deskripsi : Program ini bertujuan untuk mencari Nomor buku pada setiap rak di perpustakaan secara online. Program ini menggunakan Hash Map/Open Addressing yang  penyelesaian tabrakan (collision resolution) pada hash map yang banyak digunakan karena tidak memerlukan struktur data tambahan seperti linked list, sehingga lebih hemat ruang memori. Konsep dasar dari open addressing adalah seluruh data harus disimpan langsung ke dalam tabel hash, dan ketika sebuah kunci mengalami tabrakan, sistem tidak meletakkan elemen di luar tabel, melainkan melakukan pencarian slot kosong lain di dalam tabel itu sendiri.

Source Code : 
<img width="1770" height="4282" alt="Tugas Akhir 6" src="https://github.com/user-attachments/assets/b00dd687-5b6d-4a0a-84aa-a285b738074e" />

Baris 1: Membuat kelas SlotState untuk menyimpan status setiap slot pada hash table.

Baris 2: Mendefinisikan status EMPTY dengan nilai 0 yang menandakan slot masih kosong.

Baris 3: Mendefinisikan status OCCUPIED dengan nilai 1 yang menandakan slot sudah terisi data.

Baris 4: Mendefinisikan status DELETED dengan nilai 2 yang menandakan data telah dihapus.

Baris 7: Membuat kelas Entry sebagai representasi satu slot pada hash table.

Baris 8: Mendefinisikan konstruktor (__init__) untuk kelas Entry.

Baris 9: Menginisialisasi atribut kode_buku dengan nilai awal None.

Baris 10: Menginisialisasi atribut nomor_rak dengan nilai awal None.

Baris 11: Memberikan status awal slot sebagai EMPTY.

Baris 14: Membuat kelas Perpustakaan untuk mengelola data buku menggunakan hash table.

Baris 15: Mendefinisikan konstruktor kelas Perpustakaan dengan ukuran default 10 slot.

Baris 16: Menyimpan ukuran hash table ke dalam atribut SIZE.

Baris 17: Membuat list berisi objek Entry sebanyak ukuran hash table.

Baris 19: Mendefinisikan fungsi hash_function() untuk menghitung indeks penyimpanan buku.

Baris 20: Mengembalikan hasil perhitungan hash menggunakan operasi modulo.

Baris 22: Mendefinisikan fungsi tambah_buku() untuk menambahkan data buku.

Baris 23: Menghitung indeks awal berdasarkan kode_buku.

Baris 24: Menyiapkan variabel first_deleted dengan nilai awal -1.

Baris 25: Melakukan perulangan untuk mencari slot yang sesuai.

Baris 26: Menghitung indeks menggunakan metode Linear Probing.

Baris 27: Memeriksa apakah slot saat ini berstatus OCCUPIED.

Baris 28: Memeriksa apakah kode_buku sudah ada di dalam hash table.

Baris 29: Memperbarui nomor_rak jika kode buku sudah tersedia.

Baris 30: Mengembalikan nilai True karena proses pembaruan berhasil.

Baris 31: Memeriksa apakah slot memiliki status DELETED.

Baris 32: Memeriksa apakah belum ada slot DELETED yang disimpan.

Baris 33: Menyimpan indeks slot DELETED pertama yang ditemukan.

Baris 34: Menjalankan kondisi jika slot dalam keadaan kosong (EMPTY).

Baris 35: Memeriksa apakah sebelumnya ditemukan slot DELETED.

Baris 36: Menggunakan slot DELETED sebagai lokasi penyimpanan jika tersedia.

Baris 37: Menyimpan kode_buku ke dalam slot yang dipilih.

Baris 38: Menyimpan nomor_rak ke dalam slot yang dipilih.

Baris 39: Mengubah status slot menjadi OCCUPIED.

Baris 40: Mengembalikan nilai True karena penambahan data berhasil.

Baris 41: Mengembalikan nilai False jika tidak ada slot yang tersedia.

Baris 43: Mendefinisikan fungsi cari() untuk mencari data buku.

Baris 44: Menghitung indeks awal berdasarkan kode_buku.

Baris 46: Melakukan perulangan untuk proses pencarian data.

Baris 47: Menghitung indeks menggunakan Linear Probing.

Baris 49: Memeriksa apakah slot masih kosong.

Baris 50: Mengembalikan None jika data tidak ditemukan.

Baris 52: Memeriksa apakah slot berstatus OCCUPIED.

Baris 53: Memastikan kode_buku sesuai dengan data yang dicari.

Baris 54: Mengembalikan objek Entry yang ditemukan.

Baris 56: Mengembalikan None jika seluruh pencarian selesai tetapi data tidak ditemukan.

Baris 58: Mendefinisikan fungsi hapus() untuk menghapus data buku.

Baris 59: Mencari data buku yang akan dihapus.

Baris 61: Memeriksa apakah data buku tidak ditemukan.

Baris 62: Mengembalikan nilai False karena penghapusan gagal.

Baris 64: Mengubah status data menjadi DELETED sehingga dianggap telah dihapus.

Baris 65: Mengembalikan nilai True karena penghapusan berhasil.

Baris 67: Mendefinisikan fungsi tampilkan() untuk menampilkan isi hash table.

Baris 68: Menampilkan judul daftar penyimpanan buku.

Baris 70: Melakukan perulangan untuk setiap slot pada hash table.

Baris 71: Menampilkan nomor indeks slot.

Baris 73: Memeriksa apakah slot berstatus EMPTY.

Baris 74: Menampilkan tulisan "Kosong".

Baris 76: Memeriksa apakah slot berstatus DELETED.

Baris 77: Menampilkan tulisan "Data Dihapus".

Baris 79: Menjalankan kondisi jika slot berisi data.

Baris 80: Menampilkan kode_buku beserta nomor_rak penyimpanannya.

Baris 83: Mendefinisikan fungsi utama main().

Baris 84: Membuat objek Perpustakaan.

Baris 86: Menambahkan buku dengan kode 101 ke Rak A1.

Baris 87: Menambahkan buku dengan kode 111 ke Rak B2.

Baris 88: Menambahkan buku dengan kode 121 ke Rak C3.

Baris 89: Menambahkan buku dengan kode 102 ke Rak D1.

Baris 90: Menampilkan seluruh isi hash table.

Baris 91: Mencari buku dengan kode 111.

Baris 93: Menghapus buku dengan kode 101.

Baris 94: Menampilkan pesan bahwa proses penghapusan telah dilakukan.

Baris 95: Menampilkan kembali isi hash table setelah penghapusan.

Baris 97: Mencari buku dengan kode 102.

Baris 98: Memeriksa apakah hasil pencarian tidak bernilai None.

Baris 99: Menampilkan informasi kode buku dan nomor rak jika data ditemukan.

Baris 100: Menjalankan kondisi jika data tidak ditemukan.

Baris 101: Menampilkan pesan bahwa buku tidak ditemukan.

Baris 104: Memastikan fungsi main() hanya dijalankan ketika file dieksekusi secara langsung.

Baris 105: Memanggil fungsi main() untuk menjalankan seluruh program.

Output :
<img width="340" height="374" alt="Screenshot 2026-06-09 201702" src="https://github.com/user-attachments/assets/74055d09-36e7-43b5-a549-a5bb5dec1735" />

Penjelasan : Menampilkan 10 Slot yang dimana No 1-4 memiliki status Terisi/Occupied dan Yang lain Kosong/Empty karena hanya ditambahkan 4 Buah Buku. User menghapus Nomor buku yang diinginkan beserta Raknya, Kemudian status berubah menjadi Dihapus/Delete. User mencari Nomor Buku lain dan Kemudian ditemukan di Rak tersebut

Link Dokumentasi
