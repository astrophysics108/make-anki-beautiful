from .initialise_ui_components.init_ui import *
from aqt import mw

menu = mw.menuBar().addMenu("UI-settings")

def main():
    initui(menu)

main()