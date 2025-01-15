from antrian_soal_3 import Stack

antrian1 = Stack()
antrian1.push("lisa")
antrian1.push("lukas")
antrian1.push("adi")

while True:
    for i, data in enumerate(antrian1.items,1):
        print(f'Antrian Ke-{i} {data}')
    antrian1.tampilan()
    pilih = int(input('Masukan Pilihan : '))
    
    if pilih == 1:
        nama = str(input("Masukan Nama :"))
        antrian1.push(nama.capitalize())
    
    if pilih == 2:
        antrian1.pop()
    if pilih == 3:
        keluar = str("Ingin Keluar Program? (Y/T) : ").upper()
        if keluar == "Y":
            break