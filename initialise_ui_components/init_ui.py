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
def newactionbasic(name, text, menu, func=basicText):
    newaction =  QAction(name, mw)
    connectbasic = lambda func: func(name, text)
    newaction.triggered.connect(connectbasic(func))
    menu.addAction(newaction)

def wallpaper():
    # This function can be used to set a wallpaper or background image
    # For now, it does nothing but can be expanded later
    pass

# add tools
def addUi(menu):
    actions = {
        "Test" : "test",
        "Info" : "Addon to make anki beautiful",
        "Wallpaper" : "Set a wallpaper or background image"
    }
    for name in actions.keys():
        text = actions[name]
        newactionbasic(name, text, menu)

#init
def initui(menu):
    addUi(menu)