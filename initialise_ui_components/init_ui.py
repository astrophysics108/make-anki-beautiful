from aqt import *
from aqt.qt import *
from anki.utils import *
import os

# basic text window
def basicText(title, words):
    dlg = QDialog(mw)
    dlg.setWindowTitle(title)
    layout = QVBoxLayout()
    layout.addWidget(QLabel(words))
    dlg.setLayout(layout)
    dlg.exec()

# adds a new action that can call any function with optional arguments
def newactionbasic(name, text, menu, func=None, *args, **kwargs):
    newaction = QAction(name, mw)
    if func is None:
        func = basicText
        action = lambda: func(name, text)
    else:
        action = lambda: func(*args, **kwargs)
    newaction.triggered.connect(action)
    menu.addAction(newaction)

def wallpaper():
    config_dir = os.path.join(mw.pm.profileFolder(), "make_anki_beautiful")
    os.makedirs(config_dir, exist_ok=True)
    wallpaper_path_file = os.path.join(config_dir, "wallpaper_path.txt")

    if os.path.exists(wallpaper_path_file):
        with open(wallpaper_path_file, "r", encoding="utf-8") as f:
            wallpaper_path = f.read().strip()
        if os.path.exists(wallpaper_path):
            set_anki_wallpaper(wallpaper_path)
            basicText("Wallpaper", "Wallpaper already set.")
            return

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    file_dialog = QFileDialog(mw)
    file_dialog.setDirectory(desktop)
    file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp *.gif)")
    if file_dialog.exec():
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            wallpaper_path = selected_files[0]
            with open(wallpaper_path_file, "w", encoding="utf-8") as f:
                f.write(wallpaper_path)
            set_anki_wallpaper(wallpaper_path)
            basicText("Wallpaper", "Wallpaper set successfully.")
        else:
            basicText("Wallpaper", "No file selected.")
    else:
        basicText("Wallpaper", "No file selected.")

def set_anki_wallpaper(image_path=None):
    #image_path_fixed = image_path.replace("\\", "/")
    image_path_fixed = "https://science.nasa.gov/wp-content/uploads/2023/06/planets3x3-pluto-colormercury-axis-tilt-nolabels-1080p.00001-print.jpg"
    css = f"""
    body {{
        background-image: url("{image_path_fixed}") !important;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        background-size: cover;
        }}
    """
    return css


def inject_css(web_content, context):
    css = set_anki_wallpaper()
    if hasattr(context, "title") and "deck" in context.title:
        web_content.head += f"<style>{css}</style>"


# add tools
def addUi(menu):
    actions = {
        "Test" : "test",
        "Info" : "Addon to make anki beautiful",
    }
    for name in actions.keys():
        text = actions[name]
        newactionbasic(name, text, menu)
    newactionbasic("Wallpaper", "Set a wallpaper or background image", menu, func=wallpaper)

#init
def initui(menu):
    addUi(menu)
    