# sebuah_list = ['1','1','1',]

# try:
#     print(sebuah_list[10])
# except Exception as x:
#     print(f"proses gagal karena : {x}")

# read  text file

try:
    f = open('./public/file.txt', 'w')
    # t = f.read()
    t = f.write("Woops! I have deleted the content!")
    print(t)
    # a()
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

# print(len("Woops! I have deleted the content!"))

