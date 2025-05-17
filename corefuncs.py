import urllib.request
import os
from aqt import mw
from aqt.qt import QAction, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

def create_blank_window(title):
    dlg = QDialog(mw)
    dlg.setWindowTitle(title)
    layout = QVBoxLayout()
    layout.addWidget(QLabel("This is a blank window for '{}'.".format(title)))
    dlg.setLayout(layout)
    dlg.exec()

def on_edit_ui():
    create_blank_window("Edit UI")

def on_info():
    create_blank_window("Info")

def set_wallpaper():
    # Prompt user for image URL
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
            # Download the image
            filename = os.path.join(mw.pm.profileFolder(), "wallpaper.jpg")
            urllib.request.urlretrieve(url, filename)
            # Apply as background
            mw.web.page().mainFrame().runJavaScript(f"""
                document.body.style.backgroundImage = 'url("file:///{filename}")';
                document.body.style.backgroundSize = 'cover';
                document.body.style.backgroundRepeat = 'no-repeat';
                document.body.style.backgroundPosition = 'center center';
            """)
            QMessageBox.information(dlg, "Success", "Wallpaper set successfully.")
        except Exception as e:
            QMessageBox.critical(dlg, "Error", str(e))
        dlg.accept()

    def on_cancel():
        dlg.reject()

    btn_ok.clicked.connect(on_ok)
    btn_cancel.clicked.connect(on_cancel)

    dlg.exec()

def add_ui_settings():
    menu = mw.menuBar().addMenu("UI-settings")
    edit_ui_action = QAction("Edit UI", mw)
    edit_ui_action.triggered.connect(on_edit_ui)
    info_action = QAction("Info", mw)
    info_action.triggered.connect(on_info)

    # Create a submenu for Wallpaper options
    wallpaper_menu = menu.addMenu("Wallpaper")
    set_bg_action = QAction("Set Wallpaper from Web", mw)
    set_bg_action.triggered.connect(set_wallpaper)

    menu.addAction(edit_ui_action)
    menu.addAction(info_action)
    menu.addMenu(wallpaper_menu)
    wallpaper_menu.addAction(set_bg_action)

