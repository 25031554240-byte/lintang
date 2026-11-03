Direktori ini berisi dataset olahan proyek Data Wrangling Tren Harga Pangan Ramadan 2024 di Jawa Timur.

* `dataset_bersih_tahap4/` berisi hasil pembersihan individual dari 3 sumber data utama:
  * `data_wilayah_clean.csv` / `.parquet`: Master kode wilayah administrasi Kepmendagri (35.XX) dan kepadatan penduduk.
  * `data_cuaca_clean.csv` / `.parquet`: Data mikroklimat harian hasil konversi ke satuan SI (°C, mm, km/jam) dari NOAA GSOD.
  * `data_harga_paket_e_clean.csv` / `.parquet`: Data transaksi harian komoditas Paket E (Beras, Cabai Merah, Bawang Merah, Telur, Daging Ayam) dari PIHPS.

* `dataset_final_tahap5/` berisi dataset terintegrasi final:
  * `data_ramadan_enriched.csv` / `.parquet`: Dataset gabungan skala mingguan (ISO Week) yang telah di-imputasi, di-winsorize, dan siap digunakan untuk analisis statistik maupun dashboard BI.

* `Untitled13.ipynb` berisi seluruh dokumentasi kode Python selangkah demi selangkah dari Tahap 1 hingga Tahap 7.
