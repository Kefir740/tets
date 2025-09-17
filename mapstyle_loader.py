from gui.base import MainApp
from kivy.config import Config
from gui.config import config


def main():
    Config.set('kivy', 'keyboard_mode', 'systemanddock')
    Config.set('graphics', 'width', config['window_width'])
    Config.set('graphics', 'height', config['window_height'])
    Config.set('graphics', 'fullscreen', config['fullscreen'])


    try:
        win = MainApp()
    except Exception as e:
        print(e)
        return
    win.run()


if __name__ == '__main__':
    main()


