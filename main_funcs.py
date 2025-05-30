from aqt import *
from aqt.qt import *


def basicText(title, words):
    dlg = QDialog(mw)
    dlg.setWindowTitle(title)
    layout = QVBoxLayout()
    layout.addWidget(QLabel(words))
    dlg.setLayout(layout)
    dlg.exec()

def addUi():
    menu = mw.menuBar().addMenu("UI-settings")
    edit_ui_action = QAction("Edit UI", mw)
    edit_ui_action.triggered.connect(lambda: basicText("Edit UI", "Editing UI is as such"))
    info_action = QAction("Info", mw)
    info_action.triggered.connect(lambda: basicText("Info", "This is an addon in development\n that will make the UI of anki\n not ugly anymore"))
    tutorial =  QAction("Tutorial", mw)
    info_action.triggered.connect(lambda: basicText("Tutorial", "How to use anki"))

    menu.addAction(edit_ui_action)
    menu.addAction(info_action)

def main():
    addUi()