import pandas as pd
import os
import base64

csv_path = r'D:\Coding\rizwansuckspy\TUGAS PPK\Pemrograman Modular\database_mahasiswa.csv'
os.makedirs(os.path.dirname(csv_path), exist_ok=True)

if not os.path.exists(csv_path):
    df = pd.DataFrame(columns=['id', 'nama_asli', 'nama_enkripsi', 'usia', 'nilai_rataan'])
    df.to_csv(csv_path, index=False)

def encrypt_data(nama):
    nama_list = list(nama)
    
    for i in range(len(nama_list)):
        if 'a' <= nama_list[i] <= 'z':  
            nama_list[i] = chr(((ord(nama_list[i]) - 97 + 3) % 26) + 97)
        elif 'A' <= nama_list[i] <= 'Z': 
            nama_list[i] = chr(((ord(nama_list[i]) - 65 + 3) % 26) + 65)
    
    nama_terenkripsi = ''.join(nama_list)
    return nama_terenkripsi

def masukkan_data(nama, usia, rataan):
    df = pd.read_csv(csv_path)
    nama_terenkripsi = encrypt_data(nama)[0:len(nama)]
    new_id = df['id'].max() + 1 if not df.empty else 1  # Generate ID baru
    new_row = {'id': new_id, 'nama_asli': nama, 'nama_enkripsi': nama_terenkripsi, 'usia': usia, 'nilai_rataan': rataan}
    df = df._append(new_row, ignore_index=True)
    df.to_csv(csv_path, index=False)
    print("Data berhasil ditambahkan!")

def hapus_data(id_data):
    df = pd.read_csv(csv_path)
    df = df[df['id'] != id_data]  # Menghapus baris dengan ID yang sesuai
    df.to_csv(csv_path, index=False)
    print(f"Data dengan ID {id_data} telah dihapus.")

def lihat_riwayat_enkripsi():
    df = pd.read_csv(csv_path)
    if not df.empty:
        print("ID | Nama | Usia | Rataan |")
        print("-" * 50)
        for _, row in df.iterrows():
            print(f"{row['id']} | {row['nama_enkripsi']} | {row['usia']} | {row['nilai_rataan']} |")
    else:
        print("Belum ada data yang dicatat.")

def lihat_riwayat():
    df = pd.read_csv(csv_path)
    if not df.empty:
        print("ID | Nama | Usia | Rataan |")
        print("-" * 50)
        for _, row in df.iterrows():
            print(f"{row['id']} | {row['nama_asli']} | {row['usia']} | {row['nilai_rataan']} |")
    else:
        print("Belum ada data yang dicatat.")

def cari_nama():
    nama = input("Masukkan nama mahasiswa : ")
    df = pd.read_csv(csv_path)
    df_filtered = df[df['nama_asli'] == nama]
    if not df_filtered.empty:
        print("ID | Nama | Usia | Rataan |")
        print("-" * 50)
        for _, row in df_filtered.iterrows():
            print(f"{row['id']} | {row['nama_asli']} | {row['usia']} | {row['nilai_rataan']} |")
    else:
        print("Data tidak ditemukan.")

def rataan():
    df = pd.read_csv(csv_path)
    if not df.empty:
        avg = df['nilai_rataan'].mean()
        print(f"Rataan : {avg:.2f}")
    else:
        print("Belum ada data yang dicatat.")

def nama_lulus():
    df = pd.read_csv(csv_path)
    df_lulus = df[df['nilai_rataan'] >= 70]
    if not df_lulus.empty:
        print("ID | Nama | Usia | Rataan |")
        print("-" * 50)
        for _, row in df_lulus.iterrows():
            print(f"{row['id']} | {row['nama_asli']} | {row['usia']} | {row['nilai_rataan']} |")
    else:
        print("Tidak ada mahasiswa yang lulus.")

def maxmin():
    df = pd.read_csv(csv_path)
    if not df.empty:
        max_usia = df.loc[df['usia'].idxmax()]
        min_usia = df.loc[df['usia'].idxmin()]
        
        print("\nMahasiswa Tertua : ")
        print("ID | Nama | Usia | Rataan |")
        print("-" * 50)
        print(f"{max_usia['id']} | {max_usia['nama_asli']} | {max_usia['usia']} | {max_usia['nilai_rataan']} |")

        print("\nMahasiswa Termuda : ")
        print("ID | Nama | Usia | Rataan |")
        print("-" * 50)
        print(f"{min_usia['id']} | {min_usia['nama_asli']} | {min_usia['usia']} | {min_usia['nilai_rataan']} |")

def tutup_koneksi():
    print("Program selesai.")
