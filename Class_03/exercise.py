import decimal # Decimal doesn't come standard with Python

customer_type = input("Enter customer type")
invoice_total = float(input("Enter invoice amount"))
discount_percent = 0.0 # The discount to be determined

if customer_type == "R":
    if invoice_total >= 100.00 and invoice_total < 250.00:
        discount_percent = 0.1
    elif invoice_total >= 250.00:
        discount_percent = 0.2
elif customer_type == "W":
    if invoice_total < 500.00:
        discount_percent = 0.4
    elif invoice_total >= 500.00:
        discount_percent = 0.5
else:
    print("Code is not valid.")

print(f"Discount determined is {discount_percent}")