import requests

# Extraer indices de Twelve Data

def get_index_value(api_key, ticker):
    url = f"https://api.twelvedata.com/time_series?apikey={api_key}&interval=1day&symbol={ticker}&previous_close=true&type=index&outputsize=1"
    response = requests.get(url).json()
    return response


# Extraer indice MERVAL de la API del BCRA

def get_merval_value(header):
    response = requests.get("https://api.estadisticasbcra.com/merval_usd", headers=header).json()
    return response[-1]












