# Alberto Guzman-Alvarez

# Project 1:

taxable_subtotal = 0
nontaxable_subtotal = 0

# prompt for tax rate
tax_rate = float(input("Tax Rate (%):"))


# prompt error is tax is outside range
if tax_rate < 0 or tax_rate > 20:
    print("Tax Rate is Outside Range!")
else:

    # prompt for number of times
    num_items = int(input("Number of items:"))

# prompt for items price
    for i in range(1, num_items + 1):
        taxable_total = float(input("Item Price ($):"))
        apply_tax = input("Is item taxable (y/n)?")
        if apply_tax == 'y':
            taxable_subtotal += taxable_total
        else:
            nontaxable_subtotal += taxable_total

    # calculate tax owed
    tax = taxable_subtotal * (tax_rate / 100)

    # print
print('Subtotal: $', format(taxable_subtotal + nontaxable_subtotal, '4.2f'))
print('Tax: $', format(tax, '4.2f'))
print('Total:$', format(taxable_subtotal + nontaxable_subtotal + tax, '4.2f'))
