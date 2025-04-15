# Utils/chart_utils.py

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates

def create_chart(parent, title, color):
    fig, ax = plt.subplots(figsize=(6, 3))
    fig.patch.set_facecolor('#2a2a2a')
    ax.set_facecolor('#2a2a2a')
    ax.set_title(title, color='white', fontsize=10)
    ax.tick_params(colors='white', which='both')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax.grid(color='#3a3a3a', linestyle='--')

    line, = ax.plot([], [], color=color, linewidth=2)
    fig.autofmt_xdate()

    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    return canvas, ax, line

def update_chart(canvas, ax, line, timestamps, data, y_max):
    line.set_xdata(timestamps)
    line.set_ydata(data)
    ax.relim()
    ax.autoscale_view()
    ax.set_ylim(0, y_max * 1.1 if y_max != 0 else 100)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    canvas.draw()
