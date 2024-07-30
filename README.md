# 🔐 Password Manager

## Apa Itu Kriptografi? 🤔

Kriptografi adalah teknik untuk melindungi data dengan mengubah informasi menjadi bentuk yang tidak dapat dibaca tanpa kunci khusus. Ini penting untuk menjaga keamanan kata sandi dan informasi sensitif Anda dari akses yang tidak sah. Dalam kriptografi:

- **Kunci (Key)** adalah informasi rahasia yang digunakan untuk mengenkripsi dan mendekripsi data.
- **IV (Initialization Vector)** adalah nilai tambahan yang digunakan bersama dengan kunci untuk memastikan bahwa enkripsi tidak dapat diprediksi.

## Fitur Utama 🌟

- **Generate Key** 🗝️: 
  - Buat kunci enkripsi AES-128 dan IV dengan tombol "Generate Key".
  
- **Save Key** 💾:
  - Simpan kunci dan IV ke file untuk digunakan nanti dengan tombol "Simpan Key".
  
- **Load Key** 📂:
  - Muat kunci dan IV dari file yang sudah ada dengan tombol "Load Key".
  
- **Save Password** 🔒:
  - Masukkan kata sandi dan simpan dalam bentuk terenkripsi menggunakan tombol "Simpan Kata Sandi".
  
- **Load Password** 🧩:
  - Ambil kata sandi terenkripsi dan lihat hasil dekripsinya dengan tombol "Ambil Kata Sandi".

## Cara Menjalankan Aplikasi 🚀

### 1. Instalasi Python 🐍

Pastikan Anda memiliki Python versi 3.6 atau lebih baru terinstal di sistem Anda. Anda dapat mengunduh Python dari [situs resmi Python](https://www.python.org/downloads/).

### 2. Instalasi Dependensi 📦

Setelah Python terinstal, Anda perlu menginstal beberapa dependensi yang diperlukan oleh aplikasi. Buka terminal atau command prompt dan jalankan perintah berikut:
pip install tkinter cryptography

### 3. Jalankan Aplikasi 🏃

Running aplikasi dapat dilakukan di terminal atau via IDE seperti Visual Studio Code (py password.py)
