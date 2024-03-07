import logging
import requests


NBP_API_URL_DOLLAR = "http://api.nbp.pl/api/exchangerates/rates/a/usd/"  
NBP_API_URL_GOLD = "http://api.nbp.pl/api/cenyzlota"


class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.pln_rate = 1
        self.usd_rate = None
        self.gold_rate = None

        
        self.fetch_dollar_and_gold_rate()

    def fetch_dollar_and_gold_rate(self):
            usd_price_response = requests.get(NBP_API_URL_DOLLAR)
            gold_rate_response = requests.get(NBP_API_URL_GOLD)
            
            # Check for errors
            if usd_price_response.status_code != 200 or gold_rate_response.status_code != 200:
                logging.error("Failed to fetch rates: %s, %s", usd_price_response, gold_rate_response)
                return None
            
            self.usd_rate = usd_price_response.json()["rates"][0]["mid"]
            self.gold_rate = gold_rate_response.json()[0]["cena"]
            logging.info("Fetched rates: USD: %s, GOLD: %s", self.usd_rate, self.gold_rate)

    def convert(self, amount: float, from_currency: float, to_currency: float, result_value):
        # try to parse the ammount to float
        try:
            amount = float(amount)
        except ValueError:
            logging.error("Failed to parse amount to float: %s", amount)
            # alert the user
            result_value.set("Not a number")
            return None
        
        # check if the rates are fetched
        if self.usd_rate is None or self.gold_rate is None:
            logging.error("Rates not fetched")
            # alert the user
            result_value.set("Rates not fetched, check your internet connection and try again later.")
            return None
        
        # changing amount to PLN
        if(from_currency != "PLN"):
            if(from_currency == "USD"):
                amount = amount * self.usd_rate
            elif(from_currency == "GOLD"):
                amount = amount * self.gold_rate
        
        # converting from PLN to desired currency
        if(to_currency == "USD"):
            amount = amount / self.usd_rate
        elif(to_currency == "GOLD"):
            amount = amount / self.gold_rate
        
        result_value.set(round(amount,2))
        