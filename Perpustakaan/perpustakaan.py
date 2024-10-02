# Daftar buku Umum
buku_umum = [
    {"judul": "Good Bye, Things", "pengarang": "Fumio Sasaki"},
    {"judul": "The Alchemist", "pengarang": "Paulo Coelho"},
    {"judul": "Tetralogi Buru", "pengarang": "Pramoedya Ananta Toer"},
    {"judul": "Madilog", "pengarang": "Tan Malaka"},
]

# Daftar buku sejarah
buku_sejarah = [
    {"judul": "10 Dosa Besar Soeharto", "pengarang": "Drs. Wimanjaya K. Liotohe"},
    {"judul": "Pengkhianatan G30S/PKI", "pengarang": "Arswendo Atmowiloto"},
    {"judul": "Hidup dan Mati Adolf Hitler", "pengarang": "Agus Nur Cahyo"},
    {"judul": "20 Bodoh Besar Soeharto", "pengarang": "Drs. Wimanjaya K. Liotohe"},
]

def tampilkan_menu_buku(jenis_buku):
    if jenis_buku == "umum":
        print("\nDaftar Buku Umum:")
        for idx, buku in enumerate(buku_umum, start=1):
             print(f"{idx}. {buku['judul']} - {buku['pengarang']}")
    elif jenis_buku == "sejarah":
        print("\nDaftar Buku Sejarah:")
        for idx, buku in enumerate(buku_sejarah, start=1):
            print(f"{idx}. {buku['judul']} - {buku['pengarang']}")
    print("================================================================")

def hitung_peminjaman(jenis_buku, pilihan_buku, jumlah_buku):
        if jenis_buku == "umum":
            buku_dipilih = buku_umum[pilihan_buku - 1]
        elif jenis_buku == "sejarah":
            buku_dipilih = buku_sejarah[pilihan_buku - 1]
            
        return buku_dipilih["judul_buku"], buku_dipilih["pengarang"], jumlah_buku

def tampilkan_data_peminjam(nis, nama, kelas, jurusan, judul_buku, pengarang, jumlah_buku, tanggal_pinjam, tanggal_kembali):
    print("================================================================")
    print("             Perpustakaan Kota Ngawikarta                ")
    print("================================================================")
    print(f"NIS: {nis}")
    print(f"Nama: {nama}")
    print(f"Kelas: {kelas}")
    print(f"Jurusan: {jurusan}")
    print("================================================================")
    print("Buku yang dipinjam:")
    print(f"Judul Buku: {judul_buku}")
    print(f"Pengarang: {pengarang}")
    print(f"Jumlah Buku: {jumlah_buku}")
    print(f"Tanggal Pinjam {tanggal_pinjam}")
    print(f"Tanggal Kembali {tanggal_kembali}")
    print("================================================================")