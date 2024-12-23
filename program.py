# price and discount

def calculate_discount(price: int, discount_percent: int)-> int:
    if discount_percent >= 20:
        new_price = price * ((100 - 20) // 100) # round down to nearest whole number. eg 15 // 2 = 7
        return new_price
    else:
        return price
    
price = input("Price: ")
discount_percent = input("Discount percentage: ")

def validate_user_inputs(price: str, discount_percent: str)-> str:
    error = ""
    if price == "" or discount_percent == "":
        error = "you must enter a figure for both inputs."
        return error
    if not price.isnumeric():
        error = "price must be an integer."
        return error
    if int(price) < 5 or int(price) > 1000000:
        error = "invalid price."
        return error
    if not discount_percent.isnumeric():
        error = "discount must be an integer."
        return error
    if int(discount_percent) < 0 or int(discount_percent) > 100:
        error = "invalid percentage discount."
        return error
    return "iko sawa" # hahahaaaa

validation_result = validate_user_inputs(price, discount_percent)

while validation_result != "iko sawa":
    print("\n" + validation_result)
    price = input("Price: ")
    discount_percent = input("Discount percentage: ")
    validation_result = validate_user_inputs(price, discount_percent)

