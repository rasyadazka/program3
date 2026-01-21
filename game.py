print("Selamat datang di game tebak angka!")
print("Angka rahasia adalah antara 1 dan 1000.")

secret_number = 999

while True:
    guess = int(input("Masukkan tebakan Anda: "))
    if guess == secret_number:
        print("Selamat! Anda menebak dengan benar.")
        break
    elif guess < secret_number:
        print("Terlalu kecil. Coba lagi.")
    else:
        print("Terlalu besar. Coba lagi.")