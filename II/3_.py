#range (0,10 di ganti 0,6)
#jika itu i duluan maka i ke bwh dan j ke  samping dan begitu sebaliknya
for i in range(0,10):
    for j in range(0, i+1):
        print(f"* - {i} - {j}",end="")

    print("\r")

# for i in range(0, 6):

# 		# inner loop to handle number of columns
# 		# values changing acc. to outer loop
# 		for j in range(0, i+1):

# 			# printing stars
# 			print("* ",end="")

# 		# ending line after each row
# 		print("\r")