#task:1
'''
Take input from user in terms of days and convert them into no.of years
and months
'''
days =int(input("Enter no.of days:"))

years =days // 365

weeks = ((days%365)/7)

days = ((days%365)%7)

print("no.of years:",years)
print("no.of days:",days)
print("no.of weeks:",weeks)
