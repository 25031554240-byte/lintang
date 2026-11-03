# Proyek Data Wrangling: Analisis Tren Harga Pangan Paket E Ramadan 2024 di Jawa Timur

**Disusun Oleh:** Lintang Chorirah Ariyanto (NIM: 25031554240)[cite: 1]  
**Program Studi:** Sains Data, Universitas Negeri Surabaya (UNESA)[cite: 1]  
**Dosen Pengampu:** Dr. Belgis Ainatul Iza, S.Si., M.Mat.[cite: 1]  

---

## Deskripsi Proyek
Proyek ini mengintegrasikan, membersihkan, dan mentransformasikan tiga sumber data heterogen (PIHPS Bank Indonesia, NOAA GSOD, dan Kepmendagri) untuk menganalisis dinamika harga pangan pokok Paket E (Beras Medium I, Cabai Merah Besar, Bawang Merah, Telur Ayam Ras, Daging Ayam Ras) di 38 Kabupaten/Kota di Jawa Timur selama periode Ramadan dan Idulfitri 2024 (ISO Week 10–16)[cite: 2].

---

## Struktur Folder Repositori / ZIP

```text
.
├── dataset_mentah/             # Data mentah awal (PIHPS Excel, NOAA CSV, Kepmendagri CSV)
├── dataset_bersih_tahap4/      # Output Tahap 4: Pembersihan individual (.csv & .parquet)
├── dataset_final_tahap5/       # Output Tahap 5: Integrated master (data_ramadan_enriched)
├── notebook_wrangling.ipynb    # Python Notebook (Tahap 1 - 7)
├── laporan.pdf                 # Laporan Utama UTS (Max 10 Halaman + Lampiran & AI Declaration)
├── Kamus_Data.md               # Spesifikasi lengkap variabel data
└── README.md                   # Dokumentasi teknis proyek
