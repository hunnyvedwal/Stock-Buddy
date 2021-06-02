# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si
from yahoo_fin import news
from tkinter import ttk, Canvas
from datetime import date

import datetime as dt

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

today = date.today()


def get_tick(name, frame, root):
    if name == "Apple":
        tick = "AAPL"
        stock_info(tick, frame, root)
    elif name == "Amazon":
        tick = "AMZN"
        stock_info(tick, frame, root)
    elif name == "Microsoft":
        tick = 'MSFT'
        stock_info(tick, frame, root)
    elif name == "Facebook":
        tick = 'FB'
        stock_info(tick, frame, root)
    elif name == "Google":
        tick = 'GOOGL'
        stock_info(tick, frame, root)


def stock_info(tick, frame, root):
    # ttk.Label(frame, text="Date: " + str(today)).place(x=0, y=0)
    # get live price
    live_price = si.get_live_price(tick)
    label_stock = ttk.Label(frame, text="Current Value: $", font='Arial')
    label_stock.place(x=0, y=10)

    # Entry box for Current value
    entry = ttk.Entry(frame)
    entry.place(x=115, y=5)
    entry.insert(0, live_price)
    entry.config(state='readonly')

    ttk.Label(frame, text=tick)

    ttk.Separator(frame).place(x=0, y=45, relwidth=1)

    # canvas = Canvas(frame)
    # canvas.pack()
    # canvas.create_line(60,160,280,90)

    quote_data = si.get_quote_table(tick)
    open = quote_data["Open"]
    wr = quote_data["52 Week Range"]
    av = quote_data['Avg. Volume']
    pe = quote_data['PE Ratio (TTM)']
    pc = quote_data['Previous Close']
    vol = quote_data['Volume']
    dr = quote_data["Day's Range"]

    ttk.Label(frame, text="Open: " + str(open)).place(x=0, y=50)
    ttk.Label(frame, text="Day's Range: " + str(dr)).place(x=0, y=70)
    ttk.Label(frame, text="52 Week Range: " + str(wr)).place(x=0, y=90)
    ttk.Label(frame, text="Avg. Volume: " + str(av)).place(x=250, y=50)
    ttk.Label(frame, text="PE Ratio: " + str(pe)).place(x=250, y=70)
    ttk.Label(frame, text="Previous Close: " + str(pc)).place(x=250, y=90)
    # ttk.Label(frame, text="Volume: " + str(vol)).place(x=0, y=110)

    # start = dt.datetime(2020, 1, 1)
    # end = dt.datetime.now()
    # data = si.get_data(tick, start_date=start, end_date=end, index_as_date=True, interval='1mo')
    # fig = Figure(figsize=(8, 2))
    # a = fig.add_subplot(111)
    # a.plot(data['adjclose'])
    # canvas = FigureCanvasTkAgg(fig, master=root)
    # canvas.get_tk_widget().place(x=-40, y=300)
    ##canvas.draw()

# data = si.get_data('AAPL', start_date=None, end_date=None, index_as_date=True, interval='1mo')
# print(data['adjclose'])
#quote_data = si.get_quote_table('Doge-usd')
#print(quote_data)
