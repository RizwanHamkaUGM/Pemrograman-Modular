import sqlite3
import pandas as pd
import datetime
import os
from cryptography.fernet import Fernet
import base64

db_path = r'D:\Coding\rizwansuckspy\TUGAS PPK\Pemrograman Modular\database_mahasiswa.db'
os.makedirs(os.path.dirname(db_path), exist_ok=True)

key = Fernet.generate_key()
cipher_suite = Fernet(key)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS mahasiswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_asli TEXT NOT NULL,
        nama_enkripsi TEXT NOT NULL,
        usia INT NOT NULL,
        nilai_rataan INT NOT NULL
    )
''')

"""===============================================ENCRYPT====================================================="""
# Fungsi untuk mengenkripsi data
def encrypt_data(data):
    encrypted_data = cipher_suite.encrypt(data.encode())
    encoded_data = base64.urlsafe_b64encode(encrypted_data).decode()
    return encoded_data

# Fungsi untuk mendekripsi data
def decrypt_data(encoded_data):
    encrypted_data = base64.urlsafe_b64decode(encoded_data.encode())
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

"""===============================================ENCRYPT====================================================="""

def masukkan_data(nama, usia, rataan):
    nama_terenkripsi = encrypt_data(nama)[0:len(nama)]
    cursor.execute('''
    INSERT INTO mahasiswa (nama_asli, nama_enkripsi, usia, nilai_rataan)
    VALUES (?, ?, ?, ?)
    ''', (nama, nama_terenkripsi, usia, rataan))
    conn.commit()
    print("Data berhasil ditambahkan!")

def hapus_data(id_data):
    cursor.execute('DELETE FROM mahasiswa WHERE id = ?', (id_data,))
    conn.commit()
    print(f"data dengan ID {id_data} telah dihapus.")

def lihat_riwayat_enkripsi():
    cursor.execute('SELECT * FROM mahasiswa')
    rows = cursor.fetchall()
    if rows:
        print("ID | Nama | Usia | Rataan |")
        print("-" * 50)
        for row in rows:
            print(f"{row[0]} | {row[2]} | {row[3]} | {row[4]} |")
    else:
        print("Belum ada data yang dicatat.")

def lihat_riwayat():
    cursor.execute('SELECT * FROM mahasiswa')
    rows = cursor.fetchall()
    if rows:
        print("ID | Nama | Usia | Rataan |")
        print("-" * 50)
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[3]} | {row[4]} |")
    else:
        print("Belum ada data yang dicatat.")
    
def cari_nama():
    nama = str(input("Masukkan nama mahasiswa : "))
    cursor.execute("SELECT * FROM mahasiswa WHERE nama_asli = ?", (nama,))
    rows = cursor.fetchall()
    if rows:
        print("ID | Nama | Usia | Rataan |")
        print("-" * 50)
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[3]} | {row[4]} |")

def rataan():
    cursor.execute("select avg(nilai_rataan) as rataan from mahasiswa")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f" Rataan : {row[0]}")

def nama_lulus():
    cursor.execute("select * from mahasiswa where nilai_rataan>=70")
    rows = cursor.fetchall()
    if rows:
        print("ID | Nama | Usia | Rataan |")
        print("-" * 50)
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[3]} | {row[4]} |")

def maxmin():
    cursor.execute("select * from mahasiswa where usia = (select max(usia) from mahasiswa)")
    rows = cursor.fetchall()
    if rows:
        print()
        print("Mahasiswa Tertua : ")
        print("ID | Nama | Usia | Rataan |")
        print("-" * 50)
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[3]} | {row[4]} |")
    cursor.execute("select * from mahasiswa where usia = (select min(usia) from mahasiswa)")
    print()
    rows = cursor.fetchall()
    if rows:
        print("Mahasiswa termuda : ")
        print("ID | Nama | Usia | Rataan |")
        print("-" * 50)
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[3]} | {row[4]} |")

def tutup_koneksi():
    conn.close()
    print("Koneksi ke database ditutup.")