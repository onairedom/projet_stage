from kivy.app import App
#kivy.require('1.9.1')
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox



class Widgets(Widget):
 	def addFile(self):
 		print('aaaaaaaa')

 	def activateCheckbox(self):
 		print('bbbbbbbbb')
 		



class TestApp(App):
	def build(self):
		return Widgets()


 
if __name__ == '__main__':
    TestApp().run()