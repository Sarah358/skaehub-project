from forex_python.converter import CurrencyCodes, CurrencyRates
from forex_python.bitcoin import BtcConverter

test = CurrencyCodes()

cur_symbol = test.get_symbol('KES')
cur_name = test.get_currency_name('KES')

print('currency name is : ' +cur_name)
print('currency symbol is: ' +cur_symbol)

b = BtcConverter() 

print(b.convert_btc_to_cur(1, 'KES') )  # convert_btc_to_cur(1.25, 'USD')
