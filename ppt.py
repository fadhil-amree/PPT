'''
#program menampilkan maksimum dari dua bilangan

A = int(input('masukkan nilai A ='))
B = int(input('masukkan nilai B ='))

if A > B :
    print('nilai maksimum adalah A')

elif B > A :    
    print('nilai maksimum adalah B')

else :    
    print('nilai A dan B adalah sama')
'''

'''
#program wujud air

Suhu_air_celcius = float(input('masukkan suhu air dalam derajat celcius : '))

if Suhu_air_celcius <= 0 :
    print('wujud air adalah padat')

elif 0 < Suhu_air_celcius < 100 :     
    print('wujud air adalah cair')

else :     
    print('wujud air adalah uap') 
'''
'''
#program total hambatan seri

R1 = float(input('masukkan nilai R1 :'))
R2 = float(input('masukkan nilai R2 :'))
R3 = float(input('masukkan nilai R3 :'))

if R1 < 0 or R2 < 0 or R3 < 0 :
    print('nilai hambatan harus positif!!')

else : 
    print('nilai total hambatan seri adalah', R1+R2+R3) 
'''


    
'''
#program menampilkan maksimum dari dua bilangan

A = int(input('masukkan nilai A ='))
B = int(input('masukkan nilai B ='))

if A > B :
    print('nilai maksimum adalah A')

elif B > A :    
    print('nilai maksimum adalah B')

else :    
    print('nilai A dan B adalah sama')
'''

'''
#program wujud air

Suhu_air_celcius = float(input('masukkan suhu air dalam derajat celcius : '))

if Suhu_air_celcius <= 0 :
    print('wujud air adalah padat')

elif 0 < Suhu_air_celcius < 100 :     
    print('wujud air adalah cair')

else :     
    print('wujud air adalah uap') 
'''
'''
#program total hambatan seri

R1 = float(input('masukkan nilai R1 :'))
R2 = float(input('masukkan nilai R2 :'))
R3 = float(input('masukkan nilai R3 :'))

if R1 < 0 or R2 < 0 or R3 < 0 :
    print('nilai hambatan harus positif!!')

else : 
    print('nilai total hambatan seri adalah', R1+R2+R3) 
'''
'''
#program ranking tiga bilangan

A = int(input('masukkan nilai A = '))
B = int(input('masukkan nilai B = '))
C = int(input('masukkan nilai C = '))

if A < B < C :
    print(A) ; print(B) ; print(C)
elif A < C < B :
    print(A)
    print(C)
    print(B)
elif B < A < C :
    print(B)
    print(A)
    print(C)
elif B < C < A :
    print(B)
    print(C)
    print(A)
elif C < A < B :
    print(C)
    print(A)
    print(B)
else :
    print(C)
    print(B)
    print(A)
'''
'''
#PROGRAM MENAMPILKAN 1 - N 
N = int(input('Masukkan nilai N ='))
i = 1
while i <= N:
    print(i)
    i += 1

def jumlah(N):
    hasil = 0
    i = 1
    while i <= N:
        hasil += i
        i += 1
    return (hasil)

print(jumlah(N))
'''
#program menerima 10 bilangan dan menampilkan jumlahannya
'''
sum = 0
for i in range(0,10) :
    x = int(input())
    sum += x

print(sum)
'''
'''
N = int(input('masukkan nilai N =  ' ))
jumlah = 0

if N <= 0 :
    print('N harus positif!!')
else :
    for i in range (1,N) :
        if i % 5 == 0:
            print (i) 
            jumlah += i

print(jumlah)
'''
'''
N = int(input('masukkan banyak mahasiswa = '))
print('nilai yang dimasukkan adalah A, B, C, D, E, atau F ')
i = 1
lulus = 0
tidak_lulus = 0
while i <= N :
    x = input('nilai mahasiswa : ')
    if (x == 'A') or (x=='B') or (x == 'C') or (x == 'D') :
        lulus += 1

    else :
        tidak_lulus +=1
    
    i += 1

print('Banyak mahasiswa yang lulus adalah', lulus)
print('Banyak mahasiswa yang tidak lulus adalah', tidak_lulus)
'''
'''
i = 1
genap = 0
ganjil = 0
while i > 0:
    x = int(input())
    if x < 0 :
        break

    else:
        if x % 2 == 0 :
            genap +=1

        else :
            ganjil +=1
    i += 1

print('ganjil :', ganjil)
print('genap :', genap)
'''
'''

N = int(input('masukkan banyak ayam :'))
print('anak ayam turunlah', N)

i = 1
while i <= N :
    
    if i == N :
        print('mati satu tinggal induknya')
        break
    
    print('mati satu tinggallah', N-i)
    i += 1

'''

#mencari luas
a = float(input('a :'))
b = float(input('b :'))
delta = float(input('delta :'))
luas = 0 
luas_daerah = 0
i = a
while a <= i < b :
    y1 = i**3 + i + 1
    y2 = (i+delta)**3 + (i+delta) + 1
    #print('y1 :', y1 , 'y2', y2)
    luas = (y1 + y2) * delta / 2
    #print(luas)
    luas_daerah += luas 
    i += delta

print(luas_daerah)

'''
N = int(input('masukkan banyak hari : '))
Tb = []
Ttotal = 0
for i in range (1,N+1) :
    T = float(input('masukkan suhu ' ))
    Tb.append(T)
    Ttotal += T
rata = Ttotal / N
print('Suhu maksimal :', max(Tb))
print('suhu minimal :', min(Tb))
print('suhu rata - rata :', rata )  
'''
'''
V = []
U = []
W = []
for i in range(0,5):
    V = int(input('masukkan anggota V :'))
    U = int(input('masukkan anggota U :'))
    W.append(U + V)

print(W)
'''

