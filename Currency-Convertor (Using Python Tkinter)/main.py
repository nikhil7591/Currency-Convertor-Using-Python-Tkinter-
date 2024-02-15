import re
import requests
import tkinter as tk
from tkinter import ttk, messagebox
import json

# class for api
class RealTimeCurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        amount = round(amount * self.currencies[to_currency], 4)
        return amount
# class for GUI
class App(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title('Currency Converter')
        self.config(bg="#202630")
        self.currency_converter = converter
        self.geometry('650x350')

        self.img = tk.PhotoImage(file="OIG.png")
        self.iconphoto(False, self.img)
# label for photo_label
        self.Photo_label = tk.Label(self, fg="#202630", image=self.img)
        self.Photo_label.place(x=120, y=5)

        self.intro_label = tk.Label(self, text='Currency Converter', bg="#202630", fg='white')
        self.intro_label.config(font=('helvetica', 23, 'bold'))
        self.intro_label.place(x=180, y=5)

        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
# label for amount
        self.amount = tk.Label(self, text="Amount :", font="Helvetica 16 bold", bg="#202630", fg="#FFFFFF")
        self.amount.place(x=170, y=180)

        self.amount_field = tk.Entry(self, justify=tk.CENTER, validate='key', validatecommand=valid, font='Arial 12 bold', width=15)
        self.amount_field.place(x=290, y=183)
#  label for converted amount
        self.convert_amount = tk.Label(self, text="Converted Amount:", font="Helvetica 16 bold", bg="#202630", fg="#FFFFFF")
        self.convert_amount.place(x=100, y=220)
        self.converted_amount_field_label = tk.Label(self, text='', fg='black', bg='white', font='Arial 12 bold', width=15)
        self.converted_amount_field_label.place(x=356, y=224)

        self.from_currency_variable = tk.StringVar(self)
        self.from_currency_variable.set('INR')
        self.to_currency_variable = tk.StringVar(self)
        self.to_currency_variable.set('USD')

        font = ("courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
# label from from to to change currency
        self.from_label = tk.Label(self, text="From :", font="Helvetica 16 bold", bg="#202630", fg="#FFFFFF")
        self.from_label.place(x=20, y=130)
      # dropdown list for from currency
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,
                                                   values=list(self.currency_converter.currencies.keys()), font='Arial 12 bold', width=15)
        self.from_currency_dropdown.place(x=115, y=135)
      # label to to change currency and dropdown list for to currency
        self.to_label = tk.Label(self, text="To :", font="Helvetica 15 bold", bg="#202630", fg="#FFFFFF")
        self.to_label.place(x=330, y=130)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                 values=list(self.currency_converter.currencies.keys()), font='Arial 12 bold', width=15)
        self.to_currency_dropdown.place(x=380, y=135)
#  converte button 
        self.convert_button = tk.Button(self, text='Convert', fg="white", bg="#710193", command=self.perform)
        self.convert_button.config(font='courier 12 bold')
        self.convert_button.place(x=200, y=280)
# reset button
        self.reset_button = tk.Button(self, text='Reset', fg="white", bg="#FF0000", command=self.reset)
        self.reset_button.config(font='courier 12 bold')
        self.reset_button.place(x=330, y=280)
# theme button for change theme
        self.themed = ['Default', 'Teal', 'Coral', 'Indigo', 'Lavender', 'Turquoise', 'Gold', 'Magenta', 'Terracotta',
                       'Mint Green', 'Sapphire']
        self.themevar = tk.StringVar(self)
        self.theme_button = ttk.Combobox(self, textvariable=self.themevar, values=self.themed, font='Arial 12 bold',
                                         width=14)
        self.theme_button.set("Change Themes")
        self.theme_button.place(x=460, y=280)
        self.theme_button.bind("<<ComboboxSelected>>", self.change_theme)
# function for change theme
    def change_theme(self, *args):
      a = ""
      b=""
      selected_value = self.theme_button.get()
      if selected_value == 'Default':
        self.configure(bg="#202630")
        a= "#202630"
        b = "white"
      elif selected_value == 'Teal':
        self.configure(bg="#008080")
        a= "#008080"
        b = "black"
      elif selected_value == 'Coral':
        self.configure(bg="#FF6F61")
        a= "#FF6F61"
        b = "black"
      elif selected_value == 'Indigo':
        self.configure(bg="#4B0082") 
        a= "#4B0082"
        b = "black"
      elif selected_value == 'Lavender':
        self.configure(bg="#E6E6FA") 
        a= "#E6E6FA"
        b = "black"
      elif selected_value == 'Turquoise':
        self.configure(bg="#40E0D0") 
        a= "#40E0D0"
        b = "black"
      elif selected_value == 'Gold':
        self.configure(bg="#FFD700")
        a= "#FFD700"
        b = "black"
      elif selected_value == 'Magenta':
        self.configure(bg="#FF00FF")
        a= "#FF00FF"
        b = "black"
      elif selected_value == 'Terracotta':
        self.configure(bg="#E2725B")  
        a= "#E2725B"
        b = "black"
      elif selected_value == 'Mint Green':
        self.configure(bg="#98FF98")
        a= "#98FF98"
        b = "black"
      elif selected_value == 'Sapphire':
        self.configure(bg="#0F52BA")
        a= "#0F52BA"
        b = "black"

      self.Photo_label.configure(bg=a,fg=b)
      self.intro_label.configure(bg=a,fg=b)
      self.amount.configure(bg=a,fg=b)
      self.from_label.configure(bg=a,fg=b)
      self.to_label.configure(bg=a,fg=b)
      self.convert_amount.configure(bg=a,fg=b)

# function for convert button
    def perform(self):
        try:
            amount = float(self.amount_field.get())
            from_currency = self.from_currency_variable.get()
            to_currency = self.to_currency_variable.get()
            converted_amount = self.currency_converter.convert(from_currency, to_currency, amount)
            converted_amount = round(converted_amount, 2)
            self.converted_amount_field_label.config(text=str(converted_amount))

            if hasattr(self, 'date_label'):
                self.date_label.config(
                    text=f"1 {from_currency} = {self.currency_converter.convert(from_currency, to_currency, 1)} {to_currency} \nDate: {self.currency_converter.data['date']}")
            else:
                self.date_label = tk.Label(self,
                                           text=f"1 {from_currency} = {self.currency_converter.convert(from_currency, to_currency, 1)} {to_currency} \nDate: {self.currency_converter.data['date']}",
                                           font="helvetica 15 bold")
                self.date_label.pack(pady=70)

            user_data = {
                "Date": self.currency_converter.data['date'],
                "from": from_currency,
                "to": to_currency,
                "amount": amount,
                "convert_amount": converted_amount
            }
            self.save_to_json(user_data)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
#  function for save to json file
    def save_to_json(self, user_data):
        with open('main.json', 'a') as file:
            json.dump(user_data, file, indent=4)

  # function for reset button
    def reset(self):
        self.amount_field.delete(0, 'end')
        self.converted_amount_field_label.config(text='')
        self.from_currency_variable.set('INR')
        self.to_currency_variable.set('USD')
        if hasattr(self, 'date_label'):
            self.date_label.destroy()
            del self.date_label

# This function validates the input for the amount field
    def restrictNumberOnly(self, action, string):
      # Allow only alphanumeric characters and an optional decimal point
        regex = re.compile(r"^[a-zA-Z0-9]*\.?[0-9]*$")
      # if the action is insert, insert only alphanumeric characters and an optional decimal point
        result = regex.match(string)
      # if the action is delete, delete only alphanumeric characters and an optional decimal point
        return (string == "" or result is not None)


if __name__ == '__main__':
  # api url
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)
    app = App(converter)
    app.mainloop()
