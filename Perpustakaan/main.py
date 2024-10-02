import perpustakaan as perp
from datetime import datetime, timedelta

pilihan = "y"
while pilihan == "y":
    # Ambil data peminjam satu kali
    nis = input("Masukkan NIS: ")
    nama = input("Masukkan Nama: ")
    kelas = input("Masukkan Kelas: ")
    jurusan = input("Masukkan Jurusan: ")

    # Tanggal peminjaman dan pengembalian
    tanggal_pinjam = datetime.now().strftime("%d-%m-%Y")
    tanggal_kembali = (datetime.now() + timedelta(days=7)).strftime("%d-%m-%Y")

    # Menyimpan buku yang dipinjam dalam satu sesi
    daftar_buku = []
    max_buku = 3

    while len(daftar_buku) < max_buku:
        # Memilih kategori buku
        print("""
        ==============================
        Perpustakaan Kota Ngawi
        Pilih Jenis Buku:
        1. Umum
        2. Sejarah
        3. Novel
        ==============================
        """)
        kategori = input("Masukkan pilihan jenis buku (1/2/3): ")

        if kategori == "1":
            jenis_buku = "umum"
        elif kategori == "2":
            jenis_buku = "sejarah"
        elif kategori == "3":
            jenis_buku = "novel"
        else:
            print("Jenis buku tidak valid, silahkan pilih (1/2/3).")
            continue

        # Tampilkan menu buku berdasarkan jenis
        perp.tampilkan_menu_buku(jenis_buku)

        try:
            pilihan_buku = int(input("Masukkan nomor buku yang ingin dipinjam: "))
            jumlah_buku = int(input("Masukkan jumlah buku yang dipinjam: "))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            continue

        judul, pengarang, jumlah_buku = perp.hitung_peminjaman(jenis_buku, pilihan_buku, jumlah_buku)

        # Simpan buku yang dipilih ke daftar
        daftar_buku.append({"judul": judul, "pengarang": pengarang, "jumlah": jumlah_buku})

        # Tanyakan apakah ingin menambah buku lagi
        if len(daftar_buku) < max_buku:
            tambah = input(f"Apakah Anda ingin meminjam buku lagi? (Y/N) (Maksimal {max_buku} buku): ").lower()
            if tambah == "n":
                break

    # Tampilkan struk peminjaman setelah semua buku dipilih
    perp.tampilkan_data_peminjam(nis, nama, kelas, jurusan, daftar_buku, tanggal_pinjam, tanggal_kembali)

    # Tanyakan apakah ingin memulai peminjaman baru
    pilihan = input("Apakah Anda ingin meminjam buku baru lagi? Y/N: ").lower()
    print("Terimakasih sudah meminjam buku di Perpustakaan Kota Ngawi!")
