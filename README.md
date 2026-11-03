# Aplikasi Sistem Perpustakaan

Aplikasi Sistem Perpustakaan merupakan aplikasi desktop berbasis Python yang digunakan untuk membantu pengelolaan data buku dan pengguna perpustakaan. Aplikasi ini menerapkan pola arsitektur Model-View-Controller (MVC), menggunakan Tkinter/CustomTkinter sebagai antarmuka dan MySQL sebagai database.

## Struktur Direktori

```text
Modul4_RPL/
├── models/                 # Pengelolaan data dan interaksi database
├── controllers/            # Pengaturan logika aplikasi
├── view/                   # Tampilan antarmuka aplikasi
├── tests/                  # File pengujian aplikasi
├── config/                 # Konfigurasi aplikasi dan database
├── .github/
│   └── workflows/          # Konfigurasi CI Pipeline
├── env/                    # Virtual environment
├── main.py                 # File utama untuk menjalankan aplikasi
├── requirements.txt        # Daftar dependensi Python
├── .gitignore              # Daftar file yang diabaikan Git
└── README.md               # Dokumentasi proyek
```

## Instalasi dan Konfigurasi Database

1. Pastikan Python dan Laragon sudah terpasang pada komputer.
2. Jalankan Laragon, kemudian aktifkan layanan MySQL.
3. Buka phpMyAdmin melalui Laragon.
4. Buat database dengan nama `perpustakaan`.
5. Pastikan konfigurasi koneksi database pada file `config/database.py` menggunakan pengaturan berikut:

   - Host: `127.0.0.1`
   - Port: `3306`
   - Database: `perpustakaan`
   - Username: `root`
   - Password: kosong (default Laragon).

## Cara Menjalankan Aplikasi

1. Buka folder proyek menggunakan Visual Studio Code.
2. Aktifkan virtual environment melalui terminal:

   ```powershell
   .\env\Scripts\Activate
   ```

3. Instal seluruh dependensi yang dibutuhkan:

   ```powershell
   pip install -r requirements.txt
   ```

4. Pastikan Laragon dan MySQL sedang berjalan.
5. Jalankan aplikasi dengan perintah:

   ```powershell
   python main.py
   ```

## Pengujian Aplikasi

Pengujian aplikasi dilakukan menggunakan Pytest untuk memeriksa fungsi-fungsi yang telah dibuat. Jalankan perintah berikut melalui terminal:

```powershell
python -m pytest -v
```

## CI Pipeline

Proyek ini menggunakan GitHub Actions sebagai bagian dari proses Continuous Integration (CI). Pipeline menjalankan pemeriksaan kualitas kode menggunakan Flake8 dan pengujian otomatis menggunakan Pytest setiap kali terdapat push atau pull request pada branch `main`.
