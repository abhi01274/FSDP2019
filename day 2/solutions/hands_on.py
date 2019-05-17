a =list(range(1,10))
print("evens are >")
for i in a:
    if i%2==0:
        print(i)
print("odds are >")
for i in a:
    if i%2==0:
        continue
    else:
        print (i)

        
#_----------------------------------------------------
        
        
def ly(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        print("leap yaer")
    else:
        print("not a leap year")

ly(1990)



#----------------------------------------------------------
month = input("type the month")
month= month.lower()
def days_in_month(mon):
    if mon =='january' or 'march' or 'may' or 'july' or 'august' or 'october' or 'december':
        print(mon,"has 31 days")
    elif mon == 'april' or 'june' or 'september' or 'november':
        print(mon,"has 30 days")
    elif mon=='february':
        print(mon, "has 28/29 days")
    else:
        print("please enter the valid month")
days_in_month(month)
