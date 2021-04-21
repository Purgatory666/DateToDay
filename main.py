print("Date to Day")
print()
month = int(input("Please enter month EG: 1 for January: "))

if month>=13 or month<=0:
    print("Please enter valid number")
    exit()

date = int(input("Please enter date EG: 22: "))

if date>=32 or month<=0:
    print("Please enter valid number")
    exit()

year = int(input("Please enter year | Note: Year should not be greater than 2099 and less than 1501 | EG: 2020: "))

if year<=1500 or year>=2099:
    print("Please enter valid number")
    exit()


month_kode = [1,4,4,0,2,5,0,3,6,1,4,6]
year_kode = [0,6,4,2,0,6]
day_kode = [0,1,2,3,4,5,6]


a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0

year2 = year

a1 = date
month = month - 1
month = month_kode[month]
a2 = month


if year>=1500 and year<=1599:
    year2 = year_kode[0]

if year>=1600 and year<=1699:
    year2 = year_kode[1]

if year>=1700 and year<=1799:
    year2 = year_kode[2]

if year>=1800 and year<=1899:
    year2 = year_kode[3]

if year>=1900 and year<=1999:
    year2 = year_kode[4]

if year>=2000 and year<=2099:
    year2 = year_kode[5]

a3 = year2

a4 = year % 100

a5 = a4 / 4
a5 = int(a5)

a6 = a1 + a2 + a3 + a4 + a5

a7 = a6 % 7
a8 = 0
a8 = day_kode[a7]

if a8 == 0:
    print("The day is Saturday")

if a8 == 1:
    print("The day is Sunday")

if a8 == 2:
    print("The day is Monday")

if a8 == 3:
    print("The day is Tuesday")

if a8 == 4:
    print("The day is Wednesday")

if a8 == 5:
    print("The day is Thursday")

if a8 == 6:
    print("The day is Friday")
