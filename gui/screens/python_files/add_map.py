from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from gui.config import config
import db_logic


Builder.load_file(str(config["kv_files_folder"]) + '/add_map.kv')


class AddMap(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
