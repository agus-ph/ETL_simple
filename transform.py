from email import header
from extract import get_index_value, get_merval_value
from api_keys import twelvedata_api_key, bcra_header
import pandas as pd

# Traigo las autorizaciones del modulo api_keys.py
key = twelvedata_api_key
header = bcra_header

# Elijo los tickers de los cuales quiero trear información
tickers = ["DJI", "SPX", "NDX"]

# Creo una listo con los valores de los indices de USA con la función
# get_index_value() del modulo extract.py
usa_values = []
for ticker in tickers:
    usa_indexes = get_index_value(key, ticker)
    usa_values.append(
        {
            "date":usa_indexes["values"][0]["datetime"],
            "ticker":usa_indexes["meta"]["symbol"],
            "currency":usa_indexes["meta"]["currency"],
            "value":usa_indexes["values"][0]["close"]
        }
    )

# Creo una listo con el valor del Merval con la función
# get_merval_value() del modulo extract.py
merval = get_merval_value(header)
merval_value = [
    {
        "date":merval["d"],
        "ticker":"MERV",
        "currency":"USD",
        "value":merval["v"]
    }
]

# Uno las dos listas y creo un dataframe
all_values = usa_values + merval_value

df_indexes = pd.DataFrame(all_values)

print(df_indexes)

