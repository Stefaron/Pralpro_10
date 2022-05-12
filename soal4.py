file = input('Masukkan nama file : ')               #ini buat inputan nama file              

try:                                                #try buat program kalo gak eror dan filenya ada di komputer
    handle = open(file)                             #ini buka file
except:                                             #ini kalo programnya eror dan filenya ga ditemukan
    print(f'File tidak bisa dibuka : {file}')               
    exit()

kamus = {}                                          #buat dictionary kosong dulu
isi = []                                            #list kosong

for line in handle:                                 #buat akses perbaris di filenya
    hitung = 0                                      #buat aja dulu variable kosong (nanti buat itung jumlah perulangan)
    if line.startswith('From:'):                    #nah setelah diakses perbaris tadi, ini buat ngecek apakah dibaris itu diawali dengan 'From:'
        pisah = line.split()                        #kalo iya maka split jadi perkata
        hasil = pisah[1].split('@')                 #habis tu pisah lagi katanya dengan parameter '@', nanti jadinya nama email sama domain. Contohnya coba debug
        isi.append(hasil[1])                        #habis tu append/masukin index 1 dari hasil ke list isi

for i in isi:                                       #ini perulangan buat akses satu" isi dari list
    kamus[i] = kamus.get(i,0) + 1                   #.get itu buat ambil 

print(kamus)