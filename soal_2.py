import pandas as pd

data ={
    'Nama':['Mahasiswa1','Mahasiswa2','Mahasiswa3'],
    'Algoritma dan struktur data 2' :[90,50,65],
    'Matematika Numerik': [80,60,70]
}
df= pd.DataFrame[
    'Nama':['Mahasiswa1','Mahasiswa2','Mahasiswa3'],
    'Algoritma dan struktur data 2' :[90,50,65],
    'Matematika Numerik': [80,60,70]
]
index=['Mahasiswa1','Mahasiswa2','Mahasiswa3'],
columns=['Nama','Algoritma dan struktur data 2','Matematika Numerik']

df['Algoritma'] = [90,50,65]
df['Matematika Numerik'] = [80,60,70]

df['total'] = df.sum(axis=1)

df.loc['total'] = df.sum(axis=0)

print(df)

index_nilai_tertinggi_perbaris = df.idxmax(axis=0)
print(index_nilai_tertinggi_perbaris)
