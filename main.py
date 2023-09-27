from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.widget import Widget


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('basic.kv')

    def logger(self):
        if self.root.ids.password_box.text == '123':
            self.root.ids.login_label.text = f'Sup, {self.root.ids.username_box.text}!'
        else:
            self.root.ids.login_label.text = f'WRONG PASSWORD!'


MainApp().run()
