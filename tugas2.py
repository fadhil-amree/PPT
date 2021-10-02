def faktorial(*angka):
    hasil = 1
    for i in angka:
        hasil *= i
    return(hasil)

print(faktorial (2,3,4))
