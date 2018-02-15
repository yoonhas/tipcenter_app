import kivy

kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton


class PSS(BoxLayout):
    print("hi")
    username = ObjectProperty()
    password = ObjectProperty()
    print("hello")
    def submit_login(self):
        pass


class Main(App):
    def build(self):
        return PSS()

start = Main()
start.run()