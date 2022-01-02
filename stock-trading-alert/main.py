import requests
import config


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
news_api_key = config.NEWS_API_KEY
alphavantage_api_key = config.ALPHA_API_KEY

newsapi_url = "https://newsapi.org/v2/everything"
alphavantage_url = "https://www.alphavantage.co/query"
newsapi_parameters = {
    "q": STOCK,
    "apiKey": news_api_key,
    "totalResults": 3,
}

alphavantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": alphavantage_api_key
}

response_news = requests.get(url=newsapi_url, params=newsapi_parameters)
response_news.raise_for_status()

data_news = response_news.json()

response_alpha = requests.get(url=alphavantage_url, params=alphavantage_parameters)
response_alpha.raise_for_status()
data_stock = response_alpha.json()['Time Series (Daily)']#['2021-12-31']['4. close']
date_stock = list(data_stock)

print(date_stock[:2])

# newlist = [expression for item in iterable if condition == True] list comprehension
close_day_list = [data_stock[days]['4. close'] for days in date_stock[:2]]
subtract_close = float(close_day_list[0]) - float(close_day_list[1])
print(close_day_list)
percent_close = round((subtract_close / float(close_day_list[0])) * 100, 2)
print(percent_close)

if 5 <= percent_close <= -5:

    get_news = (data_news['articles'][0]['url'])

    url_list = [data_news['articles'][x]['url'] for x in range(0, 3)]
    print(url_list)

else:
    print("Everything is normal")
