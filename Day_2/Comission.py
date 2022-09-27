name=input("What is your name? ")
amount_sold=int(input("how much you sold this month? "))
comisson=int(input("Enter the comission percentage: "))
sales_comission=amount_sold*13/100


print(f"{name} earned commision of {sales_comission} on this month")