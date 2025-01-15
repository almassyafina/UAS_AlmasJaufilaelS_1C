import pandas as pd

data =[
    'Nama':['Mahasiswa1','Mahasiswa2','Mahasiswa3'],
    'Algoritma dan struktur data 2' :[90,50,65],
    'Matematika Numerik': [80,60,70]
]

df= pd.DataFrame(data)

rata_matkul = df.mean()
rata_maha = df.index(axis=1)

print(f'Rata-rata nilai setiap mata kuliah:{rata_matkul} ')
print(f'Rata-rata nilai mahsiswa : {rata_maha}')
