#!/usr/bin/env python

# import urllib2
import requests
import pytz
import pandas as pd
import io
from bs4 import BeautifulSoup
from datetime import datetime
# from pandas_datareader.data import DataReader
from dataplot.models import ChartData


SITE = "http://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
START = datetime(1900, 1, 1, 0, 0, 0, 0, pytz.utc)
END = datetime.today().utcnow()


def scrape_list(site):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    # req = urllib2.Request(site, headers=hdr)
    # page = urllib2.urlopen(req)

    response = requests.get(site, headers=hdr)
    page = response.text
    soup = BeautifulSoup(page)

    table = soup.find('table', {'class': 'wikitable sortable'})
    sector_tickers = dict()
    for row in table.findAll('tr'):
        col = row.findAll('td')
        if len(col) > 0:
            sector = str(col[3].string.strip()).lower().replace(' ', '_')
            ticker = str(col[0].string.strip())
            if sector not in sector_tickers:
                sector_tickers[sector] = list()
            sector_tickers[sector].append(ticker)
    return sector_tickers


def scrap_and_save_data(sector_tickers, start, end):
    for sector, tickers in sector_tickers.items():
        print('Downloading data from Yahoo for %s sector' % sector)
        for each_ticker in tickers:
            url = "http://chart.finance.yahoo.com/table.csv?s=" + \
                str(each_ticker) + \
                "&a=0&b=13&c=2017" + "&d=1&e=13&f=2017" + "&g=d&ignore=.csv"
            s = requests.get(url).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))
            for index, row in df.iterrows():
                cd = ChartData()
                cd.ticker = each_ticker
                cd.company_name = ""
                cd.sector = sector
                cd.date = row['Date']
                cd.open_value = row['Open']
                cd.close_value = row['Close']
                cd.high_value = row['High']
                cd.low_value = row['Low']
                cd.volume = row['Volume']
                cd.adj_close = row['Adj Close']
                cd.save()


def get_snp500():
    sector_tickers = scrape_list(SITE)
    scrap_and_save_data(sector_tickers, START, END)

if __name__ == '__main__':
    get_snp500()
