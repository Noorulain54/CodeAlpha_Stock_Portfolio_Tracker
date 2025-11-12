import tkinter as tk
from tkinter import messagebox

# --- Hardcoded stock prices ---
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

# --- Portfolio dictionary ---
portfolio = {}

# --- Functions ---
def add_stock():
    stock = entry_stock.get().upper()
    qty = entry_qty.get()

    if stock not in stock_prices:
        messagebox.showerror("Error", f"{stock} not found! Choose from: {', '.join(stock_prices.keys())}")
        return
    
    if not qty.isdigit():
        messagebox.showerror("Error", "Quantity must be a number!")
        return
    
    qty = int(qty)
    portfolio[stock] = portfolio.get(stock, 0) + qty
    entry_stock.delete(0, tk.END)
    entry_qty.delete(0, tk.END)
    update_summary()

def update_summary():
    text_summary.delete("1.0", tk.END)
    total = 0
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        investment = qty * price
        total += investment
        text_summary.insert(tk.END, f"{stock}: {qty} × ${price} = ${investment}\n")
    text_summary.insert(tk.END, f"\nTotal Investment: ${total}")

def save_to_file():
    total = 0
    with open("portfolio_gui.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("-" * 40 + "\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = qty * price
            total += investment
            f.write(f"{stock}: {qty} × ${price} = ${investment}\n")
        f.write("-" * 40 + "\n")
        f.write(f"Total Investment: ${total}\n")
    messagebox.showinfo("Saved", "Portfolio saved as 'portfolio_gui.txt'")

# --- GUI Window ---
root = tk.Tk()
root.title("📈 Stock Portfolio Tracker")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# --- Labels & Entries ---
tk.Label(root, text="Enter Stock Symbol:", bg="#f0f0f0").pack()
entry_stock = tk.Entry(root)
entry_stock.pack()

tk.Label(root, text="Enter Quantity:", bg="#f0f0f0").pack()
entry_qty = tk.Entry(root)
entry_qty.pack()

# --- Buttons ---
tk.Button(root, text="Add Stock", command=add_stock, bg="#007bff", fg="white").pack(pady=5)
tk.Button(root, text="Save to File", command=save_to_file, bg="#28a745", fg="white").pack(pady=5)

# --- Summary Box ---
tk.Label(root, text="\nPortfolio Summary:", bg="#f0f0f0").pack()
text_summary = tk.Text(root, height=10, width=40)
text_summary.pack()

# --- Run Window ---
root.mainloop()
