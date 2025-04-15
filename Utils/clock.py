# Update/clock.py

from datetime import datetime
import pytz

def update_clock(label, root):
    jakarta_tz = pytz.timezone('Asia/Jakarta')
    current_time = datetime.now(jakarta_tz).strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, lambda: update_clock(label, root))
