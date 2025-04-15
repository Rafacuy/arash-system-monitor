# UI/widgets.py

import tkinter as tk
from tkinter import ttk
from itertools import cycle
from datetime import datetime, timedelta

from appconfig import configure_styles
from Utils.clock import update_clock
from Update.updater import setup_initial_data, update_metrics
from Utils.chart_utils import create_chart
from Utils.misc import update_data_array


class ArashApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Arash System Monitor")
        self.geometry("1200x800")
        self.configure(bg='#1a1a1a')

        # Style setup
        self.style = ttk.Style()
        self.style.theme_use('clam')
        configure_styles(self.style)

        # Settings
        self.update_interval = 1000
        self.colors = cycle(['#2afc98', '#fc2aab', '#2a6ffc'])
        self.data_points = 60

        # Data
        self.timestamps, self.cpu_data, self.mem_data, self.disk_data, self.net_data = setup_initial_data(self.data_points)

        # Widgets
        self.create_widgets()

        # Start clocks and data updates
        update_clock(self.clock_label, self)
        update_metrics(self)


    def create_widgets(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 20))

        self.clock_label = ttk.Label(
            header_frame,
            text="00:00:00",
            font=('Segoe UI', 24, 'bold'),
            foreground='#2afc98'
        )
        self.clock_label.pack(side=tk.RIGHT)

        ttk.Label(
            header_frame,
            text="Arash System Monitor",
            font=('Segoe UI', 24, 'bold'),
            foreground='#fc2aab'
        ).pack(side=tk.LEFT)

        self.create_dashboard(main_frame)

    def create_dashboard(self, parent):
        metrics_frame = ttk.Frame(parent)
        metrics_frame.pack(fill=tk.BOTH, expand=True)

        self.cpu_chart, self.cpu_ax, self.cpu_line = create_chart(metrics_frame, "CPU Usage (%)", next(self.colors))
        self.cpu_chart.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        self.mem_chart, self.mem_ax, self.mem_line = create_chart(metrics_frame, "Memory Usage (%)", next(self.colors))
        self.mem_chart.get_tk_widget().grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        self.disk_chart, self.disk_ax, self.disk_line = create_chart(metrics_frame, "Disk Usage (%)", next(self.colors))
        self.disk_chart.get_tk_widget().grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        self.net_chart, self.net_ax, self.net_line = create_chart(metrics_frame, "Network Usage (MB)", next(self.colors))
        self.net_chart.get_tk_widget().grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

        metrics_frame.grid_columnconfigure(0, weight=1)
        metrics_frame.grid_columnconfigure(1, weight=1)
        metrics_frame.grid_rowconfigure(0, weight=1)
        metrics_frame.grid_rowconfigure(1, weight=1)
