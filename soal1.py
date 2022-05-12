kamus = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}    #Pertama, masukin nilai dari dictionary dulu
print('key\t\tvalue\t\titem')                   #ini buat print aja kata 'key', 'value', 'item' (\t artinya itu tab buat kasih jarak)

for k in kamus:                                 #perulangan buat akses isi dari dictionarynya satu per satu
    print(k,'\t\t',kamus[k],'\t\t' ,k)          #k itu sebagai keys nya, kamus[k] itu nilai dari keys nya tadi, k terakhir sama kek k yg pertama