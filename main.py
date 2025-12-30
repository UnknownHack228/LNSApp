from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class LNSApp(App):
    def build(self):
       layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
       layout.add_widget(Label(text='🎵 LNS Music Controller', font_size=28))
       layout.add_widget(Button(text='🔍 Scan Bluetooth', size_hint=(1, 0.2)))
       layout.add_widget(Button(text='▶️ Play Music', size_hint=(1, 0.2)))
       layout.add_widget(Button(text='🎤 Microphone to Speaker', size_hint=(1, 0.2)))
       layout.add_widget(Button(text='⚙️ Settings', size_hint=(1, 0.2)))
       return layout

if name == 'main':
    LNSApp().run()
