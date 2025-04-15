from tkinter import ttk

def configure_styles(self):
    self.style = ttk.Style()  

    style_settings = {
        "TFrame": {"configure": {"background": "#1a1a1a"}},
        "TLabel": {
            "configure": {
                "background": "#1a1a1a",
                "foreground": "#ffffff",
                "font": ('Segoe UI', 10)
            }
        },
        "TNotebook": {"configure": {"background": "#2a2a2a", "foreground": "white"}},
        "TNotebook.Tab": {
            "configure": {
                "padding": [10, 5],
                "background": "#2a2a2a",
                "foreground": "white"
            },
            "map": {
                "background": [("selected", "#3a3a3a")],
                "expand": [("selected", [1, 1, 1, 0])]
            }
        }
    }

    for style, settings in style_settings.items():
        if 'map' in settings:
            self.style.map(style, **settings['map'])
        self.style.configure(style, **settings.get('configure', {}))
