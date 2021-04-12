# def grettings():
#     print("Halo Apa Kabar")

# grettings()

# def sum(a,b):
#     return a + b

# print(sum(3,4))

# def x(value):
#     return sum(value)

# print(x([1,2,3,4,5]))


# def avg(value):
#     return sum(value)/len(value)

# print(avg([5,5,5,2]))

# def grettings(nama="udin"):
#     print(f"Halo Apa Kabar {nama}")


# grettings()

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        # print(i)
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's prime number")
    else:
        print("Not prime number")


n = int(input("Check Number : " ))
prime_checker(number=n)

