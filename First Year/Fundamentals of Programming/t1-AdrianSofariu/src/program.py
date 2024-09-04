#
# Functions section
#
def create_phone(manufacturer: str, model: str, price: int) -> dict:
    """
    Function that creates a dict to store information about a phone
    :param manufacturer: string describing the manufacturer
    :param model: string describing the model
    :param price:
    :return: dict with phone information
    """
    phone = {"manufacturer": manufacturer, "model": model, "price": price}
    return phone


def get_manufacturer(phone: dict):
    return phone["manufacturer"]


def get_model(phone: dict):
    return phone["model"]


def get_price(phone: dict):
    return phone["price"]


def increase_price(phone: dict, new_price: int):
    phone["price"] += new_price


def add_phone_to_list(offer: list, phone: dict):
    """
    Procedure to add a phone to the store offer
    :param offer:
    :param phone:
    :return:
    """
    offer.append(phone)


def find_matching_phones(producer: str, store_offer: list) -> list:
    """
    Function to find all phones that contain string producer in the manufacturer string
    :param producer: string
    :param store_offer: list of phones
    :return: list of phones that match the condition or if producer is empty the whole list
    """
    matching = []
    if producer != "":
        for phone in store_offer:
            if producer.lower() in get_manufacturer(phone).lower():
                matching.append(phone)
        return matching
    else:
        return store_offer


def increase_phone_price(manufacturer: str, model: str, price: int, store_offer: list):
    """
    Procedure to update a phones price based on model and manufacturer
    :param manufacturer: string
    :param model: string
    :param price: new price, should be a numeric string
    :param store_offer: list of phones
    :return:
    """
    phone_in_list(manufacturer, model, store_offer)
    for phone in store_offer:
        if get_manufacturer(phone) == manufacturer and get_model(phone) == model:
            increase_price(phone, price)


def phone_in_list(manufacturer: str, model: str, store_offer: list):
    """
    Procedure to check if the model is in our list
    :param manufacturer: string
    :param model: string
    :param store_offer: list of phones
    :return:
    raise ValueError if phone is not in list
    """
    in_list = False
    for phone in store_offer:
        if get_manufacturer(phone) == manufacturer and get_model(phone) == model:
            in_list = True
    if not in_list:
        raise ValueError("Phone not in our list")


def increase_price_of_all_phones(increase: int, store_offer: list):
    """
    Procedure to increase the price of all phones by given percent
    :param increase: integer
    :param store_offer: list of phones
    :return:
    """
    for phone in store_offer:
        current_price = get_price(phone)
        additive = (increase*current_price)//100
        increase_price(phone, additive)

#
# User interface section
#
def check_input(manufacturer: str, model: str, price: str):
    """
    Procedure to check the input of the user when creating a phone
    :param manufacturer: string
    :param model: string
    :param price: string, should be numeric
    :return:
    raises ValueError if the length of a string is less than 3 or if the price is not numeric
    """
    if len(manufacturer) < 3:
        raise ValueError("Manufacturer name too short")
    if len(model) < 3:
        raise ValueError("Model name too short")
    if not price.isnumeric() or len(price) < 3:
        raise ValueError("Invalid price")


def add_phone_functionality(store_offer: list):
    """
    Procedure to add a phone to the store offer list
    :param store_offer: list containing phone dictionaries
    :return:
    """
    print("Please provide the information regarding the new phone")
    manufacturer = input("Provide a manufacturer: ").strip()
    model = input("Provide the model: ").strip()
    price = input("Provide the price: ").strip()
    check_input(manufacturer, model, price)
    add_phone_to_list(store_offer, create_phone(manufacturer, model, int(price)))


def display_all_phones_of_producer_functionality(store_offer: list):
    """
    Procedure to handle the display all phones from given manufacturer functionality
    :param store_offer: list of phones
    :return:
    raises ValueError if match fails
    """
    producer = input("Please enter the producer name: ").strip()
    matching = find_matching_phones(producer, store_offer)
    if len(matching) >= 1:
        for phone in matching:
            print(phone)
    else:
        raise ValueError("Couldn't find phones from " + producer)


def increase_phone_price_functionality(store_offer: list):
    """
    Procedure that reads input to increase the price of a phone
    :param store_offer:
    :return:
    """
    print("Please provide the information regarding the new phone")
    manufacturer = input("Provide a manufacturer: ").strip()
    model = input("Provide the model: ").strip()
    new_price = input("Provide the price: ").strip()
    if not new_price.isnumeric():
        raise ValueError("Price must be a number")
    increase_phone_price(manufacturer, model, int(new_price), store_offer)


def increase_price_of_all_phones_functionality(store_offer: list):
    """
    Procedure to read input to increase price of all phones by given percentage
    :param store_offer: list of phones
    :return:
    """
    increase = input("Percent with which to increase the price of all phones: ").strip()
    if not increase.isnumeric():
        raise ValueError("Percent must be a number")
    if int(increase) < -50 or int(increase) > 100:
        raise ValueError("Percent must be between -50 and 100")
    increase_price_of_all_phones(int(increase), store_offer)


def print_menu():
    """
    Function to print all menu options
    :return:
    """
    print("Welcome to the phone store.")
    print(" 1. Add a phone")
    print(" 2. Display all phones from given manufacturer")
    print(" 3. Increase price for a phone model")
    print(" 4. Increase price for all phones with x%")
    print(" 5. Exit")
    print("Please choose an option")


def input_handler():
    """
    Driver procedure to handle input and commands
    :return:
    """
    phone_list = []
    while True:
        print_menu()
        option = input(">>").strip()
        try:
            if option == "1":
                add_phone_functionality(phone_list)
            if option == "2":
                display_all_phones_of_producer_functionality(phone_list)
            if option == "3":
                increase_phone_price_functionality(phone_list)
            if option == "4":
                increase_price_of_all_phones_functionality(phone_list)
            if option == "5":
                break
            else:
                raise ValueError("Incorrect command")
        except ValueError as v:
            print(v)


if __name__ == "__main__":
    input_handler()
