import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import math
stocks2 = ['AMD', 'MSFT','AAPL', 'ADBE','NVDA', 'SNE','CPRX', 'COST', 'WDC']
fig = make_subplots(rows=len(stocks2), cols=2)

num_rows = math.ceil((len(stocks2))/2)

variable = 1
for values in range(0, len(stocks2)):
    data = yf.download(tickers=stocks2[values], period='1d', interval='1m')
    values2 = values+1
    fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'],
                             name =stocks2[values]), row=values2, col=variable)
    fig.update_xaxes(rangeslider_visible=False, rangeselector=dict( buttons=list([dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"), dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=3, label="3h", step="hour", stepmode="backward"), dict(step="all")])))
    fig.update_xaxes(title_text=stocks2[values], row=values2, col=variable)
    if variable == 1:
        variable = 2
    else:
        variable = 1

fig.show()