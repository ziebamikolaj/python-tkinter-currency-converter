from tkinter import Tk
from ui import setup_ui
from currency_converter import CurrencyConverter

def main():
    root = Tk()
    currency_converter = CurrencyConverter(root)
    setup_ui(root, currency_converter)
    root.mainloop() 

if __name__ == "__main__":
    main()