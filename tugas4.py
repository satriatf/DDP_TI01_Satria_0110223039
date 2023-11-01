#deklarasi dan inisialisasi variabel
pelanggan = "andra"
totalbelanja = 250000

#struktur kendali if
if (totalbelanja > 200000):
    keterangan = "selamat anda mendapat hadiah"
else:
    keterangan = "terimakasih sudah berbelanja"

#cetak data
print("pelanggan",pelanggan,"\n","total belanja anda rp.",totalbelanja,"\n",keterangan)

print("--------------------------------------------------------------------------------")

#siswa dinyatakan lulus minimal 60 nilainya
nama = "andra"
matpel = "matematika"
nilai = 59.99
#ternary
keterangan ="lulus" if nilai >= 60 else "gagal"

#cetak data
print("nama siswa \t:",nama,
        "\nmata pelajaran \t:",matpel,
        "\nnilai \t\t:",nilai,
        "\keterangan \t:",keterangan)

print("---------------------------------------------------------------------------------")

nama = "andra"
mapel = "matematika"
nilai = 59.99
#uji grade dengan if multi konisi
if(nilai >= 85 and nilai <= 100):
    grade = "a"
elif(nilai >= 75 and nilai < 85):
    grade ="b"
elif(nilai >= 60 and nilai < 75):
    grade ="c"
elif(nilai >= 30 and nilai < 60):
    grade ="d"
else:
    grade = "e"

print("nama siswa \t:",nama,
        "\nmata pelajaran \t:",matpel,
        "\nnilai \t\t:",nilai,
        "\keterangan \t:",grade)

print("-----------------------------------------------------------------------------------")



