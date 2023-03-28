#Task2
# WAP to check year is leap year or not...
year = int(input("Enter years:"))

if year % 4 == 0 :
    print("year is leap year",year)
elif year % 100 == 0:
     print("year is not leap year",year)
elif year % 400 == 0:
     print("year is leap year",year)
else:
     print("year is  not leap year",year)
