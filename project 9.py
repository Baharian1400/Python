income=int(input())
if (income<=1000):
    taxrate=0
else:
    if ((income>1000) and (income<=2500)):
        taxrate=10
    else:
        if ((income>2500) and (income<=4000)):
            taxrate=15
        else:
            if ((income>4000) and (income<=6000)):
                taxrate=20
            else:
                if (income>8000):
                    taxrate=30
print(taxrate)
print(income)
print("net_income=",income-(taxrate/100)*income) 
