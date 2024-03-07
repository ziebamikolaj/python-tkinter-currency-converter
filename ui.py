import tkinter as tk
from tkinter import ttk

def setup_ui(root, currency_converter):
    root.configure(bg="#202327")  
    root.title("Currency Converter")
    root.geometry("300x200")
    root.resizable(False, False)
    
    # style
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TLabel', background="#202327", foreground="white")
    style.configure('TFrame', background="#202327")

    
    
    # Input Frame
    input_frame = ttk.Frame(root)
    input_frame.pack(pady=20)

    ttk.Label(input_frame, text="Amount:").grid(row=0, column=0, padx=5)
    input_value = tk.StringVar()
    input_entry = ttk.Entry(input_frame, textvariable=input_value)
    input_entry.grid(row=0, column=1, padx=5)

    # Currency Selection Frame
    currency_frame = ttk.Frame(root)
    currency_frame.pack(pady=10)

    ttk.Label(currency_frame, text="From:").grid(row=0, column=0, padx=5)
    from_combobox = ttk.Combobox(currency_frame, width=12, state="readonly")
    from_combobox['values'] = ['PLN', 'USD', 'GOLD']
    from_combobox.current(0)
    from_combobox.grid(row=0, column=1)

    ttk.Label(currency_frame, text="To:").grid(row=0, column=2, padx=5)
    to_combobox = ttk.Combobox(currency_frame, width=12, state="readonly")
    to_combobox['values'] = ['PLN', 'USD', 'GOLD']
    to_combobox.current(1)
    to_combobox.grid(row=0, column=3)

    # Result Frame
    result_frame = ttk.Frame(root)
    result_frame.pack(pady=10)

    ttk.Label(result_frame, text="Result:").grid(row=0, column=0, padx=5)
    result_value = tk.StringVar()
    result_label = ttk.Label(result_frame, textvariable=result_value)
    result_label.grid(row=0, column=1, padx=5)

    # Convert Button
    ttk.Button(root, text="Convert", command=lambda: currency_converter.convert(amount=input_value.get(), from_currency=from_combobox.get(), to_currency=to_combobox.get(), result_value=result_value)) \
        .pack(pady=10)

    # make labels and buttons look better
    for child in input_frame.winfo_children():
        child.grid_configure(pady=5, padx=5)
   