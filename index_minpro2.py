## Mini Project 2 Dasar-Dasar Pemrograman ##
## Aplikasi Forum diskusi komunitas player Visual Novel ##

# Data akun pengguna
akun = {
    "Admin": {"password": "Admin008", "role": "admin"},
    "Rin": {"password": "VNlover123", "role": "member"}
}

#List topik diskusi
topik_diskusi = []

# Fungsi login ke akun pengguna
def login():
    print("\n=== Silahkan Login Akun Anda ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in akun and akun[username]["password"] == password:
        print(f"Selamat datang! {akun[username]['role']}")
        return username, akun[username]['role']
    else:
        print("Login gagal. Username atau Password tidak sesuai")
        return None, None

    ### mendefinisikan tampilan dari setiap pilihan menu ###
# program/function untuk tampilan menu : 1. Lihat semua topik
def lihat_topik():
    if not topik_diskusi:
        print("Belum ada topik yang tersedia")
        return
    else:
        for i, topik in enumerate(topik_diskusi):
            print(f"{i+1}. {topik['judul']} (by {topik['author']})")

# program/function untuk tampilan menu : 2. Buat Topik Diskusi
def buat_topik(user):
    judul = input("Masukkan Judul: ")
    isi = input("Apa yang anda pikirkan? : ")
    topik = {"judul": judul, "isi": isi, "author": user, "komentar": []}
    topik_diskusi.append(topik)
    print("Topik berhasil ditambahkan!")

# program/function untuk tampilan menu : 3. edit Topik Diskusi
def edit_topik():
    lihat_topik()
    try:
        pilih_topik = int(input("Pilih nomor topik: ")) - 1
        topik = topik_diskusi[pilih_topik]
        topik["judul"] = input("Masukkan judul baru: ")
        topik["isi"] = input("Edit isi: ")
        print("Topik berhasil diperbarui!")
    except:
        print("Topik tidak ditemukan!")

# program/function untuk tampilan menu : 4. Hapus Topik Diskusi
def hapus_topik():
    lihat_topik()
    try:
        pilih_topik = int(input("Masukkan nomor topik yang ingin dihapus: ")) - 1
        topik_diskusi.pop(pilih_topik)
        print("Topik berhasil dihapus.")
    except:
        print("Topik tidak ditemukan!")

# Fungsi untuk mengomentari postingan (untuk user)
def komentar_topik(user):
    lihat_topik()
    try:
        pilih_topik = int(input("Pilih nomor topik: ")) - 1
        topik = topik_diskusi[pilih_topik]
        print(f"\n{topik['judul']}\n{topik['isi']}")
        print("Komentar:")
        for c in topik["komentar"]:
            print("-", c)
        teks = input("Tulis komentar (kosongkan untuk batal): ")
        if teks:
            topik["komentar"].append(f"{user}: {teks}")
            print("Komentar berhasil ditambahkan.")
    except:
        print("Topik tidak ditemukan.")

# Function untuk Menu Akses role Admin
def menu_admin():
    while True:
        print("\n=== Silahkan Pilih Menu (1-5) ===")
        print("\n1. Lihat Topik\n2. Buat Topik\n3. Edit Topik\n4. Hapus Topik\n5. Logout")
        pilih = input("Pilih: ")
        if pilih == "1":
            lihat_topik()
        elif pilih == "2":
            buat_topik("admin")
        elif pilih == "3":
            edit_topik()
        elif pilih == "4":
            hapus_topik()
        elif pilih == "5":
            break
        else:
            print("Pilihan salah.")

# Function untuk menu Akses role Member
def menu_member(user):
    while True:
        print("\n=== Silahkan Pilih Menu (1-4) ===")
        print("\n1. Lihat Topik\n2. Buat Topik\n3. Komentar\n4. Logout")
        pilih = input("Pilih: ")
        if pilih == "1":
            lihat_topik()
        elif pilih == "2":
            buat_topik(user)
        elif pilih == "3":
            komentar_topik(user)
        elif pilih == "4":
            break
        else:
            print("Pilihan salah.")

#Function untuk mengarahkan menu tampilan berdasarkan role Pengguna
print("=" *25, "Forum Komunitas Visual Novel", "=" *25)
while True:
    user, role = login()
    if role == "admin":
        menu_admin()
    elif role == "member":
        menu_member(user)

    ulang = input("Apakah anda ingin login lagi? (y/n): ")
    if ulang != "y":
        print("=" *25, "Sampai Jumpa!", "=" *25, "\n")
        break
