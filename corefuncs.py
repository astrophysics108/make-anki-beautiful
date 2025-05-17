import os
import json
import urllib.request
from aqt import mw
from aqt.qt import QAction, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from aqt import gui_hooks

# ----------- Configuration ----------- #
CONFIG_FILENAME = "wallpaper_config.json"

# ----------- Load and Save Path ----------- #
def get_config_path():
    profile_folder = mw.pm.profileFolder()
    return os.path.join(profile_folder, CONFIG_FILENAME)

def save_wallpaper_path(path):
    try:
        with open(get_config_path(), "w") as f:
            json.dump({"wallpaper": path}, f)
    except Exception as e:
        print(f"Error saving wallpaper path: {e}")

def load_wallpaper_path():
    path = get_config_path()
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                data = json.load(f)
                return data.get("wallpaper")
        except Exception as e:
            print(f"Error loading wallpaper path: {e}")
    return None

# ----------- Function to Apply Wallpaper ----------- #
def apply_stored_wallpaper():
    path = load_wallpaper_path()
    if path and os.path.exists(path):
        # Convert path to URL format
        path = path.replace("\\", "/")
        js_code = f"""
        var style = document.getElementById('custom-background-style');
        if (!style) {{
            style = document.createElement('style');
            style.type = 'text/css';
            style.id = 'custom-background-style';
            document.head.appendChild(style);
        }}
        style.innerHTML = `
        body {{
            background-image: url("file:///{path}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center center;
        }}`;
        """
        mw.web.eval(js_code)
    else:
        # Remove style if no wallpaper
        js_remove = """
        var style = document.getElementById('custom-background-style');
        if (style) style.remove();
        """
        mw.web.eval(js_remove)

# ----------- UI for setting wallpaper ----------- #
def set_wallpaper():
    dlg = QDialog(mw)
    dlg.setWindowTitle("Set Wallpaper from URL")
    layout = QVBoxLayout()

    label = QLabel("Enter Image URL:")
    url_edit = QLineEdit()
    btn_ok = QPushButton("Set Wallpaper")
    btn_cancel = QPushButton("Cancel")

    layout.addWidget(label)
    layout.addWidget(url_edit)
    layout.addWidget(btn_ok)
    layout.addWidget(btn_cancel)
    dlg.setLayout(layout)

    def on_ok():
        url = url_edit.text().strip()
        if not url:
            QMessageBox.warning(dlg, "Error", "Please enter a URL.")
            return
        try:
            filename = os.path.join(mw.pm.profileFolder(), "wallpaper.jpg")
            urllib.request.urlretrieve(url, filename)
            save_wallpaper_path(filename)
            apply_stored_wallpaper()
            QMessageBox.information(dlg, "Success", "Wallpaper set successfully.")
            dlg.accept()
        except Exception as e:
            QMessageBox.critical(dlg, "Error", str(e))

    btn_ok.clicked.connect(on_ok)
    btn_cancel.clicked.connect(dlg.reject)

    dlg.exec()

# ----------- Add Settings Menu ----------- #
def add_ui_settings():
    menu = mw.menuBar().addMenu("UI-settings")
    # Main actions
    edit_ui_action = QAction("Edit UI", mw)
    edit_ui_action.triggered.connect(lambda: create_blank_window("Edit UI"))
    info_action = QAction("Info", mw)
    info_action.triggered.connect(lambda: create_blank_window("Info"))

    # Wallpaper submenu
    wallpaper_menu = menu.addMenu("Wallpaper")
    set_bg_action = QAction("Set Wallpaper from Web", mw)
    set_bg_action.triggered.connect(set_wallpaper)

    # Add actions to menu
    menu.addAction(edit_ui_action)
    menu.addAction(info_action)
    menu.addMenu(wallpaper_menu)
    wallpaper_menu.addAction(set_bg_action)

# ----------- Helper: Blank Window ----------- #
def create_blank_window(title):
    dlg = QDialog(mw)
    dlg.setWindowTitle(title)
    layout = QVBoxLayout()
    layout.addWidget(QLabel(f"This is a blank window for '{title}'."))
    dlg.setLayout(layout)
    dlg.exec()

# ----------- Initialize after main window ready ----------- #
def on_main_window_ready():
    add_ui_settings()
    # Load and apply wallpaper at startup
    apply_stored_wallpaper()

# ----------- Hook into main window init ----------- #

def main():
    gui_hooks.main_window_did_init.append(on_main_window_ready)