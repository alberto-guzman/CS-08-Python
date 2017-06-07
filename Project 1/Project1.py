# Alberto Guzman-Alvarez

# Project 1:

# prompt for tax rate
tax_rate = float(input("Tax Rate (%):"))

# prompt error is tax is outside range
if tax_rate < 0 or tax_rate > 20:
    print("Tax Rate is Outside Range!")
else:

    # prompt for items price
    taxable_total = float(input("Item Price ($):"))
    apply_tax = input("Is item taxable (Y/N)?")

    # calculate tax owed
    tax = taxable_total * (tax_rate / 100)

    # print
    print('Subtotal: $', format(taxable_total, '4.2f'))
    print('Tax: $', format(tax, '4.2f'))

    # create total and print
    if apply_tax == 'Y':
        total = taxable_total + tax
        print('Total:$', format(total, '4.2f'))
    else:
        total = taxable_total
        print('Total:$', format(total, '4.2f'))
