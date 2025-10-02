# Markdown to PDF Converter

Program Python sederhana untuk mengubah file **Markdown (.md)** menjadi **PDF** dengan format rapi (font Times New Roman 13pt, line spacing 1.5, margin 2.54 cm, dan nomor halaman otomatis).

## ✨ Fitur
- ✅ Konversi file Markdown menjadi PDF.
- ✅ Margin standar **2.54 cm** (seperti Word).
- ✅ Font **Times New Roman 13pt** dengan line spacing **1.5**.
- ✅ Nomor halaman otomatis di footer.
- ✅ `.gitignore` untuk mengecualikan virtual environment dan file cache Python.

## 🛠️ Persyaratan
- Python 3.8+
- [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) (sudah harus di-install di Windows dan path-nya sesuai)
- Modul Python:
  - `markdown`
  - `pdfkit`

## ⚙️ Instalasi & Persiapan

1. **Clone repository** (atau salin folder ini):
   ```bash
   git clone https://github.com/username/md_to_pdf.git
   cd md_to_pdf
   ```

2. **Buat virtual environment & aktifkan**:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install library Python yang dibutuhkan**:

   ```bash
   pip install markdown pdfkit
   ```

4. **Install wkhtmltopdf** (jika belum ada):

   * Unduh di [wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)
   * Install dan pastikan path ke `wkhtmltopdf.exe` (misal: `S:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe`).

> Jika tidak masuk PATH otomatis, atur path di dalam kode `md_to_pdf.py` pada variabel `path_wkhtmltopdf`.

## 🚀 Cara Pakai

1. Simpan file Markdown yang ingin dikonversi di root folder, misalnya `USER_GUIDE.md`.
2. Jalankan program:

   ```bash
   python md_to_pdf.py
   ```
3. PDF akan dibuat dengan nama `USER_GUIDE.pdf` di folder yang sama.

## 📝 Struktur Folder

```
md_to_pdf/
├── md_to_pdf.py      # Script utama konversi Markdown → PDF
├── USER_GUIDE.md     # Contoh file markdown yang akan diubah ke PDF
├── .gitignore        # Mengabaikan venv & file sampah lain
└── README.md         # Dokumentasi proyek
```

## ⚡ Catatan

* Jika ingin menyesuaikan style PDF (font, margin, line spacing, header/footer), ubah bagian **CSS** di dalam `html_template` pada file `md_to_pdf.py`.
* wkhtmltopdf wajib terinstal karena pdfkit hanya sebagai wrapper.

---

Dikembangkan untuk kebutuhan dokumentasi internal yang rapi dan mudah dibagikan dalam bentuk PDF.