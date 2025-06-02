from aqt import *
from aqt.qt import *
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
    # Path to store the selected wallpaper path
    config_dir = os.path.join(mw.pm.profileFolder(), "make_anki_beautiful")
    os.makedirs(config_dir, exist_ok=True)
    wallpaper_path_file = os.path.join(config_dir, "wallpaper_path.txt")

    # Check if a wallpaper has already been set
    if os.path.exists(wallpaper_path_file):
        with open(wallpaper_path_file, "r", encoding="utf-8") as f:
            wallpaper_path = f.read().strip()
        if os.path.exists(wallpaper_path):
            set_anki_wallpaper(wallpaper_path)
            basicText("Wallpaper", "Wallpaper already set.")
            return

    # Ask user to select an image file from Desktop
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    file_dialog = QFileDialog(mw)
    file_dialog.setDirectory(desktop)
    file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp *.gif)")
    if file_dialog.exec():
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            wallpaper_path = selected_files[0]
            # Save the selected path
            with open(wallpaper_path_file, "w", encoding="utf-8") as f:
                f.write(wallpaper_path)
            set_anki_wallpaper(wallpaper_path)
            basicText("Wallpaper", "Wallpaper set successfully.")
        else:
            basicText("Wallpaper", "No file selected.")
    else:
        basicText("Wallpaper", "No file selected.")

def set_anki_wallpaper(image_path):
    # Inject CSS to set the background image for Anki main window
    image_path_fixed = image_path.replace("\\", "/")
    css = f"""
    QMainWindow {{
        background-image: url("{image_path_fixed}");
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        background-size: cover;
    }}
    """
    mw.setStyleSheet(css)

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