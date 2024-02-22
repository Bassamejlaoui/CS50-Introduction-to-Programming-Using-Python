import requests
from bs4 import BeautifulSoup

def rate_parser(input_curr, output_curr):
    url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From={input_curr}&To={output_curr}"
    try:
        content = requests.get(url).text
        soup = BeautifulSoup(content, 'html.parser')
        result_element = soup.find("p", class_="result__BigRate-sc-1bsijpp-1 dPdXSB")
        if result_element:
            currency_text = result_element.get_text().replace(',', '')  # Remove comma
            rate = float(currency_text.split()[0])
            return rate
        else:
            print(f"Element not found for {input_curr} to {output_curr}.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def convert(base, dest, amount):
    rate = rate_parser(base, dest)
    if rate is not None:
        new_amount = rate * amount
        return rate, new_amount
    else:
        return None

currencies = ["USD", "EUR", "CAD", "MAD", "GBP", "AUD", "JPY"]

def get_valid_currency_input(prompt, valid_currencies):
    user_input = input(prompt)
    while user_input not in valid_currencies:
        print("Invalid currency entered. Please choose from the supported currencies.")
        user_input = input(prompt)
    return user_input

def print_supported_currencies():
    print("Supported Currencies: ", currencies)

def main():
    print("Welcome to the Currency Converter!")

    while True:
        try:
            amount = float(input("Enter the amount: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print_supported_currencies()

    print("Choose the source currency:")
    base = get_valid_currency_input("Enter source currency: ", currencies)

    print_supported_currencies()

    print("Choose the destination currency:")
    dest = get_valid_currency_input("Enter destination currency: ", currencies)

    current_rate, converted_amount = convert(base, dest, amount)
    if current_rate is not None and converted_amount is not None:
        print("\nConversion Result:")
        print(f"Amount: {amount} {base}")
        print(f"From currency: {base}")
        print(f"To currency: {dest}")
        print(f"Current exchange rate: 1 {base} = {current_rate} {dest}")
        print(f"Converted amount: {converted_amount} {dest}")

if __name__ == '__main__':
    main()
