# angka1= input("masukan bilangan pertama : ")
# angka2= input("masukan bilangan kedua : ")

# # store into var
# x = int(angka1)
# y = int(angka2)

# # pengecekan
# if x == y:
#     print("nilai angka1 sama dengan nilai angka2")
# else:
#     print("nilai  angka1 != nilai angka2")

# Roller coaster
print("Welcome to The Roller Coaster")
height = int(input("what is your hegiht in cm : "))
#jika 1 - 115 di baca you can ride
#jika 115-120 di baca tes
#jika 120-150 di baca horee
#jika lebih dari banyak itu hasilnya you can"t ride roller
if height < 115:
    print("You can ride the roller coaster")
elif height < 120:
    print("tes")
elif height < 150:
    print("horeee")
else:
    print("You cant ride the roller coaster")

