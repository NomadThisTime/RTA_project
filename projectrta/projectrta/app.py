import flask
import base64
from io import BytesIO
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib
from flask import Flask, request, url_for, redirect, render_template
import pandas as pd
from matplotlib import pyplot as plt
from alpha_vantage.timeseries import TimeSeries
import numpy as np
matplotlib.use('Agg')


API_key = 'CP79H1GMVOB7F5NW' # your personal API key 
ts = TimeSeries(key = API_key, output_format = 'pandas')

app=Flask(__name__)

@app.route('/services')
def services():
        # Generate the figure **without using pyplot**.

    data = ts.get_intraday('MSFT',interval = '15min')
    market = data[0]
    market.columns = ['open', 'high', 'low', 'close', 'volume']
    market['1hr-interval'] = market['close'].rolling(4).mean()
    market['3hrs-interval'] = market['close'].rolling(12).mean()
    market['signal'] = np.where(market['1hr-interval'] > market['3hrs-interval'], 1, 0)
    market['signal'] = np.where(market['1hr-interval'] < market['3hrs-interval'], -1, market['signal'])
    market.dropna(inplace=True)
    market['return'] = np.log(market['close']).diff()
    market['system_return'] = market['signal'] * market['return']
    market['entry'] = market.signal.diff()
    plt.rcParams['figure.figsize'] = 6,4
    plt.grid(True, alpha = .3)
    plt.plot(market.iloc[-252:]['close'], label = 'price at close')
    plt.plot(market.iloc[-252:]['1hr-interval'], label = '1hr-interval')
    plt.plot(market.iloc[-252:]['3hrs-interval'], label = '3hrs-interval')
    plt.plot(market[-252:].loc[market.entry==2].index, market[-252:]['3hrs-interval'][market.entry==2], '^',
            color = 'g', markersize = 12)
    plt.plot(market[-252:].loc[market.entry==-2].index, market[-252:]['3hrs-interval'][market.entry==-2], 'v',
            color = 'r', markersize = 12)
    plt.legend(loc=1)
    plt.xticks(rotation=10)
  


    buf = BytesIO()
    plt.savefig(buf, format="png")
    # Embed the result in the html output.
    data1 = base64.b64encode(buf.getbuffer()).decode("ascii")
    plt.figure().clear()
    plt.close()
    plt.cla()
    plt.clf()

    buf.seek(0)
    buf.truncate(0)

    data = ts.get_intraday('GOOG',interval = '15min')
    market = data[0]
    market.columns = ['open', 'high', 'low', 'close', 'volume']
    market['1hr-interval'] = market['close'].rolling(4).mean()
    market['3hrs-interval'] = market['close'].rolling(12).mean()
    market['signal'] = np.where(market['1hr-interval'] > market['3hrs-interval'], 1, 0)
    market['signal'] = np.where(market['1hr-interval'] < market['3hrs-interval'], -1, market['signal'])
    market.dropna(inplace=True)
    market['return'] = np.log(market['close']).diff()
    market['system_return'] = market['signal'] * market['return']
    market['entry'] = market.signal.diff()
    plt.rcParams['figure.figsize'] = 6,4
    plt.grid(True, alpha = .3)
    plt.plot(market.iloc[-252:]['close'], label = 'price at close')
    plt.plot(market.iloc[-252:]['1hr-interval'], label = '1hr-interval')
    plt.plot(market.iloc[-252:]['3hrs-interval'], label = '3hrs-interval')
    plt.plot(market[-252:].loc[market.entry==2].index, market[-252:]['3hrs-interval'][market.entry==2], '^',
            color = 'g', markersize = 12)
    plt.plot(market[-252:].loc[market.entry==-2].index, market[-252:]['3hrs-interval'][market.entry==-2], 'v',
            color = 'r', markersize = 12)
    plt.legend(loc=1)
    plt.xticks(rotation=10)



    plt.savefig(buf, format="png")
    data2 = base64.b64encode(buf.getbuffer()).decode("ascii")
    plt.figure().clear()
    plt.close()
    plt.cla()
    plt.clf()

    buf.seek(0)
    buf.truncate(0)

    data = ts.get_intraday('AAPL',interval = '15min')
    market = data[0]
    market.columns = ['open', 'high', 'low', 'close', 'volume']
    market['1hr-interval'] = market['close'].rolling(4).mean()
    market['3hrs-interval'] = market['close'].rolling(12).mean()
    market['signal'] = np.where(market['1hr-interval'] > market['3hrs-interval'], 1, 0)
    market['signal'] = np.where(market['1hr-interval'] < market['3hrs-interval'], -1, market['signal'])
    market.dropna(inplace=True)
    market['return'] = np.log(market['close']).diff()
    market['system_return'] = market['signal'] * market['return']
    market['entry'] = market.signal.diff()
    plt.rcParams['figure.figsize'] = 6,4
    plt.grid(True, alpha = .3)
    plt.plot(market.iloc[-252:]['close'], label = 'price at close')
    plt.plot(market.iloc[-252:]['1hr-interval'], label = '1hr-interval')
    plt.plot(market.iloc[-252:]['3hrs-interval'], label = '3hrs-interval')
    plt.plot(market[-252:].loc[market.entry==2].index, market[-252:]['3hrs-interval'][market.entry==2], '^',
            color = 'g', markersize = 12)
    plt.plot(market[-252:].loc[market.entry==-2].index, market[-252:]['3hrs-interval'][market.entry==-2], 'v',
            color = 'r', markersize = 12)
    plt.legend(loc=1)
    plt.xticks(rotation=10)


    plt.savefig(buf, format="png")
    data3 = base64.b64encode(buf.getbuffer()).decode("ascii")
    plt.figure().clear()
    plt.close()
    plt.cla()
    plt.clf()

    buf.seek(0)
    buf.truncate(0)



    data = ts.get_intraday('AMZN',interval = '15min')
    market = data[0]
    market.columns = ['open', 'high', 'low', 'close', 'volume']
    market['1hr-interval'] = market['close'].rolling(4).mean()
    market['3hrs-interval'] = market['close'].rolling(12).mean()
    market['signal'] = np.where(market['1hr-interval'] > market['3hrs-interval'], 1, 0)
    market['signal'] = np.where(market['1hr-interval'] < market['3hrs-interval'], -1, market['signal'])
    market.dropna(inplace=True)
    market['return'] = np.log(market['close']).diff()
    market['system_return'] = market['signal'] * market['return']
    market['entry'] = market.signal.diff()
    plt.rcParams['figure.figsize'] = 6,4
    plt.grid(True, alpha = .3)
    plt.plot(market.iloc[-252:]['close'], label = 'price at close')
    plt.plot(market.iloc[-252:]['1hr-interval'], label = '1hr-interval')
    plt.plot(market.iloc[-252:]['3hrs-interval'], label = '3hrs-interval')
    plt.plot(market[-252:].loc[market.entry==2].index, market[-252:]['3hrs-interval'][market.entry==2], '^',
            color = 'g', markersize = 12)
    plt.plot(market[-252:].loc[market.entry==-2].index, market[-252:]['3hrs-interval'][market.entry==-2], 'v',
            color = 'r', markersize = 12)
    plt.legend(loc=1)
    plt.xticks(rotation=10)
  


    plt.savefig(buf, format="png")
    data4 = base64.b64encode(buf.getbuffer()).decode("ascii")
    plt.figure().clear()
    plt.close()
    plt.cla()
    plt.clf()

    buf.seek(0)
    buf.truncate(0)

    return render_template('services.html', plot_url = data1, plot_url2 = data2, plot_url3 = data3, plot_url4 = data4)


@app.route('/')
def home():
    # Generate the figure **without using pyplot**.

    tuple = ts.get_intraday('MSFT',interval = '15min')
    data = tuple[0]
    data.columns = ['open', 'high', 'low', 'close', 'volume']
    plt.figure(figsize=(6,4))
    plt.plot(data['high'].iloc[-200:], 'g--', label="high")
    plt.plot(data['open'].iloc[-200:], 'r--', label="open")
    plt.plot(data['low'].iloc[-200:], 'y--', label="low")
    plt.plot(data['close'].iloc[-200:], label="close")
    plt.xticks(rotation=10)
    plt.legend()


    buf = BytesIO()
    plt.savefig(buf, format="png")
    # Embed the result in the html output.
    data1 = base64.b64encode(buf.getbuffer()).decode("ascii")
    plt.figure().clear()
    plt.close()
    plt.cla()
    plt.clf()

    buf.seek(0)
    buf.truncate(0)

    tuple = ts.get_intraday('GOOG',interval = '15min')
    data = tuple[0]
    data.columns = ['open', 'high', 'low', 'close', 'volume']
    plt.figure(figsize=(6,4))
    plt.plot(data['high'].iloc[-200:], 'g--', label="high")
    plt.plot(data['open'].iloc[-200:], 'r--', label="open")
    plt.plot(data['low'].iloc[-200:], 'y--', label="low")
    plt.plot(data['close'].iloc[-200:], label="close")
    plt.xticks(rotation=10)
    plt.legend()


    plt.savefig(buf, format="png")
    data2 = base64.b64encode(buf.getbuffer()).decode("ascii")
    plt.figure().clear()
    plt.close()
    plt.cla()
    plt.clf()

    buf.seek(0)
    buf.truncate(0)

    tuple = ts.get_intraday('FB',interval = '15min')
    data = tuple[0]
    data.columns = ['open', 'high', 'low', 'close', 'volume']
    plt.figure(figsize=(6,4))
    plt.plot(data['high'].iloc[-200:], 'g--', label="high")
    plt.plot(data['open'].iloc[-200:], 'r--', label="open")
    plt.plot(data['low'].iloc[-200:], 'y--', label="low")
    plt.plot(data['close'].iloc[-200:], label="close")
    plt.xticks(rotation=10)
    plt.legend()


    plt.savefig(buf, format="png")
    data3 = base64.b64encode(buf.getbuffer()).decode("ascii")
    plt.figure().clear()
    plt.close()
    plt.cla()
    plt.clf()

    buf.seek(0)
    buf.truncate(0)



    tuple = ts.get_intraday('AMZN',interval = '15min')
    data = tuple[0]
    data.columns = ['open', 'high', 'low', 'close', 'volume']
    plt.figure(figsize=(6,4))
    plt.plot(data['high'].iloc[-200:], 'g--', label="high")
    plt.plot(data['open'].iloc[-200:], 'r--', label="open")
    plt.plot(data['low'].iloc[-200:], 'y--', label="low")
    plt.plot(data['close'].iloc[-200:], label="close")
    plt.xticks(rotation=10)
    plt.legend()


    plt.savefig(buf, format="png")
    data4 = base64.b64encode(buf.getbuffer()).decode("ascii")
    plt.figure().clear()
    plt.close()
    plt.cla()
    plt.clf()

    buf.seek(0)
    buf.truncate(0)

    return render_template('home.html', plot_url = data1, plot_url2 = data2, plot_url3 = data3, plot_url4 = data4)


if __name__=="__main__":
     app.run(port=5000,host='0.0.0.0')

