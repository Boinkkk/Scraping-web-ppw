# Detik Finance Web Scraper

Web scraper Python untuk mengekstrak artikel berita dari Detik Finance secara terstruktur, rapi, dan efisien.

## Fitur Utama

- **Ekstraksi Data Terfokus**: Hanya mengekstrak 4 atribut penting:
  1. `judul`: Judul artikel berita.
  2. `link`: URL artikel berita.
  3. `waktu`: Waktu/tanggal publikasi artikel.
  4. `isi_berita`: Teks isi artikel yang telah dibersihkan dari tag iklan, script, dan baca juga.
- **Anti-Duplikasi (Deduplication)**:
  - Mencegah link duplikat saat pengumpulan link (Tahap 1).
  - Link yang sudah pernah discrape dan tersimpan di file output (`hasil_scraping_detik.csv` / `hasil_scraping_detik.json`) otomatis **dilewati (SKIP)** pada tahap 2. Tidak ada request HTTP berulang untuk link yang sama.
  - Penyimpanan berkala (*incremental save*) untuk menjaga integritas data jika proses terhenti.
- **Dukungan Multi-Halaman Detik**: Otomatis menangani artikel Detik yang terpotong menjadi beberapa halaman (`?single=1`).
- **Antarmuka CLI Fleksibel**: Dapat dijalankan langsung dengan opsi default atau dikustomisasi via argumen command line.
- **Modular (Class-based)**: Menggunakan kelas `DetikFinanceScraper` yang mudah diimpor dan diperluas di proyek lain.

---

## Prasyarat & Instalasi

Pastikan telah menginstal dependensi:
```bash
pip install requests beautifulsoup4 pandas
```
*(Atau menggunakan `uv` jika menggunakan uv environment).*

---

## Penggunaan

### 1. Menjalankan secara Default
Mengambil link dari halaman 1 sampai 3, lalu mengekstrak detailnya ke CSV dan JSON:
```bash
python main.py
```

### 2. Menggunakan Opsi CLI
Anda dapat menyesuaikan halaman, jeda waktu (delay), atau nama file output:
```bash
# Menentukan rentang halaman (misal: halaman 1 sampai 5)
python main.py --start-page 1 --end-page 5

# Menyesuaikan jeda waktu request (contoh: 1 detik)
python main.py --delay 1.0

# Melewati pengumpulan link dan langsung scrape link yang ada di links.txt
python main.py --skip-collect

# Menentukan nama file output kustom
python main.py --csv-file output.csv --json-file output.json
```

### 3. Menggunakan Sebagai Modul Python
```python
from main import DetikFinanceScraper

# Inisialisasi scraper
scraper = DetikFinanceScraper(delay=0.5)

# Tahap 1: Kumpulkan link
links = scraper.collect_links(start_page=1, end_page=2, txt_filename="links.txt")

# Tahap 2: Scrape artikel (dengan proteksi anti-duplikasi otomatis)
results = scraper.scrape_articles_from_list(
    urls=links,
    csv_filename="hasil_scraping_detik.csv",
    json_filename="hasil_scraping_detik.json"
)
```

---

## Struktur File Output

File hasil disimpan dalam format CSV dan JSON dengan kolom:
```
judul,link,waktu,isi_berita
```
