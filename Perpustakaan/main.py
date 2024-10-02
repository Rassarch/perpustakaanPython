import perpustakaan as perp
from datetime import datetime, timedelta

pilihan = "y"
while pilihan == "y":
    print("""
    ================================================================
                        Perpustakaan Kota Ngawikarta
          
    Pilih Jenis Buku:
    1. Umum
    2. Sejarah
    
    ================================================================
    """)
    perp.tampilkan_menu_buku()

    try:
        pesan = str(input("Masukkan kode buku yang ingin dipinjam: "))
        jumlah_buku = int(input("Masukkan jumlah buku yang dipinjam: "))
    except ValueError:
        print("Input tidak valid. Harap masukkan kode.")
        continue

    # Ambil data peminjam
    nis = input("Masukkan NIS: ")
    nama = input("Masukkan Nama: ")
    kelas = input("Masukkan Kelas: ")
    jurusan = input("Masukkan Jurusan: ")

    # tanggal peminjaman dan pengembalian
    tanggal_pinjam = datetime.now().strftime("%c")
    tanggal_kembali = (datetime.now() + timedelta(days=7)).strftime("%c")

    judul_buku, pengarang, jumlah_buku = perp.hitung_peminjaman(pesan, jumlah_buku)

    if judul_buku == "_":
        pilihan = input("Buku tidak tersedia, silahkan pilih buku yang ada. Ulangi Y/N?: ").lower
    else:
        perp.tampilkan_data_peminjam(nis, nama, kelas, jurusan, judul_buku, pengarang, jumlah_buku, tanggal_pinjam, tanggal_kembali)
        pilihan = input("Apakah anda ingin meminjam buku lain? Y/N: ").lowersE