print("=====SISTEM LOGIN SEDERHANA=====")

login = 0
while True:
    username = input("Masukkkan username: ")
    password = input("Masukkan password: ")
    
    if login == 3:
        print("Login gagal! Kesempatan mencoba sudah habis. Silakan coba lagi nanti!")
        break
    
    if username == "mdhimasafrizal" and password == "bebas123":
        print("Selamat datang ", username, "!")
        break
    
    else:
        print("Coba cek kembali, username atau password salah!")
        login += 1
        
