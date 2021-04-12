# inputan
age = input("your age : ")
# proses deadline year 20
year_remaining = 20 - int(age)
# hitung bulan
month_remaining = year_remaining * 12
# hitung hari
days_remaining = year_remaining * 365
# hitung minggu
weeks_remaining = year_remaining * 52

# print(f"you have {year_remaining} year, {month_remaining} months, {weeks_remaining} weeks, {days_remaining} days remaining until 20")
print("you have" +year_remaining +"year"+month_remaining+"months")
# print("your score is " + str(score) + ", your height is " + str(height) )
