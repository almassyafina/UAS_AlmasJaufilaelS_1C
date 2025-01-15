class Fruit:
    def __init__(self, nama, warna, rasa):
        self.Nama = nama
        self.warna = warna
        self.Rasa = rasa

    
    def setNama(self,jenis):
        self.Nama = jenis

    def setWarna(self,colour):
        self.warna = colour

    def setRasa (self,suka ):
        self.Rasa = suka 

    def information(self):
          return f'Nama Buah : {self.Nama} | Warna Buah: {self.warna} | Rasa Buah: {self.Rasa}'
    

Buah1 = Fruit('Rambutan','Merah','Manis')
Buah2 = Fruit('Duren','Coklat','Manis')
Buah3 = Fruit('Jeruk','Oren','Masam')


print(Buah1.information())
print(Buah2.information())
        








