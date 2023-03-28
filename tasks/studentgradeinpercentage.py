#Task5
'''WAP to display marks of 5 student in percentage and
also give grads according to percentage'''
'''
    RESULT


'''

PYTHON = int(input("enter marks PYTHON:"))
CNS = int(input("enter marks CNS:"))
JAVA = int(input("enter marks JAVA:"))
MCAD = int(input("enter marks MCAD:"))
NMA = int(input("enter marks NMA:"))

total = PYTHON+CNS+JAVA+MCAD+NMA
per =(total / 500)*100

print("Total Marks=",total)
print("Your percentage=",per)


if(per>=90):
     print("A Grade")
elif(per>=70):
     print("B Grade")
elif(per>=50):     
     print("C Grade")
else:
     print("You are FAIL")
  
