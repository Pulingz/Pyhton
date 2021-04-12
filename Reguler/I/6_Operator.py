# exercise 2
# calculate body mass
# input height, weight
# rumus = body mass = weight : height * height
# example output = 80 : 1.75 * 1.75 = 26.12xxxxx
# solution

weight = input("enter your weight in Kg: ")
height = input("enter your Height in m : ")

bms = int(weight) / float(height) ** 2
print("Your body mass is : ", round(bms))

