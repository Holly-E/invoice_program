"""calculates discount based on customer type and purchase total"""

def discount(customer_type, purchase_total):
    if customer_type == 'retail':
        if purchase_total < 100:
            return 0
        elif 100 <= purchase_total < 250:
            return .1
        elif 250 <= purchase_total < 500:
            return .2
        else:
            return .25
    elif customer_type == 'wholesale':
        if purchase_total < 500:
            return .3
        else:
            return .35
    else:
        return 0
