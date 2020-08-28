import datetime as DT
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# dates = mdates.date2num(list_of_datetimes)
# matplotlib.pyplot.plot_date(dates, values)


start = [DT.datetime(2000,1,1)+DT.timedelta(days=i) for i in (2,0,3)]
end = [s+DT.timedelta(days=i) for s,i in zip(start, [15,7,10])]
start = mdates.date2num(start)
end = mdates.date2num(end)
yval = [1,2,3]
width = end-start

fig, ax = plt.subplots()
ax.bar(x=yval,width=.3, bottom=start, height=width)
xfmt = mdates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(xfmt)
# autorotate the dates
fig.autofmt_xdate()
plt.show()