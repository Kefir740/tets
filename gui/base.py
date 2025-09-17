from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from gui.screens import *


Builder.load_file('gui/base.kv')


class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.sm = ScreenManager()

        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(MapsList(name='maps_list'))
        self.sm.add_widget(AddMap(name='add_map'))

    def build(self):
        return self.sm
