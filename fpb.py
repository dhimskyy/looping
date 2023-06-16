print("=====PROGRAM MENCARI FPB=====")
# mendefinisikan fungsi
def hitung_FPB(x, y):
    # memilih bilangan yang paling kecil
    if x > y:
        terkecil = y
    else:
        terkecil = x
    for i in range(1, terkecil+1):
        if ((x % i == 0) and (y % i == 0)):
            fpb = i
    return fpb
            
            
nilai1 = int(input("Masukkan bilanagan pertama: "))
nilai2 = int(input("Masukkan bulangan kedua: "))
print("Faktor Persekutuan Terbesar =", hitung_FPB(nilai1, nilai2))

