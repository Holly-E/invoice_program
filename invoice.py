import discount_module

#\n creates new line
print('The Invoice Program\n')

# \t tabs out to line up our output
customer_type = input('Enter customer type (retail/wholesale):\t')
purchase_total = float(input('Enter purchase total:\t\t\t'))

#use discount module to calculate discount
discount = discount_module.discount(customer_type, purchase_total)
discount_percent = discount * 100
discount_amount = purchase_total * discount
invoice = format((purchase_total - discount_amount), '.2f')

#sep="" gets rid of the space around the variable
print('Total Purchase: \t\t\t', purchase_total, sep="")
print('Discount Percent: \t\t\t', discount_percent, '%', sep="")
print('Discount Amount: \t\t\t', discount_amount, '\n', sep="")
print('New Invoice Total:\t\t\t$', invoice, sep="")
print('Thank you for your business!')
