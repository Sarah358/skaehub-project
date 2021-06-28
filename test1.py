# import modules
import json as json
import requests as requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


converter = Tk()
converter.title('Currency converter app/Crypto-currency conveter app')
converter.geometry("800x800")

# create tabs
my_notebook = ttk.Notebook(converter)
my_notebook.pack(pady=5)   #padding


# create frames
currency_frame = Frame(my_notebook, width=780, height=780)
crypto_frame = Frame(my_notebook, width=780, height=780)

currency_frame.pack(fill="both",expand=1 )
crypto_frame.pack(fill="both",expand=1 )

# add tabs
my_notebook.add(currency_frame,text='currencies')
my_notebook.add(crypto_frame,text='cryptocurrency')

# ################
# currencies
###############

# app name
app_name = Label(currency_frame, text='Currency Converter App',font=('aerial',25,'bold','underline'),fg='dark red')
app_name.pack(pady=20)



# amount label
amount_label = LabelFrame(currency_frame, text='Amount To Convert...',font=('aerial',15,'bold','underline'),fg='red')
amount_label.pack(pady=20)

# amount entry 
amount_entry = Entry(amount_label,font=('aerial',24))
amount_entry.pack(padx=10,pady=10)









# results frame
results_label = LabelFrame(currency_frame, text='Results....',font=('aerial',22,'bold','underline'),fg='black')
results_label.pack(pady=20)

# results text 
results = Text(results_label,height=3,width=30,font=('aerial',10,'bold'),bd=5)
results.pack(padx=3)













converter.mainloop()