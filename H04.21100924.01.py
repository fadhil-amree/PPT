# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : selasa, 27 April 2021 
# Deskripsi   : Program mengimplementasikan fungsi

A = int(input('masukkan A: '))
B = int(input('masukkan B: '))

def fungsi(A,B):
    for i in range(A, B+1):
        f = i**2 - 2*i + 5
        print(f'f({i}) = {f}')

fungsi(A,B) 