# n = int(input("Enter a number: "))
# for i in range(2, n):
#     print(i)
#     if n % i == 0:
#         print(False)
#         break
# else:
#     print(True)

############################# ALUR #######################################*
# for 12 in range(12,25+1)
# 	jika 12 > 1:
# 		for 2 in range(2,12):
# 			if(11%10==0):
# 			break
# 	else:
# 		print(11)



# 2 - 11

# 12 - 25
# ##########################################################################

# start = int(input("Start : "))
# end = int(input("End : "))
# temp = 0
# for i in range(start, end, 2):
#   if i>1:
#     for j in range(2,i):
#         if(i % j==0):
#             break

#     else:
#         print(i)


#
for i in range(1,20):
    temp = 0
    for j in range(1,i+1):
        reminder = i % j
        if reminder == 0:
            temp += 1

    if temp == 2:
        print (f"{i},bilangan prima")
    else:
        print (f"{i},bukan bilangan prima")



