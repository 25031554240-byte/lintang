import customtkinter as ctk
import time

# ==============================================================================
# DATA AWAL PERJALANAN DINAS 35 DATA
# ==============================================================================
data_awal = [
    [18, "SPD018", "Rian Firmansyah", "Banjarmasin", "2026-02-05", "2026-02-08", "Koordinasi Instansi"],
    [4, "SPD004", "Deni Pratama", "Yogyakarta", "2026-01-08", "2026-01-10", "Monitoring Proyek"],
    [29, "SPD029", "Cindy Oktavia", "Tasikmalaya", "2026-02-27", "2026-03-01", "Monitoring Proyek"],
    [12, "SPD012", "Lukman Hakim", "Batam", "2026-01-24", "2026-01-27", "Rapat Tahunan"],
    [33, "SPD033", "Vina Kartika", "Semarang", "2026-03-06", "2026-03-08", "Sosialisai Proyek"],
    [1, "SPD001", "Andi Saputra", "Jakarta", "2026-01-02", "2026-01-05", "Rapat Koordinasi"],
    [22, "SPD022", "Vina Melati", "Lombok", "2026-02-13", "2026-02-16", "Workshop IT"],
    [15, "SPD015", "Olivia Natalia", "Solo", "2026-01-30", "2026-02-02", "Seminar Nasional"],
    [8, "SPD008", "Hendra Wijaya", "Makassar", "2026-01-16", "2026-01-19", "Sosialisasi Program"],
    [25, "SPD025", "Yoga Prasetyo", "Bengkulu", "2026-02-19", "2026-02-22", "Sosialisasi Aplikasi"],
    [31, "SPD031", "Lila Andari", "Lumajang", "2026-03-04", "2026-03-06", "Monitoring Sistem"],
    [5, "SPD005", "Eka Putri", "Semarang", "2026-01-10", "2026-01-12", "Studi Banding"],
    [19, "SPD019", "Sinta Maharani", "Aceh", "2026-02-07", "2026-02-10", "Pelatihan Operator"],
    [11, "SPD011", "Kiki Amelia", "Pontianak", "2026-01-22", "2026-01-25", "Pelatihan SDM"],
    [26, "SPD026", "Zaki Ramadhan", "Cirebon", "2026-02-21", "2026-02-23", "Rapat Evaluasi"],
    [2, "SPD002", "Budi Santoso", "Bandung", "2026-01-04", "2026-01-06", "Seminar Teknologi"],
    [24, "SPD024", "Xena Larasati", "Jayapura", "2026-02-17", "2026-02-21", "Kunjungan Dinas"],
    [14, "SPD014", "Nanda Putra", "Lampung", "2026-01-28", "2026-01-30", "Kunjungan Kerja"],
    [35, "SPD035", "Dini Oktavia", "Jombang", "2026-03-08", "2026-03-11", "Pelatihan Kerja"],
    [7, "SPD007", "Gina Maharani", "Bali", "2026-01-14", "2026-01-17", "Workshop Nasional"],
    [20, "SPD020", "Tono Wijoyo", "Padang", "2026-02-09", "2026-02-12", "Audit Lapangan"],
    [32, "SPD032", "Rian Mahendra", "Mojokerto", "2026-03-05", "2026-03-07", "Kunjungan Kerja"],
    [9, "SPD009", "Intan Permata", "Medan", "2026-01-18", "2026-01-21", "Evaluasi Kinerja"],
    [23, "SPD023", "Wahyu Hidayat", "Kupang", "2026-02-15", "2026-02-18", "Evaluasi Program"],
    [17, "SPD017", "Qori Rahma", "Samarinda", "2026-02-03", "2026-02-06", "Monitoring Sistem"],
    [3, "SPD003", "Citra Lestari", "Surabaya", "2026-01-06", "2026-01-08", "Pelatihan Sistem"],
    [13, "SPD013", "Maya Sari", "Pekanbaru", "2026-01-26", "2026-01-28", "Pendataan Proyek"],
    [30, "SPD030", "Daffa Alfarizi", "Jember", "2026-03-01", "2026-03-03", "Koordinasi Daerah"],
    [6, "SPD006", "Fajar Nugroho", "Malang", "2026-01-12", "2026-01-14", "Audit Internal"],
    [28, "SPD028", "Bagas Maulana", "Madiun", "2026-02-25", "2026-02-27", "Supervisi Lapangan"],
    [10, "SPD010", "Joko Susilo", "Palembang", "2026-01-20", "2026-01-22", "Pengawasan Lapangan"],
    [21, "SPD021", "Uli Kurniawan", "Manado", "2026-02-11", "2026-02-14", "Pengembangan Sistem"],
    [16, "SPD016", "Putra Aditya", "Balikpapan", "2026-02-01", "2026-02-04", "Supervisi Proyek"],
    [34, "SPD034", "Saka Putra", "Sleman", "2026-03-07", "2026-03-09", "Evaluasi Keja"],
    [27, "SPD027", "Anisa Fitri", "Kediri", "2026-02-23", "2026-02-25", "Pelatihan Pegawai"]
]

# Daftar kode surat dropdown diurutkan rapi secara alfabet untuk mempermudah user memilih
daftar_kode_surat = sorted([baris[1] for baris in data_awal])

# ==============================================================================
# LOGIKA PROSES ALGORITMA DENGAN PENYUSUNAN LOG LANGKAH
# ==============================================================================
def run_sequential(arr, key, is_ascending):
    steps_log = []
    langkah = 0
    steps_log.append(f"=== ANALISIS STRATEGI: SEQUENTIAL SEARCH ({'ASCENDING' if is_ascending else 'DESCENDING'}) ===")
    steps_log.append(f"Ukuran Data: {len(arr)} | Kunci Target: {key}")
    steps_log.append(f"Metode: Memeriksa data satu per satu secara linear mulai dari indeks awal.\n")
    
    for i in range(len(arr)):
        langkah += 1
        current_id = arr[i][1]
        steps_log.append(f"Langkah Ke-{langkah} -> Mengecek data pada Indeks {i}: Apakah {current_id} == {key}?")
        if current_id == key:
            steps_log.append(f"   [COCOK] Data ditemukan di Indeks {i} setelah melalui {langkah} operasi pemeriksaan.")
            return i, langkah, "\n".join(steps_log)
        else:
            steps_log.append(f"   [SALAH] Data tidak cocok. Melanjutkan ke elemen berikutnya.")
            
    steps_log.append(f"\n-> Hasil Akhir: Data tidak ditemukan hingga batas akhir array ({langkah} langkah).")
    return -1, langkah, "\n".join(steps_log)

def run_binary(arr, key, is_ascending):
    steps_log = []
    langkah = 0
    low = 0
    high = len(arr) - 1
    
    steps_log.append(f"=== ANALISIS STRATEGI: BINARY SEARCH ({'ASCENDING' if is_ascending else 'DESCENDING'}) ===")
    steps_log.append(f"Ukuran Data: {len(arr)} | Kunci Target: {key}")
    steps_log.append(f"Metode: Membagi rentang data menjadi dua secara rekursif di titik tengah (mid).\n")
    
    while low <= high:
        langkah += 1
        mid = (low + high) // 2
        current_id = arr[mid][1]
        
        steps_log.append(f"Langkah Ke-{langkah}:")
        steps_log.append(f"  • Rentang Aktif: Indeks {low} s/d Indeks {high} (Sisa Data: {high - low + 1} elemen)")
        steps_log.append(f"  • Kalkulasi Batas Tengah: ({low} + {high}) // 2 = Indeks {mid}")
        steps_log.append(f"  • Membaca Data Titik Tengah: '{current_id}'")
        steps_log.append(f"  • Evaluasi: Apakah {current_id} == {key}?")
        
        if current_id == key:
            steps_log.append(f"  -> [COCOK PERFECT] Target ditemukan tepat di Indeks {mid}!")
            return mid, langkah, "\n".join(steps_log)
        
        if is_ascending:
            if current_id < key:
                steps_log.append(f"  -> [SALAH] Karena nilai '{current_id}' < '{key}', maka seluruh data di sebelah kiri dibuang.")
                steps_log.append(f"     Batas rendah (Low) digeser naik ke indeks tengah + 1 = {mid + 1}")
                low = mid + 1
            else:
                steps_log.append(f"  -> [SALAH] Karena nilai '{current_id}' > '{key}', maka seluruh data di sebelah kanan dibuang.")
                steps_log.append(f"     Batas tinggi (High) digeser turun ke indeks tengah - 1 = {mid - 1}")
                high = mid - 1
        else:
            if current_id < key:
                steps_log.append(f"  -> [SALAH] (Mode Descending) Karena '{current_id}' < '{key}', data sebelah kanan bernilai lebih kecil, maka dibuang.")
                steps_log.append(f"     Batas tinggi (High) digeser turun ke indeks tengah - 1 = {mid - 1}")
                high = mid - 1
            else:
                steps_log.append(f"  -> [SALAH] (Mode Descending) Karena '{current_id}' > '{key}', data sebelah kiri bernilai lebih besar, maka dibuang.")
                steps_log.append(f"     Batas rendah (Low) digeser naik ke indeks tengah + 1 = {mid + 1}")
                low = mid + 1
        steps_log.append("")
                
    steps_log.append(f"-> Hasil Akhir: Target tidak ditemukan di dalam ruang pencarian array.")
    return -1, langkah, "\n".join(steps_log)

def run_interpolation(arr, key):
    steps_log = []
    langkah = 0
    low = 0
    high = len(arr) - 1
    
    steps_log.append("=== METODE BARU YANG DIAJUKAN: INTERPOLATION SEARCH ===")
    steps_log.append(f"Kunci Target: {key}")
    steps_log.append("Prinsip Kerja: Memprediksi letak posisi indeks secara dinamis berdasarkan nilai numerik target (seperti mencari kamus).\n")
    
    try:
        key_num = int(key.replace("SPD", ""))
    except ValueError:
        return -1, 0, "Format Penulisan Salah. Pastikan diawali kode huruf 'SPD' lalu diikuti angka."

    while low <= high:
        low_num = int(arr[low][1].replace("SPD", ""))
        high_num = int(arr[high][1].replace("SPD", ""))
        
        if key_num < low_num or key_num > high_num:
            steps_log.append(f"-> Target angka {key_num} berada di luar jangkauan batas array [{low_num} s/d {high_num}].")
            break
            
        langkah += 1
        steps_log.append(f"Langkah Ke-{langkah}:")
        steps_log.append(f"  • Informasi Nilai Batas: Low_Value={low_num} (Idx {low}) | High_Value={high_num} (Idx {high})")
        
        if low_num == high_num:
            if low_num == key_num:
                steps_log.append(f"  -> Batas atas dan bawah bernilai konstan sama. Ditemukan di Indeks {low}")
                return low, langkah, "\n".join(steps_log)
            break
            
        pos = low + int(((key_num - low_num) / (high_num - low_num)) * (high - low))
        steps_log.append(f"  • Kalkulasi Posisi Estimasi (pos): {low} + [({key_num} - {low_num}) / ({high_num} - {low_num})] * ({high} - {low}) = Indeks {pos}")
        
        if pos < 0 or pos >= len(arr):
            steps_log.append("  -> Kesalahan Komputasi: Posisi hasil estimasi berada di luar indeks dimensi array.")
            break
            
        current_id = arr[pos][1]
        steps_log.append(f"  • Membuka Data pada Posisi Estimasi (Indeks {pos}): Ditemukan data '{current_id}'")
        
        if current_id == key:
            steps_log.append(f"  -> [COCOK SEMPURNA] Nilai estimasi posisi tepat 100%! Target langsung ditemukan hanya dalam 1 langkah.")
            return pos, langkah, "\n".join(steps_log)
            
        if current_id < key:
            steps_log.append(f"  -> Nilai posisi terlalu kecil. Menggeser batas Low ke {pos + 1}")
            low = pos + 1
        else:
            steps_log.append(f"  -> Nilai posisi terlalu besar. Menggeser batas High ke {pos - 1}")
            high = pos - 1
        steps_log.append("")
            
    return -1, langkah, "\n".join(steps_log)

def hitung_semua_perbandingan(key):
    hasil_perbandingan = []
    data_asc = sorted(data_awal, key=lambda x: x[1])
    data_desc = sorted(data_awal, key=lambda x: x[1], reverse=True)

    mulai = time.perf_counter()
    idx, langkah, _ = run_sequential(data_asc, key, True)
    waktu = (time.perf_counter() - mulai) * 1000
    hasil_perbandingan.append(("Sequential Search (Ascending)", langkah, waktu, idx))

    mulai = time.perf_counter()
    idx, langkah, _ = run_sequential(data_desc, key, False)
    waktu = (time.perf_counter() - mulai) * 1000
    hasil_perbandingan.append(("Sequential Search (Descending)", langkah, waktu, idx))

    mulai = time.perf_counter()
    idx, langkah, _ = run_binary(data_asc, key, True)
    waktu = (time.perf_counter() - mulai) * 1000
    hasil_perbandingan.append(("Binary Search (Ascending)", langkah, waktu, idx))

    mulai = time.perf_counter()
    idx, langkah, _ = run_binary(data_desc, key, False)
    waktu = (time.perf_counter() - mulai) * 1000
    hasil_perbandingan.append(("Binary Search (Descending)", langkah, waktu, idx))

    mulai = time.perf_counter()
    idx, langkah, _ = run_interpolation(data_asc, key)
    waktu = (time.perf_counter() - mulai) * 1000
    hasil_perbandingan.append(("Interpolation Search", langkah, waktu, idx))

    return sorted(hasil_perbandingan, key=lambda x: x[2])

# ==============================================================================
# FUNGSI EVENT UTAMA SAAT TOMBOL DIKLIK
# ==============================================================================
def eksekusi_pencarian():
    key = combo_kode_surat.get().strip()
    skema = combo_skema.get()
    
    if not key or key == "Pilih Kode Surat":
        hasil_tab1.configure(state="normal")
        hasil_tab1.delete("1.0", "end")
        hasil_tab1.insert("end", "⚠️ Peringatan: Pilih kode surat terlebih dahulu dari daftar!")
        hasil_tab1.configure(state="disabled")
        return

    # Pemrosesan dan penataan urutan data dinamis berdasarkan skema pengujian yang dipilih
    if "Ascending" in skema or "Metode Baru" in skema:
        working_data = sorted(data_awal, key=lambda x: x[1])
        is_ascending = True
    else:
        working_data = sorted(data_awal, key=lambda x: x[1], reverse=True)
        is_ascending = False

    index_found = -1
    total_langkah = 0
    log_perjalanan = ""
    
    waktu_mulai = time.perf_counter()
    
    if "Sequential" in skema:
        index_found, total_langkah, log_perjalanan = run_sequential(working_data, key, is_ascending)
    elif "Binary" in skema:
        index_found, total_langkah, log_perjalanan = run_binary(working_data, key, is_ascending)
    elif "Metode Baru" in skema:
        index_found, total_langkah, log_perjalanan = run_interpolation(working_data, key)
        
    waktu_selesai = time.perf_counter()
    kompensasi_waktu_ms = (waktu_selesai - waktu_mulai) * 1000

    hasil_tab1.configure(state="normal")
    hasil_tab1.delete("1.0", "end")
    
    if index_found != -1:
        d = working_data[index_found]
        
        # ----------------------------------------------------------------------
        # PROSES PENCCARIAN INDEKS ASAL (DARI LIST DATA_AWAL YANG MASIH ACAK)
        # ----------------------------------------------------------------------
        indeks_asal = -1
        for idx_asli, baris in enumerate(data_awal):
            if baris[1] == d[1]:
                indeks_asal = idx_asli
                break
        
        output_ui = f"""✅ HASIL PENCARIAN DATA SURAT PERJALANAN DINAS

📋 ATRIBUT DATA INFORMASI YANG DITEMUKAN
──────────────────────────────────────────────────────────────────────────
• Posisi Urutan Skema Aktif: Indeks Ke-{index_found}
• Posisi Indeks Asal Excel : Indeks Ke-{indeks_asal} (Sebelum Diurutkan/Acak murni)
• Nomor Kode Surat         : {d[1]}
• Nama Karyawan/PNS        : {d[2]}
• Kota Tujuan Dinas        : {d[3]}
• Tanggal Berangkat        : {d[4]}
• Tanggal Kembali          : {d[5]}
• Keperluan Agenda         : {d[6]}

⏱️ METRIK ANALISIS PERFORMA & KOMPENSASI WAKTU
──────────────────────────────────────────────────────────────────────────
• Skema Algoritma          : {skema}
• Jumlah Beban Loop        : {total_langkah} Kali Operasi Evaluasi
• Kompensasi Waktu         : {kompensasi_waktu_ms:.6f} milidetik (ms)

👉 CATATAN :
Penjelasan logis runtutan alur proses mengapa algoritma di atas dapat menghasilkan 
kesimpulan tersebut secara terperinci telah dicetak di lembar berikutnya. 
Silakan klik judul 'Tab 2: Langkah Algoritma' di bagian atas layar Anda!"""
    else:
        output_ui = f"❌ Hasil Analisis: Kode data '{key}' Tidak Ditemukan.\n\nSaran: Pastikan rentang nomor berkas berkisar antara SPD001 sampai SPD035."

    hasil_tab1.insert("1.0", output_ui)
    hasil_tab1.configure(state="disabled")
    
    hasil_tab2.configure(state="normal")
    hasil_tab2.delete("1.0", "end")
    hasil_tab2.insert("1.0", log_perjalanan)
    hasil_tab2.configure(state="disabled")

    # === OUTPUT: PERBANDINGAN DI TAB 3 ===
    hasil_perbandingan = hitung_semua_perbandingan(key)
    hasil_tab3.configure(state="normal")
    hasil_tab3.delete("1.0", "end")

    teks_perbandingan = f"""📊 ANALISIS PERBANDINGAN KECEPATAN & KINERJA ALGORITMA
Kode yang dicari: {key}
Ukuran Data: {len(data_awal)} Data
──────────────────────────────────────────────────────────────────────────
{"Peringkat":<10} | {"Metode Algoritma":<25} | {"Langkah":<8} | {"Waktu (ms)":<12} | {"Status":<10}
──────────────────────────────────────────────────────────────────────────\n"""

    for i, (nama, langkah, waktu, idx) in enumerate(hasil_perbandingan, 1):
        status = "✅ Ditemukan" if idx != -1 else "❌ Tidak Ada"
        teks_perbandingan += f"{i:<10} | {nama:<25} | {langkah:<8} | {waktu:.6f}   | {status:<10}\n"

    teks_perbandingan += """
📈 ANALISIS KOMPLEKSITAS WAKTU (TIME COMPLEXITY) PILIHAN
──────────────────────────────────────────────────────────────────────────"""

    if "Sequential" in skema:
        teks_perbandingan += f"""
• Algoritma Aktif : {skema}
  - Best Case    : O(1)
  - Average Case : O(n)
  - Worst Case   : O(n)
  
• Kompleksitas Total Implementasi:
  - Murni Searching : O(n)

📝 KESIMPULAN ANALISIS SKEMA:
• Menelusuri array satu per satu dari awal. Efisiensi bergantung posisi target.
• Jika data berada di depan (*Ascending* pada kode awal), pencarian sangat kilat. 
• Jika data berada di paling akhir, performa akan melambat secara linear (Worst Case)."""

    elif "Binary" in skema:
        teks_perbandingan += f"""
• Algoritma Aktif : {skema}
  - Best Case    : O(1)
  - Average Case : O(log n)
  - Worst Case   : O(log n)

• Kompleksitas Total Implementasi:
  - Sorting + Search : O(n log n) + O(log n) = O(n log n)

📝 KESIMPULAN ANALISIS SKEMA:
• Membagi wilayah pencarian menjadi dua bagian secara konsisten di setiap tahapan loop.
• Jauh lebih efisien dibanding Sequential Search saat menangani data yang berukuran besar.
• Memiliki performa langkah yang stabil baik dalam mode urutan Ascending maupun Descending."""

    elif "Metode Baru" in skema:
        teks_perbandingan += f"""
• Algoritma Aktif : {skema}
  - Best Case    : O(1)
  - Average Case : O(log log n)
  - Worst Case   : O(n)

• Kompleksitas Total Implementasi:
  - Sorting + Search : O(n log n) + O(log log n) = O(n log n)

📝 KESIMPULAN ANALISIS SKEMA:
• Bekerja dengan rumus estimasi layaknya manusia mencari halaman kata kunci pada sebuah kamus cetak.
• Berhasil mencapai efisiensi tertinggi (**hanya 1 langkah**) dikarenakan data kode surat `SPD001` 
  hingga `SPD035` memiliki pola sebaran nilai numerik yang sangat seragam dan teratur."""

    teks_perbandingan += """

💡 TIPS REKOMENDASI SISTEM:
Untuk performa terbaik tanpa bottleneck O(n log n), lakukan proses pengurutan (Sorting) data di awal program saja (satu kali saja), jangan diletakkan di dalam fungsi tombol klik pencarian."""

    hasil_tab3.insert("1.0", teks_perbandingan)
    hasil_tab3.configure(state="disabled")

# ==============================================================================
# DESAIN ANTARMUKA DAN PENGATURAN LAYAR PENUH (FULL SCREEN)
# ==============================================================================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Sistem Analisis Kompensasi Waktu Perbandingan Algoritma Searching")
root.state('zoomed') 

frame_container = ctk.CTkFrame(root, corner_radius=15, fg_color="#f1f5f9")
frame_container.pack(pady=20, padx=20, fill="both", expand=True)

label_title = ctk.CTkLabel(
    frame_container, 
    text="Sistem Komparasi Kompleksitas Algoritma Pencarian Surat Dinas", 
    font=ctk.CTkFont(family="Lato", size=22, weight="bold"), 
    text_color="#1e3a8a"
)
label_title.pack(pady=(20, 10))

tab_system = ctk.CTkTabview(frame_container, corner_radius=10)
tab_system.pack(pady=10, padx=15, fill="both", expand=True)

tab_1 = tab_system.add("Tab 1: Dashboard Utama")
tab_2 = tab_system.add("Tab 2: Langkah Algoritma")
tab_3 = tab_system.add("Tab 3: Perbandingan Kecepatan")

# ----------------- KOMPONEN-KOMPONEN DI TAB 1 -----------------
frame_input_grup = ctk.CTkFrame(tab_1, fg_color="transparent")
frame_input_grup.pack(pady=15)

lbl_input = ctk.CTkLabel(frame_input_grup, text="Pilih Nomor Kode Surat :  ", font=ctk.CTkFont(size=13, weight="bold"))
lbl_input.grid(row=0, column=0, padx=5, pady=5, sticky="w")

combo_kode_surat = ctk.CTkOptionMenu(frame_input_grup, values=daftar_kode_surat, width=280, height=35)
combo_kode_surat.set("Pilih Kode Surat")
combo_kode_surat.grid(row=0, column=1, padx=5, pady=5)

lbl_skema = ctk.CTkLabel(frame_input_grup, text="Pilih Skema Pengujian :  ", font=ctk.CTkFont(size=13, weight="bold"))
lbl_skema.grid(row=0, column=2, padx=(20, 5), pady=5, sticky="w")

combo_skema = ctk.CTkOptionMenu(frame_input_grup, values=[
    "Sequential Search Ascending",
    "Sequential Search Descending",
    "Binary Search Ascending",
    "Binary Search Descending",
    "Metode Baru: Interpolation Search"
], width=280, height=35)
combo_skema.grid(row=0, column=3, padx=5, pady=5)

btn_proses = ctk.CTkButton(
    tab_1, 
    text="JALANKAN & HITUNG WAKTU", 
    command=eksekusi_pencarian, 
    font=ctk.CTkFont(size=13, weight="bold"), 
    fg_color="#1d4ed8", 
    hover_color="#1e40af", 
    width=300, 
    height=40
)
btn_proses.pack(pady=(0, 15))

hasil_tab1 = ctk.CTkTextbox(tab_1, font=ctk.CTkFont(family="Consolas", size=13), border_width=1, border_color="#cbd5e1")
hasil_tab1.pack(pady=10, padx=10, fill="both", expand=True)
hasil_tab1.configure(state="disabled")

# ----------------- KOMPONEN-KOMPONEN DI TAB 2 -----------------
hasil_tab2 = ctk.CTkTextbox(tab_2, font=ctk.CTkFont(family="Consolas", size=13), fg_color="#0f172a", text_color="#f8fafc")
hasil_tab2.pack(pady=10, padx=10, fill="both", expand=True)
hasil_tab2.insert("1.0", "💡 Belum ada riwayat simulasi.\nSilakan masukkan kode surat dan tekan tombol eksekusi di 'Tab 1: Dashboard Utama' terlebih dahulu!")
hasil_tab2.configure(state="disabled")

# ----------------- KOMPONEN-KOMPONEN DI TAB 3 -----------------
hasil_tab3 = ctk.CTkTextbox(tab_3, font=ctk.CTkFont(family="Consolas", size=13))
hasil_tab3.pack(pady=10, padx=10, fill="both", expand=True)
hasil_tab3.insert("1.0", "⚖️ Belum ada data perbandingan.\nJalankan pencarian terlebih dahulu untuk melihat analisis kecepatan seluruh algoritma!")
hasil_tab3.configure(state="disabled")

root.mainloop()