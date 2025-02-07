import requests

# Replace with your actual API key from ExchangeRate API
# On ExchangeRate users can have a free API key. 500 requests as of currently in 2025.
API_KEY = " "
BASE_URL = "https://v6.exchangerate-api.com/v6"


def get_exchange_rate(base_currency, target_currency):
    """
    Fetches the real-time exchange rate between two currencies using ExchangeRate API.
    """
    url = f"{BASE_URL}/{API_KEY}/latest/{base_currency}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print("❌ API Error: Unable to fetch exchange rates.")
            return None

        rates = data.get("conversion_rates", {})

        if target_currency in rates:
            return rates[target_currency]
        else:
            print("❌ Invalid target currency. Please try again.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        return None


def convert_currency(amount, base_currency, target_currency):
    """
    Converts an amount from one currency to another.
    """
    rate = get_exchange_rate(base_currency, target_currency)

    if rate is not None:
        converted_amount = round(amount * rate, 2)
        print(f"💱 {amount} {base_currency} = {converted_amount} {target_currency}")
    else:
        print("❌ Conversion failed. Please check your inputs.")


if __name__ == "__main__":
    print("🌍 Welcome to the Real-Time Currency Converter!")

    try:
        amount = float(input("Enter the amount to convert: "))
        base_currency = input("Enter the base currency (e.g., USD, EUR): ").upper()
        target_currency = input("Enter the target currency (e.g., GBP, JPY): ").upper()

        convert_currency(amount, base_currency, target_currency)
    except ValueError:
        print("❌ Invalid amount. Please enter a valid number.")
