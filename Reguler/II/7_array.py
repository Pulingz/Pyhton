# # List
# x = ['male','female',1,0.24]
# print(x[0:3])
# 0,1,2

# # tuple
# x = ('male','female',1,0.24)
# print(x[0:3])
# # 0,1,2
# dictionary
# employee = [
#                 {'name': 'udin', 'gender': 'male', 'age': 13},
#                 {'name': 'ucup', 'gender': 'male', 'age': 14}
#             ]

# for x in employee:
#     print(x['name'])

# Mengubah isi list/tuple/disctionary
# list
# x = ['male','female',1,0.24]
# x[0] = 'udin'
# x[0] = 'ucup'
# print(x)

# tuple
# x = ('male','female',1,0.24)
# x[0] = 'udin'
# print(x)

# dictionary
# employee = {'name': 'udin', 'gender': 'male', 'age': 13}

# employee['name'] = 1.4
# print(employee)


# Menambah multiple elemen pada list
# x = ['male','female',1,0.24]
# y = [3,4,7,'tes']
# newX = x + y
# print(newX)

# # Menambah multiple elemen pada tuple
# x = ('male','female',1,0.24)
# y = (3,4,7,'tes')
# newX = x + y
# print(newX)

# Menambah multiple elemen pada dictionary
# employee = {'name': 'udin', 'gender': 'male', 'age': 13}
# employees = {'status': 'single','asal': 'jkt'}
# employee.update(employees)
# print(employee)

# menghapus element pada list
# x = ['male','female',1,0.24]
# del x[0]
# print(x)

# menghapus element pada dictionary
# employee = {'name': 'udin', 'gender': 'male', 'age': 13}
# del employee['name']
# print(employee)

# min, max
# x = ['male','female',1,0.24]
# y = [34,55,76,23,44]
# # print(max(y))

# max = 0
# for x in y:
#     # print(x)
#     if x > max:
#         max = x
# print(max)


# case
# student_height = input("Input List of Student Height : ").split(',')
# for n in range(0, len(student_height)):
#     student_height[n] = int(student_height[n])
# # print(max(student_height))
# max = 0
# for x in student_height:
#     # print(x)
#     if x > max:
#         max = x
# print(max)

# n = int(input("\nBanyaknya Data : "))
# data = []
# jumlah = 0
# for i in range(n):
#     temp = float(input("masukan data ke - %d: " %(i+1)))
#     data.append(temp)
#     jumlah += data[i]
#     rata2 = jumlah / n



# print("Data yang di masukan (%d data) adalah : " %(n), list(data))
# print("Hasil Jumlah Keselurahan Data : %0.2f "% jumlah )
# print("Hasil Nilai Rata2 : %0.2f "% rata2)

# days = ["senin","selasa","rabu"]
# chosen_day = input("Pick One of your day : ").lower()
# today = days.index(chosen_day)
# yesterday = today - 1

# print(f"today is {days[today]} and yesterday is {days[yesterday]}")

# note
# tuple tidak dapat melakukan oprasi perubahan list
