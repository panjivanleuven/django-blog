# 🚀 My Awesome Project

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue)

> Aplikasi Django sederhana untuk manajemen tugas harian.

---

## Daftar Isi

- [Deskripsi Proyek](#deskripsi-proyek)
- [Fitur](#fitur)
- [Cara Menggunakan](#cara-menggunakan)
- [Screenshots](#screenshots)
- [Teknologi](#teknologi)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

---

## Deskripsi Proyek

My Awesome Project adalah aplikasi berbasis web untuk membantu Anda mengelola tugas harian. Aplikasi ini dibangun menggunakan Django dan PostgreSQL.

---

## Fitur

- ✅ Autentikasi pengguna dengan OAuth.
- ✅ CRUD tugas dengan antarmuka yang responsif.
- ✅ Notifikasi email untuk deadline tugas.

---

## Cara Menggunakan

### Prasyarat

- Python >= 3.8
- PostgreSQL

### Instalasi

```bash
# Clone repositori
git clone https://github.com/username/repo.git
cd repo

# Buat virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Jalankan migrasi
python manage.py migrate

# Jalankan server
python manage.py runserver
