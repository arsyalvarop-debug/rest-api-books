
# REST API Manajemen Buku

REST API sederhana untuk mengelola data buku menggunakan Python, Flask, dan SQLite.

## Fitur
- Melihat semua buku
- Melihat detail buku berdasarkan ID
- Menambahkan buku
- Mengubah data buku
- Menghapus buku

## Teknologi
- Python
- Flask
- SQLite
- Thunder Client untuk pengujian API

## Cara Menjalankan
1. Clone repository.
2. Buat dan aktifkan virtual environment.
3. Install dependency dengan `pip install -r requirements.txt`.
4. Jalankan aplikasi dengan `python app.py`.
5. Buka `http://127.0.0.1:5000`.

## Endpoint API

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | /books | Melihat semua buku |
| GET | /books/<id> | Melihat detail buku |
| POST | /books | Menambahkan buku |
| PUT | /books/<id> | Mengubah buku |
| DELETE | /books/<id> | Menghapus buku |

## Format Data Buku

{
  "title": "Belajar Python",
  "author": "Arsy",
  "publisher": "Buku Teknologi",
  "year": 2026,
  "isbn": "9781234567890"
}
