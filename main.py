# Main.py
    
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from UI.widgets import ArashApp
from tkinter import messagebox

if __name__ == "__main__":
    try:
        app = ArashApp()
        app.mainloop()
    except Exception as e:
        messagebox.showerror("Critical Error", f"Application failed to start:\n{str(e)}")
