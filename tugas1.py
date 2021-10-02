
i = 3
while i < 15 :
    if (i%2 == 0):
        print(i,'i adalah bilangan genap')
    else :
        print(i,'i adalah bilangan ganjil')
    i +=1

# Fungsi

def fungsi_eksponen() :
    a = int(input('masukkan bilangan = '))
    b = 2
    if a % b == 0 :
        print(str(a), 'adalah bilangan genap' )
    else :
        print(str(a), 'adalah bilangan ganjil' )

fungsi_eksponen()


def hitung_luas_segitiga(alas, tinggi):
  luas = (alas * tinggi) / 2
  return luas
    
var1 = hitung_luas_segitiga(5, 7)
print("Luas segitiga adalah:",var1)