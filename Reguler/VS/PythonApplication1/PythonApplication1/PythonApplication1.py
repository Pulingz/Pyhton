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



