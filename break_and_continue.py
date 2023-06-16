# for i in range(1, 10):
#     print("Ini perulangan ke-", i)
#     if i == 7:
#         print("Perulangan ke-", i, "Dihentikan!")
#         break
    

# for i in range(0, 10):
#     #skkip jika i == 5
#     if (i == 5):
#         continue
    
#     print(i)

# a = 0
# while True:
#     print("Step ke-", a, "!")
#     a += 1
#     if a == 7:
#         print("Step ke-", a, "Dihentikan!")
#         break

angka = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# skip jika i bilangan genap
# dan i lebih dari 0
i = -1
while i < len(angka):
    i += 1
    if i % 2 == 0 and i > 0:
        print('Skip')
        continue
    
    # tidak dieksekusi ketika continue dipanggil
    print(angka[i])
    
