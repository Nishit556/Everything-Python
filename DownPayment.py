Price = input('Price')
print(type(Price))
good_credit= True
if good_credit:
    down_payment = 0.1 * float(Price)
else :
    down_payment = 0.2 * float(Price)
print(f"Down Payment is {down_payment}")

