from kivy.app import App
#kivy.require('1.9.1')
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from os.path import join, isdir


Builder.load_string("""
<MyWidget>:
    FileChooserListView:
        filters: [root.is_dir]
""")


    

class Widgets(Widget):
 	def addFile(self,number,file):
 		 numberFile=int(number.text)
 		 name=file.text
 		 print(numberFile)
 		 print(name)
 		 pass

 	def is_dir(self, directory, filename):
        return isdir(join(directory, filename))


 	def addWeeks(self):
 		self.ids.week1.disabled=False
 		self.ids.week2.disabled=False

 	def deleteWeeks(self):
 		self.ids.week1.disabled=True
 		self.ids.week2.disabled=True



class TestApp(App):
	def build(self):
		return Widgets()


 
if __name__ == '__main__':
    TestApp().run()