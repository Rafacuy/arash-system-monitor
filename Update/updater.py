# Update/updater.py

import psutil
from datetime import datetime, timedelta

from Utils.chart_utils import update_chart
from Utils.misc import update_data_array

def setup_initial_data(data_points):
    now = datetime.now()
    timestamps = [now - timedelta(seconds=i) for i in reversed(range(data_points))]
    cpu_data = [0] * data_points
    mem_data = [0] * data_points
    disk_data = [0] * data_points
    net_data = [0] * data_points
    return timestamps, cpu_data, mem_data, disk_data, net_data


def update_metrics(app):
    app.timestamps.append(datetime.now())
    if len(app.timestamps) > app.data_points:
        app.timestamps.pop(0)

    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    net = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    net_mb = round(net / (1024 ** 2), 2)

    update_data_array(app.cpu_data, cpu, app.data_points)
    update_data_array(app.mem_data, mem, app.data_points)
    update_data_array(app.disk_data, disk, app.data_points)
    update_data_array(app.net_data, net_mb, app.data_points)

    update_chart(app.cpu_chart, app.cpu_ax, app.cpu_line, app.timestamps, app.cpu_data, 100)
    update_chart(app.mem_chart, app.mem_ax, app.mem_line, app.timestamps, app.mem_data, 100)
    update_chart(app.disk_chart, app.disk_ax, app.disk_line, app.timestamps, app.disk_data, 100)
    update_chart(app.net_chart, app.net_ax, app.net_line, app.timestamps, app.net_data,
                 max(app.net_data) if app.net_data else 100)

    app.after(app.update_interval, lambda: update_metrics(app))
