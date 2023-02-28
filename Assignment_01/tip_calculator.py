# Using decimal data type to deal with currency
import decimal

# Federal and provincial sales tax rates used to calculate the pre-tip total of the meal
FED_TAX_RATE = 0.05
QC_TAX_RATE = 0.09975

nb_diners = int(input("Please enter the number of diners"))

while True:
    price_meal = input("Please enter the price of the meal, before tax")

    # Check if price entered is a number
    try:
        price_meal = decimal.Decimal(price_meal)
        break
    except:
        print("Sorry, please enter a number")

while True:
    tip_pct = input("Please choose the tip \n 1) Exceptional 20%, 2) Good 15%, 3) Basic 10%, 4) Horrible 0%")

    # Assign the tip percentage based on the option selected
    if tip_pct in "1234" and len(tip_pct) == 1:
        if tip_pct == "1":
            tip_pct = 0.2
        elif tip_pct == "2":
            tip_pct = 0.15
        elif tip_pct == "3":
            tip_pct = 0.1
        elif tip_pct == "4":
            tip_pct = 0
        break
    else:
        print("Sorry, please choose option 1, 2, 3 or 4")

# Calculate the outputs to display
fed_tax_added = price_meal * decimal.Decimal(FED_TAX_RATE)
qc_tax_added = price_meal * decimal.Decimal(QC_TAX_RATE)
total_inc_tax = fed_tax_added + qc_tax_added + price_meal
tip_amount = price_meal * decimal.Decimal(tip_pct)
grand_total = total_inc_tax + tip_amount
amount_per_person = grand_total / nb_diners

# Find the length of the longest line in the print-out to right justify all numbers
longest_line = len("The grand total including taxes and tips:")

# Print all amounts and numbers in the correct format and right justify with reference to the longest line
print(f"{'The number of diners: ':<{longest_line}s} {nb_diners}")
print(f"{'The price of the meal before tax: ':<{longest_line}s} ${price_meal:0.2f}")
print(f"{'GST: ':<{longest_line}s} ${fed_tax_added:0.2f}")
print(f"{'QST: ':<{longest_line}s} ${qc_tax_added:0.2f}")
print(f"{'The total including tax: ':<{longest_line}s} ${total_inc_tax:0.2f}")
print(f"{'Tip amount: ':<{longest_line}s} ${tip_amount:0.2f}")
print("The grand total including taxes and tips: ${0:.2f}".format(grand_total))
print(f"{'The amount owed per person: ':<{longest_line}s} ${amount_per_person:0.2f}")
