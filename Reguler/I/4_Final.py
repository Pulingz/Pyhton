#variable + concat
# Band name generator
# 1 Create greeting for you program like "Welcome to the band name generator"
# 2 Ask the user which city did you grew up // jakarta
# 3 Ask the user for the name pet? // Rabbit
# Output  "Your band name could be ${city} ${pet}" //"Your band name could be Jakaart Rabbit"

# solution
# inputan
city = input("Ask the user which city did you grew up ? ")
pet = input("Ask the user for the name pet? ")

# output
print("Your band name could be {1} {0}".format(city, pet))
print(f"Your band name could be {city} {pet}")
