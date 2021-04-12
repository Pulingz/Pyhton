def sebuah_fungsi():
    x = 10
    return x

def fungsi_lain():
    global x
    x = 114
    print(x)

x = 666

print(x)
print(sebuah_fungsi())


