
"""
balance  = 1000
amount = "" 

while amount != -1:
    amount = int(input("enter the amount or press -1 to ext = "))

    if amount > balance:
        print("insufficient amount")

    elif amount == -1:
        break

    else:
        balance -= amount
        print(f"you have succefull withdraw the amount and you balance is {balance}")


"""