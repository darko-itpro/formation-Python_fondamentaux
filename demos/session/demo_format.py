PRICE_FR = "Prix : {} {}"
CURRENCY_EU = "€"


def display_price(template:str, price:float, currency:str):
    print(template.format(price, currency))
