def greet (lang):
    if lang == "es":               #lang bir yer tutucudur,böylece fonksiyonun ardışık çağrılarında veya çağrılmasında
        print("Hola")                     #programın ilk parametre olarak koyduğu şeye erişebiliriz.yani diyoruz ki ilk parametreyi almaya hazırız.
    elif lang == "fr":                        #yeniden kullanılabilir bir fonksiyon parçası şu an bu kod. // DEF //
        print("Bonjour")
    else:
        print("Hello")

greet("fr")