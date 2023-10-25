#tugas pertama
var = ["beat","motor","150cc","biru","2"]
var.append ("15 juta")
var.append ("esp")
var.insert (2,"honda")
print(var[6])

print("=============================================")

#tugas kedua
pilihan=input(""" Hitunglah luas dari bangun ruang dibawah ini
====================================
1. menghitung persegi
2. menghitubg lingkaran
3. menghitung segitiga
====================================
silahkan pilih?
""")
match pilihan:
    case "1":
        print("menghitung luas persegi")
        sisi = int(input("masukkan sisi"))
        luasP = int(sisi*sisi)
        print("luas persegi adalah",luasP)
    case "2":
        print("menghitung luas lingkaran")
        jari = float(input("masukkan jari-jari"))
        luasL = float(3.14* jari-jari) 
        print("luas lingkaran adalah",luasL) 
    case "3" :
        print("menghitung luas segitiga") 
        alas = int(input("masukan alas"))
        tinggi = int(input("masukan tinggi")) 
        luasS = int (alas*tinggi/2)
        print("luas segitiga adalah",luasS)
    case _:
        print("operasi tidak di temukan")