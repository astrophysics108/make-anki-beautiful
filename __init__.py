from aqt import mw
from aqt.qt import QAction, QDialog, QVBoxLayout, QLabel
from .corefuncs import *

def main():
    action_menu = mw.menuBar().addMenu("UI-settings")
    edit_ui_action = QAction("Edit UI", mw)
    edit_ui_action.triggered.connect(on_edit_ui)
    info_action = QAction("Info", mw)
    info_action.triggered.connect(on_info)
    action_menu.addAction(edit_ui_action)
    action_menu.addAction(info_action)

main()