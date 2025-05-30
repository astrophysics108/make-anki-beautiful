from aqt import *
from aqt.qt import *

# basic text window
def basicText(title, words):
    dlg = QDialog(mw)
    dlg.setWindowTitle(title)
    layout = QVBoxLayout()
    layout.addWidget(QLabel(words))
    dlg.setLayout(layout)
    dlg.exec()

# adds a new action that just makes a basic text window
def newactionbasic(name, text, menu):
    newaction =  QAction(name, mw)
    newaction.triggered.connect(lambda: basicText(name, text))
    menu.addAction(newaction)

# add tools
def addUi(menu):
    actions = {
        "Test" : "test",
        "Info" : "Addon to make anki beautiful"
    }
    for name in actions.keys():
        text = actions[name]
        newactionbasic(name, text, menu)

#init
def initui(menu):
    addUi(menu)