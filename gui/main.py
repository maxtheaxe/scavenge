# scavenge! app (main.py) for backyard-hacks-2020 by max
from kivy.app import App
from kivy.lang import Builder # remove later
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# create different screens
class StartScreen(Screen):
	pass
class ZipScreen(Screen):
	pass
class LoadingScreen(Screen):
	pass
class GPSLoadingScreen(LoadingScreen):
	pass
class HuntScreen(Screen):
	pass
class EndScreen(Screen):
	pass
# create screen manager
# ref: https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html
# ref: https://stackoverflow.com/a/38110500
class ScreenManagement(ScreenManager):
	pass
# run app
class ScavengeApp(App):
	def build(self):
		return ScreenManagement()

if __name__ == '__main__':
	app = ScavengeApp()
	app.run()