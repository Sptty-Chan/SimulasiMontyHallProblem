import random


print("Tebak Tirai Yang Berisi Mobil\n")

""" List Hadiah """
hadiah = [(1, "Mobil"), (0, "Zonk"), (0, "Zonk")]

""" Mengacak Hadiah """
random.shuffle(hadiah)

""" Mengambil Pilihan Pertama """
pilihanPertama = int(input("Pilih tirai 1, 2, atau 3: "))
print("\n")
""" Index List Hadiah & Menghapus Index Yang Dipilih Agar Tidak Dibuka"""
ind = [0, 1, 2]
del ind[pilihanPertama - 1]

""" Memilih Salah Satu Index Yang Tidak Dipilih & Berisi Zonk Untuk Dibuka """
while True:
    cInd = random.choice(ind)
    if not hadiah[cInd][0]:
        ind.remove(cInd)
        break

print(f"Pembawa Acara Membuka Tirai Nomor {cInd + 1} & Isinya Adalah Zonk\n")
print(f"Tersisa 2 Tirai, Apakah Anda Ingin Berpindah Ke Tirai Nomor {ind[0] + 1}")
print("Dalam Konteks Monty Hall Problem, Pilihan Terbaik Dengan Probabilitas Kemenangan Tinggi Adalah Pindah.\n")

pilihanKedua = input("Pindah Atau Tidak (y/t): ")
print("\n")
if pilihanKedua.lower() == "y":
    if hadiah[ind[0]][0]:
        print("Selamat, Anda Mendapatkan Hadiah Utama Yaitu Sebuah Mobil.")
    else:
        print(f"Anda Mendapatkan Zonk, Mobilnya Ada Di Tirai Nomor {pilihanPertama}.")
else:
    if hadiah[pilihanPertama - 1][0]:
        print("Selamat, Anda Mendapatkan Hadiah Utama Yaitu Sebuah Mobil.")
    else:
        print(f"Anda Mendapatkan Zonk, Mobilnya Ada Di Tirai Nomor {ind[0] + 1}.")
