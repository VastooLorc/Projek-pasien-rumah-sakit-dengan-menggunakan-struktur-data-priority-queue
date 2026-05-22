class Pasien:
    def __init__(self, pid, nama, kondisi, kesadaran, detak_jantung, nyeri):

        self.id=pid 
        self.nama=nama
        self.kondisi=kondisi
        self.kesadaran=kesadaran
        self.detak_jantung=detak_jantung
        self.nyeri=nyeri
 
class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next= None

class HashHeap:
    def __init__(self, size = 20):
        self.size = size
        self.table = [None]*size

    def hash_function(self,key):
        total = 0
        for char in key:
            total += ord(char)
            return total % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table sss

 