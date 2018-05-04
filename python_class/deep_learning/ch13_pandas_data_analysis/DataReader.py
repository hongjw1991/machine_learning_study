import pandas_datareader.data as web

import datetime

start = datetime.datetime(2016, 2, 10)
end = datetime.datetime(2018, 3, 1)

gs = web.DataReader("MSFT", "iex", start, end)

gs.info()

