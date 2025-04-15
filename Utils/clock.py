# Update/clock.py

from datetime import datetime
import pytz

def update_clock(label, root):
    current_time = datetime.now().strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, lambda: update_clock(label, root))
