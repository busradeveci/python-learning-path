yagmurlu = False   #true olanı yazıyor çalıştırdığında yani komutu böyle işliyor.
gunesli = False       #ikisi de true olunca en baştaki komutu çalıştırıyor. #true olanı çalıştırıyor sistem.
if yagmurlu:
    print("Ceketini Giy!")

    #bunlar birbirinden bağımsız kontrol mekanizması oldu.yani o yüzden yazdırıyor.
elif gunesli:       #else if kısaltılmışıdır elif. else if aksi takdirde demekdir.
    print("Güneş gözlüğünü tak.")
else:
    print("Normal bir şekilde dışarı çık.")

    #ikiside false olursa komutların bu ifadeyi yazdıracak.
    #yani bunların hiçbiri true değilse bunu yap demektir.

