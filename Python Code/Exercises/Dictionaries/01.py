def currency_symbol(str):
    currencies: dict = {
        'EURO': '€',
        'DOLLAR': '$',
        'YEN': '¥'
    }
    if str in currencies:
        return currencies[str]
    else:
        return "Not Found"




if __name__ == "__main__":
    str = input("Enter the name of the money: ")
    str = str.upper()
    print(currency_symbol(str))