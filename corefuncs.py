from aqt import mw
from aqt.qt import QAction, QDialog, QVBoxLayout, QLabel


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

def add_edit_ui_option():
    action_menu = mw.menuBar().addMenu("UI-settings")
    edit_ui_action = QAction("Edit UI", mw)
    edit_ui_action.triggered.connect(on_edit_ui)
    info_action = QAction("Info", mw)
    info_action.triggered.connect(on_info)
    action_menu.addAction(edit_ui_action)
    action_menu.addAction(info_action)