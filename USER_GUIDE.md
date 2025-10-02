# **Panduan Pengguna - Sistem Inventaris Vokse Textile**

Selamat datang di panduan penggunaan aplikasi manajemen inventaris Vokse Textile. Aplikasi ini dirancang untuk membantu Anda melacak setiap roll kain secara akurat, mulai dari barang masuk hingga keluar, termasuk penanganan kasus-kasus khusus seperti barang rusak dan retur.

---

## **Bab 1: Persiapan Awal (Pengelolaan Data Master)**

Sebelum memulai transaksi, pastikan semua data referensi (Master Data) sudah lengkap. Data ini akan menjadi pilihan di form-form transaksi Anda.

* **Akses Menu Master:** Buka menu samping (ikon ☰ di pojok kiri atas) untuk menemukan semua menu pengelolaan data master.
* **Menambah Data:** Untuk setiap menu master (`Suppliers`, `Customers`, `Kategori Warna`, `Nama Warna`, `Jenis Kain`, `Rajut`), tekan tombol `+` di pojok kanan bawah untuk menambahkan data baru.
* **Aturan Pengisian:**
    * **Kategori:** Data `POLOS` dan `PRINT` sudah tersedia secara *default*.
    * **Kategori Warna, Warna, Jenis Kain, Rajut:** Wajib mengisi **Nama** dan **Singkatan** (misal: "Tua Special" -> `TUAS`). Singkatan ini sangat penting karena akan membentuk `LotID`.
    * **Warna:** Saat mendaftarkan warna baru, pastikan Anda memilih **Kategori** (`POLOS`/`PRINT`) dan **Kategori Warna** (`TUA`/`MUDA`, dll) yang sesuai.
    * **Suppliers & Customers:** Cukup isi nama dan informasi tambahan jika ada.

---

## **Bab 2: Alur Kerja Inti**

Ini adalah aktivitas utama yang akan Anda lakukan sehari-hari.

### **2.1. Penerimaan Barang (Inbound)**

Proses ini mencatat semua roll kain yang masuk dari supplier.

1.  **Buka Form Penerimaan:** Dari menu utama bawah, pilih **`Receiving Form`**.
2.  **Isi Data Surat Jalan (Header):**
    * **No Surat Jalan:** Masukkan nomor SJ fisik dari supplier. Sistem akan menolak jika nomor ini sudah pernah ada.
    * **Tanggal:** Otomatis terisi tanggal hari ini.
    * **Nama Pengisi:** Isi dengan nama Anda.
    * **Supplier:** Pilih dari daftar supplier yang sudah ada.
3.  **Tambah Lot:**
    * Di bagian "Related Lots", tekan **`New`**.
    * Isi semua spesifikasi teknis kain (`Kategori`, `Kategori Warna`, `Warna`, `Jenis Kain`, `Rajut`, `Besar Benang`, `Setting`, `Handfeel`, `GSM Minimal`).
    * `GSM Maksimal` akan otomatis terisi (`GSM Minimal` + 10).
4.  **Tambah Roll:**
    * Di dalam form Lot yang sedang Anda isi, gulir ke bawah ke bagian "Related Rolls" dan tekan **`New`**.
    * Isi `BrutoKG` (sesuai dokumen) dan `NettoKG_Receive` (sesuai hasil timbangan).
    * `StatusKualitas` otomatis diatur ke `AMAN`.
    * Anda bisa menekan `New` berulang kali untuk menambahkan beberapa roll dalam satu Lot.
5.  **Simpan:** Setelah semua Lot dan Roll sesuai SJ fisik selesai diinput, tekan `Save`.

### **2.2. Mencetak Label Barcode (ZPL)**

Setiap roll yang masuk **wajib** memiliki label barcode untuk pelacakan.

1.  Buka menu **`List Surat Jalan`**.
2.  Pilih (klik) Surat Jalan yang baru saja Anda buat.
3.  Anda akan masuk ke halaman detail. Cari kolom bernama **`ZPL_AllRolls`**.
4.  **Salin (Copy)** seluruh isi teks dari kolom tersebut.
5.  **Tempel (Paste)** teks tersebut ke dalam software printer Anda (**Zebra Setup Utilities**).
6.  Cetak label dan **tempelkan pada setiap roll kain yang sesuai.**
    * **PERHATIAN:** Proses penempelan label sangat krusial. Pastikan `RollID` pada label cocok dengan roll fisiknya. Kesalahan di sini akan menyebabkan data inventaris Anda kacau. Selalu lakukan pengecekan ulang.
    
    

### **2.3. Pengeluaran Barang (Outbound)**

Proses ini mencatat semua roll kain yang keluar karena dibeli oleh customer.

1.  Buka menu **`Outbound Form`**.
2.  **Isi Data Invoice (Header):**
    * **Tanggal:** Otomatis terisi hari ini.
    * **No Invoice:** Isi sesuai nomor invoice Anda.
    * **Nama Customer:** Pilih dari daftar customer yang sudah ada.
3.  **Tambah Roll yang Dijual:**
    * Di bagian "Related Outbounds", tekan **`New`**.
    * **Pindai (Scan)** QR code pada label roll yang akan dijual.
    * Pilih **`Tipe Keluar`**:
        * **`PENUH`**: Jika roll dijual utuh.
        * **`SEBAGIAN`**: Jika roll dipotong. Kolom `QtyKeluarKG` akan muncul dan **wajib diisi**.
4.  **Simpan & Konfirmasi:**
    * Setelah semua roll ditambahkan, tekan **`Save`**.
    * Aplikasi akan membawa Anda ke halaman detail. Tekan tombol **`Konfirmasi & Update Stok`** untuk memfinalisasi transaksi. Status roll akan otomatis ter-update.

---

## **Bab 3: Utilitas & Penanganan Kasus Khusus**

### **3.1. Mencari Roll (Fitur Paling Penting)**
Untuk mengetahui detail lengkap sebuah roll dengan cepat:
1.  Buka menu **`Cari Roll`**.
2.  Tekan ikon scan dan arahkan kamera ke QR code pada label roll.
3.  Aplikasi akan langsung menampilkan semua detailnya: spesifikasi, sisa stok, status, dan status kualitas.

### **3.2. Menangani Barang Rusak & Retur**

**A. Menandai Barang Rusak (Internal)**
Jika Anda menemukan roll yang rusak di gudang.
1.  Buka form **`Tandai Rusak`** dari menu.
2.  Pindai (scan) roll yang rusak, lalu tekan **`Save`**.
3.  Status kualitas roll tersebut akan otomatis berubah menjadi `Rusak Internal`.

**B. Membatalkan Status Rusak**
Jika roll yang ditandai rusak ternyata kondisinya baik.
1.  Buka form **`Batal Rusak`** dari menu.
2.  Pindai (scan) roll yang statusnya ingin dibatalkan, lalu tekan **`Save`**.
3.  Status kualitas roll akan kembali menjadi `AMAN`.

**C. Menerima Retur dari Customer**
1.  **Syarat:** Pastikan customer membawa Invoice asli dan label barcode pada roll masih utuh.
2.  Buka form **`Return from Customer`**.
3.  Isi **No. Surat Pengembalian**, pilih **Customer**, dan yang terpenting, pilih **Invoice Asli** dari daftar.
4.  Di bagian detail, tekan `New` dan pindai (scan) roll yang dikembalikan.
5.  Tekan **`Save`**. Stok roll tersebut akan otomatis kembali ke sistem dengan `StatusKualitas` = `Rusak Retur Customer`. **Tidak perlu cetak label baru.**

**D. Mengembalikan Barang ke Supplier**
Hanya roll yang berstatus `Rusak` (`Internal` atau `Retur Customer`) yang bisa dikembalikan.
1.  Buka form **`Return to Supplier`**.
2.  Isi **No. Surat Retur** dan pilih **Supplier**.
3.  Di bagian detail, tekan `New` dan pindai (scan) roll rusak yang akan dikembalikan.
4.  Tekan **`Save`**. Stok roll tersebut akan menjadi nol dan status kualitasnya berubah menjadi `Diretur ke Supplier`.

---

## **Bab 4: Laporan & Pelacakan**

Aplikasi ini menyediakan beberapa layar laporan untuk analisis.

* **`List Surat Jalan` & `List Invoice`:** Menampilkan daftar semua transaksi masuk dan keluar.
* **`Roll List`:** Menampilkan daftar **semua roll aktif** yang ada di gudang (yang statusnya bukan `HABIS` atau `DIRETUR`).
* **`Lot List`:** Menampilkan daftar semua Lot yang pernah dibuat.
* **`Daftar Roll Bermasalah`:** Menampilkan daftar semua roll yang status kualitasnya **bukan `Aman`**, dikelompokkan berdasarkan status masalahnya (`Rusak Internal`, `Rusak Retur Customer`, dll).
* **`Laporan Sumber Kerusakan`:** Menampilkan jejak histori **asal-muasal kerusakan** sebuah roll, meskipun statusnya saat ini sudah berubah.
* **`Laporan Mutasi Global (Ledger)`:** Ini adalah "Buku Besar" untuk **semua transaksi**. Anda bisa melihat riwayat lengkap setiap roll. Gunakan ikon **Corong (Filter)** di pojok kanan atas untuk mencari transaksi berdasarkan rentang tanggal.

---

### **Bab 5: Stock Opname (Proses Mingguan/Bulanan)**

Stock Opname adalah proses krusial untuk memastikan data stok di aplikasi cocok dengan jumlah fisik di gudang. Aplikasi ini menggunakan sistem **Sesi Opname** berbasis checklist untuk membuat prosesnya terstruktur, akurat, dan dapat dilacak.

#### **5.1. Memulai Sesi Stock Opname**

Proses ini biasanya dilakukan oleh Admin atau Kepala Gudang.

1.  **Buka Menu Sesi:** Dari menu utama, pilih **`Sesi Stock Opname`**.
2.  **Buat Sesi Baru:** Tekan tombol `+` untuk membuat sesi baru. Sebuah form akan muncul.
    * **Tanggal Mulai:** Otomatis terisi hari ini.
    * **Tipe Sesi:** Pilih salah satu:
        * **`Mingguan`**: Untuk pengecekan cepat. Di form isian, berat fisik akan otomatis terisi sesuai data sistem (penimbangan bersifat opsional).
        * **`Bulanan`**: Untuk pengecekan menyeluruh. Di form isian, berat fisik wajib diisi (wajib timbang ulang).
    * **Nama Pemeriksa:** Isi nama penanggung jawab opname.
3.  **Simpan Form.** Sebuah "wadah" sesi baru telah dibuat dengan status `Berlangsung`.

#### **5.2. Membuat Checklist Pekerjaan**

Setelah sesi dibuat, Admin harus membuat daftar roll yang perlu diperiksa.

1.  Masuk ke detail sesi yang baru saja dibuat.
2.  Anda akan melihat tombol besar di bagian atas: **`Mulai Sesi & Generate Checklist (BOT)`**.
3.  Tekan tombol ini. Sebuah pesan konfirmasi akan muncul.
4.  Setelah Anda konfirmasi, **sebuah Bot akan berjalan di latar belakang** untuk membuat checklist semua roll yang relevan (semua roll yang statusnya bukan `HABIS` atau `DIRETUR`).
    * Proses ini mungkin butuh beberapa saat. Checklist akan muncul di tab **"Belum Diperiksa"**.
    * Tombol `Mulai Sesi...` akan otomatis menghilang setelah ditekan untuk mencegah duplikasi.

#### **5.3. Pelaksanaan Opname oleh Operator**

Ini adalah alur kerja bagi operator di gudang.

1.  **Buka Sesi Aktif:** Buka `Sesi Stock Opname` dan pilih sesi yang statusnya `Berlangsung`.
2.  **Mulai Memindai (Scan):** Di dalam dashboard sesi, tekan tombol **`SCAN`**. Kamera akan aktif.
3.  **Pindai QR Code** pada label roll fisik yang ada di depan Anda.
4.  **Aplikasi akan otomatis** mencari roll tersebut di dalam checklist dan membuka **form isian** yang sesuai.
5.  **Isi Hasil Pemeriksaan:**
    * Pertanyaan pertama adalah **`Hasil Pemeriksaan`**.
        * Pilih **`Ditemukan`**: Jika roll fisik ditemukan. Kolom `BeratFisikKG` akan muncul.
        * Pilih **`Hilang`**: Jika roll yang ada di checklist tidak bisa Anda temukan fisiknya di gudang. Langsung tekan `Save`.
    * Jika Anda memilih `Ditemukan`, isi **`BeratFisikKG`**:
        * Untuk sesi **Mingguan**, kolom ini sudah terisi otomatis. Anda hanya perlu mengubahnya jika hasil timbangan berbeda.
        * Untuk sesi **Bulanan**, kolom ini **kosong dan wajib diisi** sesuai hasil timbangan.
6.  **Simpan Form.** Item yang baru saja Anda periksa akan otomatis **pindah dari tab "Belum Diperiksa" ke tab "Sudah Selesai"**.
7.  Ulangi proses scan untuk semua roll fisik yang Anda temukan.

#### **5.4. Menyelesaikan & Memfinalisasi Sesi**

Setelah semua roll yang ditemukan selesai dipindai, Admin atau Kepala Gudang harus memfinalisasi sesi.

1.  Buka kembali detail sesi opname.
2.  Periksa tab **"Belum Diperiksa"**. Item yang masih tersisa di sini adalah roll yang tercatat di sistem tapi tidak ditemukan fisiknya saat proses scan.
3.  Tekan tombol **`Tutup Sesi Opname`** (ikon gembok).
4.  Sebuah pesan konfirmasi akan muncul.
5.  Setelah Anda konfirmasi, sistem akan secara **otomatis memproses semua item yang tersisa di "Belum Diperiksa" sebagai `Hilang`**.
6.  Sesi akan terkunci (menjadi `READ_ONLY`) dan statusnya berubah menjadi `Selesai`.

---

### **Bagaimana Opname Mengubah Stok? Peran `StockAdjustmentLog`**

Setiap kali Anda menyimpan hasil opname (baik `Ditemukan` dengan berat berbeda, maupun `Hilang`), sebuah **Aksi** atau **Bot** akan berjalan di latar belakang dan membuat satu baris catatan baru di tabel **`StockAdjustmentLog`**.

* **Tabel `StockAdjustmentLog`** adalah "buku jurnal akuntansi" untuk semua perubahan stok yang *bukan* karena penjualan atau penerimaan awal. Ini berlaku untuk **Opname**, **Retur ke Supplier**, dan **Retur dari Customer**.

* **Cara Kerjanya:**
    * Catatan ini berisi `StokSistemKG` (stok sebelum opname) dan `StokFisikKG` (hasil opname).
    * Kolom `SelisihKG_Real` dihitung secara otomatis (`StokFisikKG` - `StokSistemKG`).
    * **Contoh:** Jika `StokSistemKG` adalah `20` dan Anda menginput `StokFisikKG` sebesar `19.6`, maka `SelisihKG_Real` akan dicatat sebagai `-0.4`.
    * Kolom `VC_NettoKG_Current` di tabel `Rolls` secara **otomatis dan real-time** akan membaca semua log penyesuaian ini dan menghitung ulang saldo stok terbaru. Inilah yang membuat stok Anda selalu akurat.

---

### **5.5. Laporan Hasil Stock Opname**

Anda bisa melihat hasil dari semua sesi opname di dua layar laporan utama:

* **`Laporan Global Opname`:**
    * Ini adalah pandangan "helikopter" yang menampilkan **ringkasan untuk setiap sesi opname**.
    * Anda bisa melihat berapa total item yang diperiksa, berapa yang `Sesuai`, berapa yang `Selisih Beratnya`, dan berapa yang `Hilang`, beserta total `Selisih KG` untuk sesi tersebut.
    * Klik pada salah satu baris untuk "mengebor" lebih dalam ke detail sesi tersebut.

* **`Laporan Rincian Selisih Opname`:**
    * Ini adalah pandangan "mikroskop" yang menampilkan **daftar detail setiap roll yang bermasalah** (`Selisih` atau `Hilang`) dari **semua sesi opname yang pernah ada**.
    * Laporan ini dikelompokkan per sesi, sehingga Anda bisa langsung melihat rincian roll mana saja yang menjadi penyebab selisih di sesi tertentu.