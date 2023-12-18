lembar = int(input("masukan jumlah halaman: "))
kolom = int(input("masukan jumlah kolom: "))
baris = int(input("masukkan jumlah baris: "))
print()
kelas = []  # Definisikan variabel kelas
presensi = [[["" for k in range(kolom)] for j in range(baris)] for i in range(lembar)]

for x in range(lembar):
    presensi[x][0][0] = "nama"

for x in range(lembar):
    kel = 0
    while kel == 0:
        print(x + 1, end=".")
        nama = input("masukan kelas: ").upper()
        if nama == "":
            print("nama wajib diisi")
        else:
            kel = 1
            kelas.append(nama)  # Perbaiki penambahan kelas ke dalam variabel kelas

for x in range(lembar):
    for y in range(kolom):
        if y == 0:
            pass
        else:
            a = str(y)
            presensi[x][0][y] = ("Pertemuan ke-" + a)

print()
print("Masukkan Nama Mahasiswa")
for x in range(lembar):
    print("kelas", kelas[x], ":")
    for y in range(baris):
        if y == 0  :
            pass
        else:
            print(y, end=".")
            char = 0
            while char == 0:
                nama = input("masukan nama mahasiswa : ")
                if len(nama) > 20:
                    print("tidak boleh lebih dari 20 karakter")
                else:
                    char = 1
                    presensi[x][y][0] = nama

print()
for z in range(len(presensi)):
    print(kelas[z],":")
    for x in range(len(presensi[z])):
        if presensi[z][x][0]=="":
            pass
        elif x>0:
            print(presensi[z][x][0],":")
            for y in range(len(presensi[z][x])):
                if y>0:
                    print("pertemuan ke-",y,":")
                    wh = 0
                    while wh==0:
                        kehadiran = input("hadir(h)/sakit(s)/alpha(a)):".lower())
                        if kehadiran=="hadir" or kehadiran=='h':
                            presensi[z][x][y]="Hadir"
                            wh=1
                        elif kehadiran == "sakit" or kehadiran=='s':
                            presensi[z][x][y] = "sakit"
                            wh=1
                        elif kehadiran == "alpha" or kehadiran=='a':
                            presensi[z][x][y] = "Alpha"
                            wh=1
                        else:
                            print("INPUT SALAH!")
                else :
                    pass
            print()
        else :
            pass
for z in range(len(presensi)):
    print(kelas[z],":")
    for x in range(len(presensi[z])):
        for y in range(len(presensi[z][x])):
            if x == 0 :
                if y == 0 :
                    print('|{:^20s}|'.format(presensi[z][x][y]),end="")
                else :
                    print('|{:^15s}|'.format(presensi[z][x][y]),end="")
            else :
                if y == 0 :
                    print('|{:^20s}|'.format(presensi[z][x][y]),end="")
                else :
                    print('|{:^15s}|'.format(presensi[z][x][y]),end="")
        print()
    print()
print()