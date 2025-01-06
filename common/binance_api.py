from binance.client import Client
import pandas as pd

# API-Schlüssel (falls nötig)
API_KEY = "dein_api_key"  # Ersetzen durch deinen API-Schlüssel
API_SECRET = "dein_api_secret"  # Ersetzen durch dein API-Secret

# Binance-Client initialisieren
client = Client(API_KEY, API_SECRET)

# Liste der Coins mit ihren Listungsdaten
coins = [
    {"symbol": "LUMIAUSDT", "listed_date": "2024-10-18 10:30"},
    {"symbol": "EIGENUSDT", "listed_date": "2024-09-30 10:19"},
    {"symbol": "THEUSDT", "listed_date": "2024-11-27 10:30"},
    {"symbol": "BONKUSDT", "listed_date": "2023-12-15 04:58"},
    {"symbol": "1000SATSUSDT", "listed_date": "2023-12-12 07:09"},
    {"symbol": "JTOUSDT", "listed_date": "2023-12-07 12:55"},
    {"symbol": "BLURUSDT", "listed_date": "2023-11-24 07:09"},
    {"symbol": "ORDIUSDT", "listed_date": "2023-11-07 07:44"},
    {"symbol": "NTRNUSDT", "listed_date": "2023-10-10 09:45"},
    {"symbol": "APTUSDT", "listed_date": "2022-10-18 03:04"},
    {"symbol": "OPUSDT", "listed_date": "2022-06-01 03:00"},
    {"symbol": "MOBUSDT", "listed_date": "2022-04-29 07:58"},
    {"symbol": "NEXOUSDT", "listed_date": "2022-04-29 07:58"},
    {"symbol": "APEUSDT", "listed_date": "2022-03-17 08:02"},
    {"symbol": "KDAUSDT", "listed_date": "2022-03-11 06:17"},
]

def get_daily_data(symbol, start_date):
    """
    Holt tägliche Kline-Daten (Candlestick-Daten) von Binance ab dem Listungsdatum.
    
    :param symbol: Das Symbol des Coins, z. B. 'BTCUSDT'.
    :param start_date: Startdatum (im Format '1 Jan, 2021').
    :return: Pandas DataFrame mit den Kline-Daten.
    """
    try:
        # Hole tägliche Klines
        klines = client.get_historical_klines(
            symbol=symbol,
            interval=Client.KLINE_INTERVAL_1DAY,
            start_str=start_date
        )
        
        # Umwandeln in ein DataFrame
        data = pd.DataFrame(klines, columns=[
            "Open time", "Open", "High", "Low", "Close", "Volume", 
            "Close time", "Quote asset volume", "Number of trades", 
            "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"
        ])
        
        # Zeitstempel konvertieren
        data["Open time"] = pd.to_datetime(data["Open time"], unit='ms')
        data["Close time"] = pd.to_datetime(data["Close time"], unit='ms')
        
        # Datensätze bereinigen (nur relevante Spalten behalten)
        data = data[["Open time", "Open", "High", "Low", "Close", "Volume"]]
        data.set_index("Open time", inplace=True)
        
        return data
    except Exception as e:
        print(f"Fehler beim Abrufen der Daten für {symbol}: {e}")
        return None

# Daten für alle Coins abrufen
for coin in coins:
    symbol = coin["symbol"]
    listed_date = coin["listed_date"]
    
    print(f"Hole Daten für {symbol}, Listungsdatum: {listed_date}")
    data = get_daily_data(symbol, listed_date)
    
    if data is not None:
        # Daten als CSV speichern
        filename = f"{symbol}_daily_data.csv"
        data.to_csv(filename)
        print(f"Daten für {symbol} gespeichert in {filename}")
