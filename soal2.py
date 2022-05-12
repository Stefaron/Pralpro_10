'''list_a = ['red', 'green', 'blue']           
list_b = ['#FF0000','#008000', '#0000FF']
kamus = {}                                  #pertama buat dictionary kosong dulu

for i in list_a:                            #ini buat akses satu persatu isi list dari list_a
    for j in list_b:                        #ini buat akses satu persatu isi list dari list_b
        kamus[i]=j
        list_b.remove(j)
        break

print(kamus)'''


list_a = ['red', 'green', 'blue']           
list_b = ['#FF0000','#008000', '#0000FF']

kamus = dict(zip(list_a,list_b))            #fungsi zip buat gabungin 2 list secara berurutan
print(kamus)                                #habis tu dibuat dictionary dan di print