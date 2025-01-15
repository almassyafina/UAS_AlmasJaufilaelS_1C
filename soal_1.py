data_mahasiswa = []
while True:
    nim = input('Masukan Nama NIM :') 
    nama = input('Masukan Nama Nama Mahasiswa :')

    data_mahasiswa.append(f'NIM : {nim}','Nama Mahasiswa : {nama}')

    tambah_lagi = input('Ingin Tambah Lagi? (ya/tidak):')
    if tambah_lagi: 'ya'
    break

print('Data Mahasiswa : ')