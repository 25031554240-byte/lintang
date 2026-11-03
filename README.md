# 📊 PROYEK DATA WRANGLING: TREN HARGA PANGAN RAMADAN 2024 JAWA TIMUR

---

## 📌 1. Deskripsi Proyek
Proyek ini bertujuan untuk mengintegrasikan, membersihkan, mentransformasi, dan menganalisis dataset multi-sumber terkait tren harga komoditas pangan utama (**Paket E**: Beras Medium I, Cabai Merah Besar, Bawang Merah, Telur Ayam Ras, Daging Ayam Ras) di pasar tradisional Jawa Timur selama periode **Ramadan 2024**.

Dataset akhir menyatukan 3 dimensi data utama:
1. **Harga Pangan (PIHPS)**: Transaksi harian/mingguan komoditas pasar tradisional.
2. **Master Wilayah & Demografi (Kepmendagri)**: Pengodean wilayah resmi (`35.XX`) dan kepadatan penduduk.
3. **Kondisi Mikroklimat (NOAA GSOD)**: Suhu udara, curah hujan, dan kecepatan angin.

---

## 🗂️ 2. Struktur Folder & Output Dataset

* **`dataset_bersih_tahap4/`** *(Dataset Pembersihan Individual)*:
  * `data_wilayah_clean.parquet` & `.csv` (Master Wilayah Kode Kepmendagri 35.XX)
  * `data_cuaca_clean.parquet` & `.csv` (Data Iklim NOAA Metrik)
  * `data_harga_paket_e_clean.parquet` & `.csv` (Data Transaksi PIHPS Tidy)
* **`dataset_final_tahap5/`** *(Dataset Terintegrasi Final)*:
  * `data_ramadan_enriched.parquet` & `.csv` (Data Gabungan Siap BI Dashboard / Model Analysis)

---

## 🛠️ 3. Alur Kerja & Metodologi (Tahap 1 - 7)

| Tahap | Nama Tahapan | Deskripsi Operasi Main / Metodologi |
| :--- | :--- | :--- |
| **Tahap 1–3** | **Ingestion & Reshaping** | Loading multi-format data (`.csv`, `.xlsx`, `.parquet`) dan *unpivot* (*melting*) matriks harga menjadi *long format* deret waktu. |
| **Tahap 4** | **Data Cleaning** | Normalisasi teks wilayah ke kode Kepmendagri (`35.XX`), konversi satuan cuaca ke SI ($°C$, $mm$), dan pembersihan nilai *sentinel*. |
| **Tahap 5** | **Data Enrichment & Join** | Agregasi ke skala **ISO Weekly**, penanganan stasiun cuaca duplikat, dan **`LEFT JOIN`** ke master wilayah & cuaca (*zero data loss*). |
| **Tahap 6** | **Validation & Scaling** | Interpolasi linear harga, *Winsorization* outlier (1%-99%), serta transformasi ($\log(X+1)$, Min-Max Scaling, Z-score). |
| **Tahap 7** | **Group Processing & Analysis** | Agregasi multi-fungsi (`groupby.agg`), *z-score* per grup, persentase perubahan mingguan, *pivot table*, dan visualisasi tren harga. |

---

## 📊 4. Ringkasan Temuan Utama & Keterbatasan Data

### 💡 Temuan Utama Analisis
* **Volatilitas Komoditas**: Cabai Merah Besar dan Daging Ayam Ras mencatatkan lonjakan harga paling signifikan pada puncak periode Ramadan (Minggu ke-14 & 15).
* **Integrasi Data**: Penggunaan `LEFT JOIN` menjaga **100% data harga PIHPS utuh** tanpa ada transaksi yang terbuang.

### ⚠️ Keterbatasan Data (*Data Limitations*)
1. Data harga PIHPS mencatat transaksi pada hari kerja (Senin–Jumat).
2. Imputasi stasiun cuaca dilakukan secara rata-rata regional bagi kabupaten/kota yang tidak memiliki stasiun NOAA aktif secara mandiri.

---

## 🚀 5. Cara Menjalankan Notebook (Execution Guide)
1. Buka file `Untitled13.ipynb` di **Google Colab**.
2. Pastikan file data mentah (`PIHPS`, `NOAA`, `Kepmendagri`) berada di direktori kerja yang sesuai.
3. Jalankan sel kode secara berurutan mulai dari **Tahap 1 hingga Tahap 7** (`Runtime > Run all`).
