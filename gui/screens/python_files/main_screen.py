from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from gui.config import config


Builder.load_file(str(config["kv_files_folder"]) + '/main_screen.kv')


class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
