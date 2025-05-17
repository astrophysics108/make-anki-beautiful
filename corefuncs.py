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