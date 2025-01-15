
from  soal_3 import enqueue,dequeue
while True :
    opsi = int(input('Masukan pesanan : '))

    if opsi == 1:
        item = input('Daftar Pesanan :')
        enqueue(item)
        
    else:
        opsi == 2
        dequeue()
    
    print(enqueue())
    print(dequeue())
