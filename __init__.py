from .initialise_ui_components.init_ui import *
from aqt import mw
import time

menu = mw.menuBar().addMenu("UI-settings")

def main():
    gui_hooks.webview_will_set_content.append(inject_css)
    initui(menu)
    # while True: 
    #     time.sleep(100)
    #     aqt.mw.addonManager.loadAddons()

main()