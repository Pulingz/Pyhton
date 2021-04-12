# Math operator
# *,/,+,-
#exponential / perpangkatan **
# 2 * 2 * 2
print(2 ** 3)

# which operator will be assign first?
# print(3 * 3 + 3 / 3 - 3 ) // 7 or 1
# 9 + 1 - 3
print(3 * 3 + 3 / 3 - 3 )

# exercise 2
# calculate body mass
# input height, weight
# rumus = body mass = weight : height * height
# example output = 80 : 1.75 * 1.75 = 26.12xxxxx
# solution
weight = input("enter your weight in kg : ")
height = input("enter your height in m : ")

result = float(weight) / float(height) ** 2

print(result)
# membulatkan
print(round(result, 2))

# shortcode operation
#  +=, *=, -=, /=
score = 23
# score = score + score // 46
score += score
# score = score + 1 //24
score += 1

print(score)
