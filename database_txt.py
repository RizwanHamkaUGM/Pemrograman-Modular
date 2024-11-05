import os
from cryptography.fernet import Fernet
import base64

# Path untuk menyimpan file teks
txt_path = r'D:\Coding\rizwansuckspy\TUGAS PPK\Pemrograman Modular\database_mahasiswa.txt'
os.makedirs(os.path.dirname(txt_path), exist_ok=True)

# Inisialisasi kunci enkripsi
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(data):
    encrypted_data = cipher_suite.encrypt(data.encode())
    encoded_data = base64.urlsafe_b64encode(encrypted_data).decode()
    return encoded_data

def decrypt_data(encoded_data):
    encrypted_data = base64.urlsafe_b64decode(encoded_data.encode())
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

def masukkan_data(nama, usia, rataan):
    if not os.path.exists(txt_path):
        with open(txt_path, 'w') as file:
            file.write("id|nama_asli|nama_enkripsi|usia|nilai_rataan\n")

    # Baca data dari file untuk mendapatkan ID terakhir
    with open(txt_path, 'r') as file:
        lines = file.readlines()
        last_id = int(lines[-1].split('|')[0]) if len(lines) > 1 else 0
        new_id = last_id + 1

    # Enkripsi nama
    nama_terenkripsi = encrypt_data(nama)[0:len(nama)]

    # Tambah data baru ke file
    with open(txt_path, 'a') as file:
        file.write(f"{new_id}|{nama}|{nama_terenkripsi}|{usia}|{rataan}\n")
    print("Data berhasil ditambahkan!")

def hapus_data(id_data):
    with open(txt_path, 'r') as file:
        lines = file.readlines()
    
    with open(txt_path, 'w') as file:
        for line in lines:
            if line.startswith(str(id_data) + "|"):
                print(f"Data dengan ID {id_data} telah dihapus.")
                continue
            file.write(line)

def lihat_riwayat_enkripsi():
    with open(txt_path, 'r') as file:
        lines = file.readlines()[1:]  # Skip header

    if lines:
        print("ID | Nama (Terenkripsi) | Usia | Rataan |")
        print("-" * 50)
        for line in lines:
            data = line.strip().split('|')
            print(f"{data[0]} | {data[2]} | {data[3]} | {data[4]}")
    else:
        print("Belum ada data yang dicatat.")

def lihat_riwayat():
    with open(txt_path, 'r') as file:
        lines = file.readlines()[1:]  # Skip header

    if lines:
        print("ID | Nama | Usia | Rataan |")
        print("-" * 50)
        for line in lines:
            data = line.strip().split('|')
            print(f"{data[0]} | {data[1]} | {data[3]} | {data[4]}")
    else:
        print("Belum ada data yang dicatat.")

def cari_nama():
    nama = input("Masukkan nama mahasiswa : ")
    with open(txt_path, 'r') as file:
        lines = file.readlines()[1:]  # Skip header

    found = False
    print("ID | Nama | Usia | Rataan |")
    print("-" * 50)
    for line in lines:
        data = line.strip().split('|')
        if data[1] == nama:
            print(f"{data[0]} | {data[1]} | {data[3]} | {data[4]}")
            found = True
    if not found:
        print("Data tidak ditemukan.")

def rataan():
    with open(txt_path, 'r') as file:
        lines = file.readlines()[1:]  # Skip header

    if lines:
        total, count = 0, 0
        for line in lines:
            data = line.strip().split('|')
            total += int(data[4])
            count += 1
        print(f"Rataan : {total / count:.2f}")
    else:
        print("Belum ada data yang dicatat.")

def nama_lulus():
    with open(txt_path, 'r') as file:
        lines = file.readlines()[1:]  # Skip header

    print("ID | Nama | Usia | Rataan |")
    print("-" * 50)
    for line in lines:
        data = line.strip().split('|')
        if int(data[4]) >= 70:
            print(f"{data[0]} | {data[1]} | {data[3]} | {data[4]}")

def maxmin():
    with open(txt_path, 'r') as file:
        lines = file.readlines()[1:]  # Skip header

    if lines:
        usia_data = [(int(line.split('|')[3]), line.strip()) for line in lines]
        tertua = max(usia_data)[1]
        termuda = min(usia_data)[1]

        print("\nMahasiswa Tertua : ")
        print("ID | Nama | Usia | Rataan |")
        print("-" * 50)
        data = tertua.split('|')
        print(f"{data[0]} | {data[1]} | {data[3]} | {data[4]}")

        print("\nMahasiswa Termuda : ")
        print("ID | Nama | Usia | Rataan |")
        print("-" * 50)
        data = termuda.split('|')
        print(f"{data[0]} | {data[1]} | {data[3]} | {data[4]}")

def tutup_koneksi():
    print("Program selesai.")
