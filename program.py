# price and discount

def calculate_discount(price: int, discount_percent: int)-> float:
    if discount_percent >= 20:
        new_price = price * ((100 - discount_percent) / 100) 
        return round(new_price, 2)
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

# calculate price
print(f"Final price = {calculate_discount(int(price), int(discount_percent))}")