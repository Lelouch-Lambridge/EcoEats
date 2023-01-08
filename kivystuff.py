import kivy
kivy.require("2.1.0")
from kivy.app import App
#from kivy.uix.label import Label
#from kivy.uix.button import Button
#from kivy.uix.textinput import TextInput
#from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from googlesearch import search

Builder.load_file('kivycrap.kv')

#where google search function would go
def see(stuff):
 return ' '.join(stuff.split()[2:])

class MyLayout(Widget):
 def press(self):
  words = self.ids.txt_in.text
  #for once we get google search function running
  #[exec(f"self.ids.re{n}.text, self.ids.c{n}.text = tuplist[{n}]") for n in range(0,len(tuplist))]
  self.ids.re1.text = see(words)
  #print(self.ids.re1)
  #print(self.ids.re1)
  #self.ids.c1 = ' '.join(words.split()[2:])
  self.ids.txt_in.text = 'Enter word: '
  return words

class MyApp(App):
 def build(self):
  return MyLayout()

MyApp().run()
