# PROYEK DATA WRANGLING: TREN HARGA PANGAN RAMADAN 2024 JAWA TIMUR

Repositori ini berisi dataset olahan dan skrip Python untuk analisis tren harga komoditas pangan utama (Paket E: Beras Medium I, Cabai Merah Besar, Bawang Merah, Telur Ayam Ras, Daging Ayam Ras) di pasar tradisional Jawa Timur selama periode Ramadan 2024.

---

## Daftar File dan Direktori

* **`dataset_bersih_tahap4/`**: Direktori berisi hasil pembersihan individual dari 3 sumber data utama dalam format `.csv` dan `.parquet`:
  * `data_wilayah_clean.*`: Master kode wilayah administrasi Kepmendagri (`35.XX`) dan kepadatan penduduk.
  * `data_cuaca_clean.*`: Data iklim harian hasil konversi ke satuan SI ($°C$, $mm$, $km/jam$) dari NOAA GSOD.
  * `data_harga_paket_e_clean.*`: Data transaksi harian komoditas Paket E dari PIHPS yang telah di-*unpivot* (*tidy format*).

* **`dataset_final_tahap5/`**: Direktori berisi dataset terintegrasi final:
  * `data_ramadan_enriched.*`: Dataset gabungan skala mingguan (*ISO Week*) yang telah di-imputasi, di-winsorize, dan siap digunakan untuk analisis statistik atau *dashboard* BI.

* **`Untitled13.ipynb`**: File Notebook Python utama yang memuat dokumentasi kode selangkah demi selangkah dari Tahap 1 hingga Tahap 7.

---

## Alur Metodologi Singkat (Tahap 1–7)

1. **Tahap 1–3 (Ingestion & Reshaping)**: Import data mentah dan *unpivot* (*melting*) matriks harga menjadi deret waktu harian.
2. **Tahap 4 (Data Cleaning)**: Pembersihan teks wilayah, konversi satuan cuaca ke Metrik, dan penanganan nilai *sentinel*.
3. **Tahap 5 (Integration & Join)**: Agregasi ke skala *ISO Weekly* dan penggabungan via `LEFT JOIN` berbasis kode Kepmendagri.
4. **Tahap 6 (Validation & Scaling)**: Interpolasi *missing value*, *Winsorization* outlier (1%-99%), serta transformasi $\log(X+1)$, Min-Max, dan Z-score.
5. **Tahap 7 (Group Processing & Analysis)**: Agregasi multi-fungsi (`groupby.agg`), Z-score per grup, *pivot table*, dan visualisasi tren harga akhir.

---

## Cara Menggunakan
1. Jalankan notebook `Untitled13.ipynb` di Google Colab / Jupyter Notebook.
2. Pastikan struktur folder `dataset_bersih_tahap4/` dan `dataset_final_tahap5/` berada dalam direktori kerja yang sama.
