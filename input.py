import database_csv as dbs
import os

def tampilkan_menu():
    print()
    print("Menu:")
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Data Mahasiswa (Terenkripsi)")
    print("3. Tampilkan Nama Asli Mahasiswa")
    print("4. Cari Mahasiswa Berdasarkan Nama")
    print("5. Hitung Rata-Rata Nilai")
    print("6. Tampilkan yang Lulus")
    print("7. Tampilkan Mahasiswa Tertua dan Termuda")
    print("8. Keluar")

def tambah_data_mahasiswa():
    print("Masukkan Nama, Usia dan Nilai Rataan Mahasiswa")
    nama = input("Masukkan nama mahasiswa : ")
    usia = input("Masukkan usia mahasiswa : ")
    rataan = input("Masukkan nilai mahasiswa : ")
    print()
    print("Menambah data mahasiswa...")
    dbs.masukkan_data(nama, usia, rataan)

def tampilkan_data_terenkripsi():
    print("Menampilkan data mahasiswa yang terenkripsi...")
    print()
    dbs.lihat_riwayat_enkripsi()

def tampilkan_nama_asli():
    print("Menampilkan nama asli mahasiswa...")
    print()
    dbs.lihat_riwayat()

def cari_mahasiswa_berdasarkan_nama():
    print("Mencari mahasiswa berdasarkan nama...")
    print()
    dbs.cari_nama()

def hitung_rata_rata_nilai():
    print("Menghitung rata-rata nilai mahasiswa...")
    print()
    dbs.rataan()

def tampilkan_yang_lulus():
    print("Menampilkan mahasiswa yang lulus...")
    print()
    dbs.nama_lulus()

def tampilkan_mahasiswa_tertua_termuda():
    print("Menampilkan mahasiswa tertua dan termuda...")
    dbs.maxmin()

def main():
 while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1-8): ")
        
        os.system('cls' if os.name == 'nt' else 'clear') 
        if pilihan == '1':
            tambah_data_mahasiswa()
        elif pilihan == '2':
            tampilkan_data_terenkripsi()
        elif pilihan == '3':
            tampilkan_nama_asli()
        elif pilihan == '4':
            cari_mahasiswa_berdasarkan_nama()
        elif pilihan == '5':
            hitung_rata_rata_nilai()
        elif pilihan == '6':
            tampilkan_yang_lulus()
        elif pilihan == '7':
            tampilkan_mahasiswa_tertua_termuda()
        elif pilihan == '8':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")
        
        input("\nTekan Enter untuk kembali ke menu...")  
main()