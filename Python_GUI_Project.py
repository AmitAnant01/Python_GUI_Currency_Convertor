import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class CurrencyConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("INR Currency Converter")
        self.window.geometry("700x600")
        self.window.configure(bg="#f0f0f0")

        # Heading Label
        heading_label = tk.Label(self.window, text="Welcome to Currencies Converter", bg="#f0f0f0",
                           font=("Helvetica", 18, "bold"))
        heading_label.grid(row=0, column=0, columnspan=3, padx=10, pady=20)
        heading_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        self.exchange_rates = {
        "🇺🇸 United States (USD)": 82.5,
        "🇪🇺 European Union (EUR)": 90.0,
        "🇬🇧 United Kingdom (GBP)": 105.0,
        "🇯🇵 Japan (JPY)": 0.56,
        "🇦🇺 Australia (AUD)": 55.0,
        "🇨🇦 Canada (CAD)": 60.0,
        "🇨🇭 Switzerland (CHF)": 94.0,
         "🇨🇳 China (CNY)": 11.5,
        "🇳🇿 New Zealand (NZD)": 50.0,
        "🇸🇬 Singapore (SGD)": 61.0,
        "🇭🇰 Hong Kong (HKD)": 10.6,
        "🇰🇷 South Korea (KRW)": 0.063,
        "🇹🇭 Thailand (THB)": 2.3,
        "🇲🇾 Malaysia (MYR)": 17.7,
        "🇷🇺 Russia (RUB)": 0.92,
        "🇿🇦 South Africa (ZAR)": 4.4,
        "🇧🇷 Brazil (BRL)": 16.8,
        "🇲🇽 Mexico (MXN)": 4.8,
        "🇦🇪 UAE (AED)": 22.5,
        "🇸🇦 Saudi Arabia (SAR)": 22.0,
            "🇺🇸 United States (USD)": 82.5,
        "🇪🇺 European Union (EUR)": 90.0,
        "🇬🇧 United Kingdom (GBP)": 105.0,
        "🇯🇵 Japan (JPY)": 0.56,
        "🇦🇺 Australia (AUD)": 55.0,
        "🇨🇦 Canada (CAD)": 60.0,
        "🇨🇭 Switzerland (CHF)": 94.0,
        "🇨🇳 China (CNY)": 11.5,
        "🇳🇿 New Zealand (NZD)": 50.0,
        "🇸🇬 Singapore (SGD)": 61.0,
        "🇭🇰 Hong Kong (HKD)": 10.6,
        "🇰🇷 South Korea (KRW)": 0.063,
        "🇹🇭 Thailand (THB)": 2.3,
        "🇲🇾 Malaysia (MYR)": 17.7,
        "🇷🇺 Russia (RUB)": 0.92,
        "🇿🇦 South Africa (ZAR)": 4.4,
        "🇧🇷 Brazil (BRL)": 16.8,
        "🇲🇽 Mexico (MXN)": 4.8,
        "🇦🇪 UAE (AED)": 22.5,
        "🇸🇦 Saudi Arabia (SAR)": 22.0,
        "🇦🇷 Argentina (ARS)": 0.094,
        "🇪🇬 Egypt (EGP)": 2.0,
        "🇳🇬 Nigeria (NGN)": 0.099,
        "🇮🇩 Indonesia (IDR)": 0.0053,
        "🇵🇰 Pakistan (PKR)": 0.30,
        "🇧🇩 Bangladesh (BDT)": 0.75,
        "🇵🇭 Philippines (PHP)": 1.48,
        "🇻🇳 Vietnam (VND)": 0.0035,
        "🇹🇷 Turkey (TRY)": 2.6,
        "🇮🇱 Israel (ILS)": 22.0,
        "🇮🇷 Iran (IRR)": 0.0016,
        "🇮🇶 Iraq (IQD)": 0.063,
        "🇦🇫 Afghanistan (AFN)": 0.96,
        "🇳🇵 Nepal (NPR)": 0.63,
        "🇧🇹 Bhutan (BTN)": 1.0,
        "🇱🇰 Sri Lanka (LKR)": 0.28,
        "🇲🇲 Myanmar (MMK)": 0.039,
        "🇰🇭 Cambodia (KHR)": 0.020,
        "🇰🇼 Kuwait (KWD)": 270.0,
        "🇶🇦 Qatar (QAR)": 22.5,
        "🇧🇭 Bahrain (BHD)": 220.0,
        "🇴🇲 Oman (OMR)": 215.0,
        "🇾🇪 Yemen (YER)": 0.33,
        "🇸🇾 Syria (SYP)": 0.052,
        "🇱🇧 Lebanon (LBP)": 0.0055,
        "🇯🇴 Jordan (JOD)": 117.0,
        "🇵🇸 Palestine (ILS)": 22.0,
        "🇹🇳 Tunisia (TND)": 26.0,
        "🇲🇦 Morocco (MAD)": 8.0,
        "🇩🇿 Algeria (DZD)": 0.61,
        "🇰🇪 Kenya (KES)": 0.64,
        "🇺🇬 Uganda (UGX)": 0.022,
        "🇹🇿 Tanzania (TZS)": 0.032,
        "🇪🇹 Ethiopia (ETB)": 1.45,
        "🇸🇩 Sudan (SDG)": 0.14,
        "🇨🇩 Congo (CDF)": 0.027,
        "🇨🇲 Cameroon (XAF)": 0.14,
        "🇸🇳 Senegal (XOF)": 0.14,
        "🇬🇭 Ghana (GHS)": 7.0,
        "🇿🇲 Zambia (ZMW)": 3.7,
        "🇲🇼 Malawi (MWK)": 0.048,
        "🇲🇿 Mozambique (MZN)": 1.3,
        "🇧🇼 Botswana (BWP)": 6.3,
        "🇳🇦 Namibia (NAD)": 4.4,
        "🇦🇴 Angola (AOA)": 0.10,
        "🇷🇴 Romania (RON)": 18.0,
        "🇵🇱 Poland (PLN)": 21.0,
        "🇭🇺 Hungary (HUF)": 0.23,
        "🇨🇿 Czech Republic (CZK)": 3.6,
        "🇸🇰 Slovakia (EUR)": 90.0,
        "🇸🇮 Slovenia (EUR)": 90.0,
        "🇭🇷 Croatia (EUR)": 90.0,
        "🇧🇬 Bulgaria (BGN)": 46.0,
        "🇷🇸 Serbia (RSD)": 0.83,
        "🇬🇷 Greece (EUR)": 90.0,
        "🇮🇹 Italy (EUR)": 90.0,
        "🇪🇸 Spain (EUR)": 90.0,
        "🇫🇷 France (EUR)": 90.0,
        "🇩🇪 Germany (EUR)": 90.0,
        "🇧🇪 Belgium (EUR)": 90.0,
        "🇳🇱 Netherlands (EUR)": 90.0,
        "🇸🇪 Sweden (SEK)": 8.3,
        "🇳🇴 Norway (NOK)": 7.8,
        "🇩🇰 Denmark (DKK)": 12.0,
        "🇫🇮 Finland (EUR)": 90.0,
        "🇮🇸 Iceland (ISK)": 0.60,
        "🇵🇹 Portugal (EUR)": 90.0,
        "🇨🇱 Chile (CLP)": 0.090,
        "🇵🇪 Peru (PEN)": 22.0,
        "🇨🇴 Colombia (COP)": 0.021,
        "🇺🇾 Uruguay (UYU)": 2.1,
        "🇵🇦 Panama (USD)": 82.5,
        "🇨🇷 Costa Rica (CRC)": 0.15,
        "🇬🇹 Guatemala (GTQ)": 10.5,
        "🇩🇴 Dominican Republic (DOP)": 1.5,
        "🇯🇲 Jamaica (JMD)": 0.54,
        "🇹🇹 Trinidad & Tobago (TTD)": 12.0,
        "🇧🇸 Bahamas (BSD)": 82.5,
        "🇧🇧 Barbados (BBD)": 41.0,
        "🇧🇿 Belize (BZD)": 41.0,
        "🇫🇯 Fiji (FJD)": 37.0,
        "🇵🇬 Papua New Guinea(PGK)":22.5
        } # Here you can add more countries also.

        # Generate Historical Dummy Data for fluctuation simulation
        self.generate_historical_rates()

        # Currency dropdown
        tk.Label(self.window, text="Select Currency:", bg="#ffff00", fg="#00698f", 
                 font=("Helvetica", 12, "bold")).grid(row=1, column=0, padx=10, pady=10)
        self.selected_currency = tk.StringVar(self.window)
        self.selected_currency.set(list(self.exchange_rates.keys())[0])
        ttk.Combobox(self.window, textvariable=self.selected_currency,
                     values=list(self.exchange_rates.keys()), state='readonly').grid(row=1, column=1, padx=10, pady=10)

        # Amount input 
        tk.Label(self.window, text="Enter Amount:", bg="#ffff00", fg="#00698f", 
                 font=("Helvetica", 12, "bold")).grid(row=2, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(self.window, width=20, bg="#ffffcc", font=("Helvetica", 12))
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)

        # For choose Date 
        tk.Label(self.window, text="Select Date:", bg="#ffff00", fg="#00698f", 
                 font=("Helvetica", 12, "bold")).grid(row=3, column=0, padx=10, pady=10)
        self.date_entry = DateEntry(self.window, width=18, background='darkblue', foreground='white', 
                                    borderwidth=2, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=3, column=1, padx=10, pady=10)

        # Making the Convert Buttons
        tk.Button(self.window, text="Convert to INR", command=self.convert_to_inr,
                  bg="#ffa500", font=("Helvetica", 12, "bold")).grid(row=4, column=0, pady=10)
        tk.Button(self.window, text="INR to Foreign", command=self.convert_from_inr,
                  bg="#90ee90", font=("Helvetica", 12, "bold")).grid(row=4, column=1, pady=10)

        # Clear Button
        tk.Button(self.window, text="Clear", command=self.clear_fields,
                  bg="#ff6666", font=("Helvetica", 12)).grid(row=4, column=2, padx=10)

        # Result Display
        self.result_label = tk.Label(self.window, text="", bg="#f0f0f0", fg="#008000",
                                     font=("Helvetica", 13, "bold"))
        self.result_label.grid(row=5, column=0, columnspan=3, pady=10)

        # Trend Button
        tk.Button(self.window, text="📈 Show 7-Day Trend", command=self.show_graph,
                  bg="#00bfff", font=("Helvetica", 12, "bold")).grid(row=15, column=0, columnspan=3, pady=10)

        self.window.mainloop()

    def generate_historical_rates(self):
        self.historical_rates = {}
        for currency, base_rate in self.exchange_rates.items():
            # Simulate a small random fluctuation around the base rate for 7 days
            self.historical_rates[currency] = [round(base_rate + random.uniform(-2, 2), 2) for _ in range(7)]

    def convert_to_inr(self):
        currency = self.selected_currency.get()
        date_selected = self.date_entry.get_date()
        today = datetime.today().date()

        try:
            amount = float(self.amount_entry.get())
            # Calculate index offset for historical data based on date difference
            day_offset = (today - date_selected).days

            # Use the historical rate if within a 7-day window
            if -3 <= day_offset <= 3:
                rate = self.historical_rates[currency][day_offset + 3]
            else:
                rate = self.exchange_rates[currency]

            result = amount * rate
            self.result_label.config(
                text=f"{amount:,.2f} {currency} = ₹{result:,.2f} INR\nExchange Rate on {date_selected}: ₹{rate}"
            )
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def convert_from_inr(self):
        currency = self.selected_currency.get()
        date_selected = self.date_entry.get_date()
        today = datetime.today().date()

        try:
            amount = float(self.amount_entry.get())
            day_offset = (today - date_selected).days

            if -3 <= day_offset <= 3:
                rate = self.historical_rates[currency][day_offset + 3]
            else:
                rate = self.exchange_rates[currency]

            result = amount / rate
            self.result_label.config(
                text=f"₹{amount:,.2f} INR = {result:,.2f} {currency}\nExchange Rate on {date_selected}: ₹{rate}"
            )
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def clear_fields(self):
        self.amount_entry.delete(0, tk.END)
        self.result_label.config(text="")

    def show_graph(self):
        currency = self.selected_currency.get()
        rates = self.historical_rates[currency]
        dates = [(datetime.today() + timedelta(days=i - 3)).strftime("%b %d") for i in range(7)]

        fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
        ax.plot(dates, rates, marker='o', color='blue', linewidth=2)
        ax.set_title(f"{currency} to INR - Last 7 Days")
        ax.set_ylabel("INR Rate")
        ax.grid(True)

        # Add data labels for each point
        for i, v in enumerate(rates):
            ax.text(i, v + 0.5, f"{v}", ha='center', fontsize=9)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=7, column=0, columnspan=3, pady=10)

if __name__ == "__main__":
    CurrencyConverter()


