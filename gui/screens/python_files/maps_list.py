from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from gui.config import config
import db_logic


Builder.load_file(str(config["kv_files_folder"]) + '/maps_list.kv')


class MapsList(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.data = None
        self.table = self.ids['table']

    def on_pre_enter(self, *args):
        pass

    def load_data(self):
        db_data = db_logic.get_maps_list()
        self.table.data = [{'text': f'{row[0]} | {row[1]}'} for row in db_data]

