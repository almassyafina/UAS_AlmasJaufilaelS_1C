antrian_restoran = []

def enqueue(item):
    antrian_restoran.append(item)

def dequeue():
      antrian_restoran.pop(0)

def isempty():
    return len(antrian_restoran) == 0

def front():
    if isempty() or len(antrian_restoran) == 1:
        return 'antrian kosong'
    else:
        return antrian_restoran[0]

def second():
    if isempty() or len(antrian_restoran)==1:
        return 'Kosong'
    else :
        return antrian_restoran[1]
    

    
def lihat_semua():
    for R in antrian_restoran:
        print(R)

