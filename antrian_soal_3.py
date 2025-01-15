class Stack:
    def __init__(self):
        self.items = []  

    def tampilan(self):
        print('''Pilihan
              1. Tambah Antrian
              2. Lanjut Ke Antrian Berikutnya
              3. Keluar
''')


    def push(self, push):
        self.items.append(push)
        print(f'"{push}" ditambahkan ke dalam antrian')

    def pop(self):
        if self.isEmpty():
            print("Antrian Kosong")
        else:
            self.items.pop(0)
