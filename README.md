Oke bro, ini dia versi bahasa Inggris-nya, lengkap dan clean buat langsung dipakai di `README.md`:

---

```markdown
# ArashTool

🛠️ **ArashTool** is a GUI-based system monitoring tool that provides real-time insights into your CPU, RAM, Disk, and Network usage. Designed for developers, power users, and anyone who wants to monitor their system performance with a sleek and responsive interface.

---

## 🚀 Features

- 📊 **Real-time Monitoring**: Displays live system stats including CPU, Memory, Disk, and Network usage.
- 🎨 **Custom UI Styling**: Modern dark-themed interface using advanced ttk styles.
- ⚙️ **Optimized Performance**: Efficient data updates using `psutil`.
- 🧩 **Modular Codebase**: Clean architecture with separated concerns for UI, logic, and utilities.
- 🖥️ **Built with**: `tkinter`, `psutil`, `matplotlib`, `ttk`

---

## 📂 Project Structure

```
ArashTool/
├── UI/
│   └── widgets.py          # Main UI component (ArashApp)
├── Utils/
│   ├── chart_utils.py      # Utilities for updating charts
|   ├── clock.py            # Utilities
│   └── misc.py             # Helper functions
├── Update/
│   └── updater.py          # Data fetching from system
├── app_config.py           # ttk style configuration
├── main.py                 # Entry point of the application
└── README.md               # You’re reading it!
```

---

## ⚙️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ArashTool.git
   cd ArashTool
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   python main.py
   ```

---

## 📦 Dependencies

- `psutil`
- `matplotlib`
- `tkinter` *(comes with Python)*
- `ttk` *(part of tkinter)*

> Recommended Python version: **3.8 or higher**

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute with proper attribution.

---

## 🤝 Contributions

Contributions, ideas, and pull requests are always welcome.  
Found a bug or have a cool feature in mind? Let’s build together!

---

## 👤 Author

Crafted with ❤️ by **[RafardhanCuy](https://github.com/Rafacuy)**  
If you find this tool useful, consider giving it a ⭐

---

