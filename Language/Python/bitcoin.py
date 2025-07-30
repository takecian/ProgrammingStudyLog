import requests
import datetime
import matplotlib.pyplot as plt

def fetch_btc_price_from_coingecko(start_date, end_date):
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range"
    params = {
        "vs_currency": "usd",
        "from": start_date.timestamp(),
        "to": end_date.timestamp()
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    # タイムスタンプと価格を取得
    print(data)
    prices = [(datetime.datetime.utcfromtimestamp(p[0] / 1000), p[1]) for p in data["prices"]]
    return prices

# 半減期ごとの開始日と終了日（1000日後まで）
halving_dates = [
    datetime.datetime(2012, 11, 28),
    datetime.datetime(2016, 7, 9),
    datetime.datetime(2020, 5, 11),
    datetime.datetime(2024, 4, 20),
]

end_dates = [d + datetime.timedelta(days=1000) for d in halving_dates]

# 各半減期後の価格データを取得
price_trends = {}
for i, halving_date in enumerate(halving_dates[:-1]):  # 直近の2024年はデータが不完全なため取得しない
    prices = fetch_btc_price_from_coingecko(halving_date, end_dates[i])
    days_since_halving = [(p[0] - halving_date).days for p in prices]
    price_trends[str(halving_date.year)] = (days_since_halving, [p[1] for p in prices])

# チャートの描画
plt.figure(figsize=(10, 6))

for year, (days, prices) in price_trends.items():
    plt.plot(days, prices, label=f"Halving {year}")

plt.axvline(x=0, color="black", linestyle="--", label="Halving Day")
plt.yscale("log")  # 対数スケールで表示
plt.xlabel("Days Since Halving")
plt.ylabel("Bitcoin Price (log scale)")
plt.title("Bitcoin Price Trends After Each Halving")
plt.legend()
plt.grid()

plt.show()
