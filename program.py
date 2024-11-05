import os
import sys

def tampilkan_menu():
    daftar = ['Jika sebuah kata memiliki lebih banyak huruf kapital (uppercase)\n   daripada huruf kecil (lowercase), maka seluruh kata akan\n   diubah menjadi huruf kapital..\n',
              'Jika sebuah kata memiliki lebih banyak huruf kecil daripada huruf\n   kapital, maka seluruh kata akan diubah menjadi huruf kecil.\n',
              'Jika jumlah huruf kapital dan huruf kecil dalam sebuah kata sama,\n   maka kata tersebut akan diubah menjadi huruf kapital atau \n   huruf kecil berdasarkan karakter terakhirnya.']

    for indeks, aturan in enumerate(daftar, start=1):
        print(f"{indeks}. {aturan}")

    print("\nMenu:")
    print("1. Mulai Program")
    print("2. Keluar")

def check_string(input_string):
    return input_string.strip() != "" and all(char.isalpha() or char.isspace() for char in input_string)

def count_upper_lower(input_string):
    upper, lower = 0, 0
    for char in input_string:
        if char.isupper():
            upper += 1
        else:
            lower += 1
    return upper, lower

def uppercase_all(input_string):
    return input_string.upper()

def lowercase_all(input_string):
    return input_string.lower()

def loweruppercase_by_end(input_string):
    if input_string[-1].isupper():
        return uppercase_all(input_string)
    else:
        return lowercase_all(input_string)

def programend():
    print("Program selesai.")
    sys.exit()

def process(input_string):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Input valid!\n")
    upper, lower = count_upper_lower(input_string)
    print(f"Kalimat yang Anda input: {input_string}")

    if upper > lower:
        print("\nHuruf besar terdeteksi lebih banyak daripada huruf kecil.\nSeluruh kata akan diubah menjadi huruf kapital.")
        print(f"Hasil: {uppercase_all(input_string)}")
    elif lower > upper:
        print("\nHuruf kecil terdeteksi lebih banyak daripada huruf besar.\nSeluruh kata akan diubah menjadi huruf kecil.")
        print(f"Hasil: {lowercase_all(input_string)}")
    else:
        print("\nHuruf kecil terdeteksi sama banyak dengan huruf besar.")
        if input_string[-1].isupper():
            print("Karena huruf terakhir adalah huruf besar maka seluruh kata diubah menjadi huruf kapital")
        else:
            print("Karena huruf terakhir adalah huruf kecil maka seluruh kata diubah menjadi huruf kecil")
            
        print(f"Hasil: {loweruppercase_by_end(input_string)}")

def checking():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nHalo ini adalah program untuk mengecek huruf\n")
    input_string = input("Masukkan kalimat: ")

    if check_string(input_string):
        process(input_string)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Input tidak valid!\n")

def main_control():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1-2): ")
        
        os.system('cls' if os.name == 'nt' else 'clear') 
        if pilihan == '1':
            checking()
        elif pilihan == '2':
            programend()

        input("\nTekan Enter untuk kembali ke menu...") 

main_control()