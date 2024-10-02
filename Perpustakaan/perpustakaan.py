# Daftar buku Umum
buku_umum = [
    {"judul": "Good Bye, Things", "pengarang": "Fumio Sasaki"},
    {"judul": "The Alchemist", "pengarang": "Paulo Coelho"},
    {"judul": "Tetralogi Buru", "pengarang": "Pramoedya Ananta Toer"},
    {"judul": "Madilog", "pengarang": "Tan Malaka"},
    {"judul": "Seni Bersikap Bodo Amat", "pengarang": "Mark Manson"},
    {"judul": "Man's Search for Meaning", "pengarang": "Viktor E. Frankl"},
    {"judul": "Thinking, Fast and Slow", "pengarang": "Daniel Kahneman"},
    {"judul": "Filosofi Teras", "pengarang": "Henry Manampiring"},
    {"judul": "Outliers: The Story of Success", "pengarang": "Malcolm Gladwell"},
    {"judul": "Atomic Habits", "pengarang": "James Clear"},
    {"judul": "Sapiens: A Brief History of Humankind", "pengarang": "Yuval Noah Harari"}
]

# Daftar buku sejarah
buku_sejarah = [
    {"judul": "10 Dosa Besar Soeharto", "pengarang": "Drs. Wimanjaya K. Liotohe"},
    {"judul": "Pengkhianatan G30S/PKI", "pengarang": "Arswendo Atmowiloto"},
    {"judul": "Hidup dan Mati Adolf Hitler", "pengarang": "Agus Nur Cahyo"},
    {"judul": "20 Bodoh Besar Soeharto", "pengarang": "Drs. Wimanjaya K. Liotohe"},
    {"judul": "A History of Modern Indonesia", "pengarang": "Adrian Vickers"},
    {"judul": "Sapiens: A Brief History of Humankind", "pengarang": "Yuval Noah Harari"},
    {"judul": "Guns, Germs, and Steel", "pengarang": "Jared Diamond"},
    {"judul": "The Silk Roads: A New History of the World", "pengarang": "Peter Frankopan"},
    {"judul": "The Diary of a Young Girl", "pengarang": "Anne Frank"},
    {"judul": "1776", "pengarang": "David McCullough"},
    {"judul": "The Rise and Fall of the Third Reich", "pengarang": "William L. Shirer"},
    {"judul": "Team of Rivals: The Political Genius of Abraham Lincoln", "pengarang": "Doris Kearns Goodwin"},
    {"judul": "The Wright Brothers", "pengarang": "David McCullough"}
]

# Daftar Novel
buku_novel = [
    {"judul": "Laskar Pelangi", "pengarang": "Andrea Hirata"},
    {"judul": "Bumi Manusia", "pengarang": "Pramoedya Ananta Toer"},
    {"judul": "Pulang", "pengarang": "Leila S. Chudori"},
    {"judul": "Supernova", "pengarang": "Dee Lestari"},
    {"judul": "Cantik Itu Luka", "pengarang": "Eka Kurniawan"},
    {"judul": "Perahu Kertas", "pengarang": "Dee Lestari"},
    {"judul": "To Kill a Mockingbird", "pengarang": "Harper Lee"},
    {"judul": "1984", "pengarang": "George Orwell"},
    {"judul": "The Catcher in the Rye", "pengarang": "J.D. Salinger"},
    {"judul": "Pride and Prejudice", "pengarang": "Jane Austen"},
    {"judul": "The Great Gatsby", "pengarang": "F. Scott Fitzgerald"},
    {"judul": "The Kite Runner", "pengarang": "Khaled Hosseini"},
    {"judul": "Keajaiban Toko Kelontong Namiya", "pengarang": "Keigo Higashino"},
    {"judul": "One Hundred Years of Solitude", "pengarang": "Gabriel García Márquez"},
    {"judul": "Moby Dick", "pengarang": "Herman Melville"},
    {"judul": "Anna Karenina", "pengarang": "Leo Tolstoy"},
    {"judul": "The Road", "pengarang": "Cormac McCarthy"},
    {"judul": "Harry Potter and the Philosopher's Stone", "pengarang": "J.K. Rowling"},
    {"judul": "The Lord of the Rings", "pengarang": "J.R.R. Tolkien"},
    {"judul": "The Book Thief", "pengarang": "Markus Zusak"}
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
    elif jenis_buku == "novel":
        print("\nDaftar Buku Novel:")
        for idx, buku in enumerate(buku_novel, start=1):
            print(f"{idx}. {buku['judul']} - {buku['pengarang']}")
    print("===============================")

def hitung_peminjaman(jenis_buku, pilihan_buku, jumlah_buku):
    if jenis_buku == "umum":
        buku_dipilih = buku_umum[pilihan_buku - 1]
    elif jenis_buku == "sejarah":
        buku_dipilih = buku_sejarah[pilihan_buku - 1]
    elif jenis_buku == "novel":
        buku_dipilih = buku_novel[pilihan_buku - 1]
    else:
        return None
        
    return buku_dipilih["judul"], buku_dipilih["pengarang"], jumlah_buku

def tampilkan_data_peminjam(nis, nama, kelas, jurusan, daftar_buku, tanggal_pinjam, tanggal_kembali):
    print("================================================================")
    print("             Perpustakaan Kota Ngawi                ")
    print("================================================================")
    print(f"NIS: {nis}")
    print(f"Nama: {nama}")
    print(f"Kelas: {kelas}")
    print(f"Jurusan: {jurusan}")
    print("================================================================")
    print("Buku yang dipinjam:")
    for buku in daftar_buku:
        print(f"Judul Buku: {buku['judul']} Pengarang: {buku['pengarang']} Jumlah: {buku['jumlah']}")
    print(f"Tanggal Pinjam: {tanggal_pinjam}")
    print(f"Tanggal Kembali: {tanggal_kembali}")
    print("================================================================")
