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

Builder.load_file('kivystuff.kv')

#where google search function would go
def see(stuff):
 #return ' '.join(stuff.split()[2:]), '0'
 
 try:
  from googlesearch import search
 except ImportError:
  print(" 'google' not found")
 prompt = str(' '.join(stuff.split()[2:]))
 query = prompt + ' recipe'

 url_list = []

 while len(url_list) < 2:
  for j in search(query, tld="com", num=1, stop=1, pause=0):
   if not ('youtube' in j or 'tiktok' in j or 'pintrest' in j or 'facebook' in j or '.gov' in j):
    url_list.append(j)
 url_list.pop()
 return url_list, '0'
 

class MyLayout(Widget):
 def press(self):
  words = self.ids.txt_in.text
  tuplist = see(words)
  #while len(tuplist) > 5: tuplist.pop()
  print(tuplist)
  
  self.ids.re0.text = tuplist[0][0]
  self.ids.c0.text = tuplist[1]

  #for n in range(len(tuplist)): exec(f"self.ids.re{n}.text, self.ids.c{n}.text = tuplist[{n}]") 
  self.ids.txt_in.text = 'Enter word: '
  return words

class MyApp(App):
 def build(self): return MyLayout()

MyApp().run()
