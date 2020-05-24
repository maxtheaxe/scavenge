# scavenge! app (main.py) for backyard-hacks-2020 by max
# handle stuff in other folder
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '../backend'))
from ScavengerHunt import ScavengerHunt
# normal imports
from kivy.app import App
from kivy.lang import Builder # remove later
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ObjectProperty, BooleanProperty

global hunt

# create helper widgets
class ImageButton(ButtonBehavior, Image):
	'''image that can also be clicked like a button, with iname property as well'''
	# ref: https://stackoverflow.com/a/33489264
class NamedImageButton(ImageButton):
	'''image that can also be clicked like a button, with iname property as well'''
	def __init__(self, iname, **kwargs):
		super(ImageButton, self).__init__(**kwargs)
		self.iname = iname
# create different screens
class StartScreen(Screen):
	pass
class ZipScreen(Screen):
	def setup_hunt(self, zip_code):
		'''creates scavenger hunt obj with zip and stores it in self.hunt field'''
		global hunt
		hunt = ScavengerHunt(location = zip_code)
	def load_hunt(self, zip_code):
		'''switches to loading screen, then grabs data, and switches away'''
		# self.parent.current = 'loading' # won't show first for some reason
		self.setup_hunt(zip_code)
		self.parent.current = 'hunt'
	pass
class LoadingScreen(Screen):
	pass
class GPSLoadingScreen(LoadingScreen):
	pass
class HuntScreen(Screen):
	def __init__(self, target_list_checkboxes = [], **kwargs):
		super(Screen, self).__init__(**kwargs)
		self.target_list_checkboxes = target_list_checkboxes
	def populate_list(self):
		global hunt
		# grab box that contains targets
		target_list = self.ids['huntlist_display']
		# store checkboxes for easy access later
		self.target_list_checkboxes = []
		# clear any kids that were there before from prev calls
		target_list.clear_widgets()
		# loop over hunt targets to repopulate from hunt
		for i in range(hunt.get_hunt_length()):
			current_item = hunt.get_hunt_item(i) # store curr hunt item for easier access
			# create box to hold all items for this row (and all components of it)
			target_box = BoxLayout(size_hint = (1,0.2),
								   orientation = 'horizontal')
			target_image = NamedImageButton(source = current_item.get_picture(),
									   size_hint = (0.2, 0.9),
									   iname = current_item.get_name())
			# # bind on_press behavior to zoom in on image
			# target_image.bind(
			# 	on_press = lambda x:self.update_storage(current_item.get_picture(),
			# 											current_item.get_name(),
			# 											target_list_checkboxes))
			# bind on_press behavior to zoom in on image
			target_image.bind(
				on_press = self.image_pressed)
			target_box.add_widget(target_image) # add to target box for this item
			target_name = Label(text = current_item.get_name(),
								size_hint = (0.6, 1))
			target_box.add_widget(target_name) # add to target box for this item
			target_checkbox = CheckBox(active = current_item.get_found(),
									   size_hint = (0.2, 1))
			# store in list for later updating vars
			self.target_list_checkboxes.append(target_checkbox)
			# bind on_active behavior for checkbox
			target_checkbox.bind(on_active = lambda x:self.flip_checkbox(target_checkbox, current_item))
			target_box.add_widget(target_checkbox) # add to target box for this item
			target_list.add_widget(target_box) # add the box with all components to the storage area
	def end_pressed(self):
		'''handles calling the end screen with relevant information'''
		# update found statuses in actual checkbox object, using checkbox gui status
		self.update_checkboxes(self.target_list_checkboxes)
		# count num checked in finished list
		total_found = 0 # go away, I'm sure there are better ways
		for i in range(len(self.target_list_checkboxes)):
			if self.target_list_checkboxes[i].active == True: # if the checkbox is checked
				total_found += 1 # then add one to total
		# get total possible
		total_possible = len(self.target_list_checkboxes)
		self.manager.screens[5].set_score(total_found, total_possible)
		self.manager.current = 'end'
		return
	def image_pressed(self, box):
		'''updates checkbox storage and image to be zoomed on press'''
		# ref: https://stackoverflow.com/a/47592040
		self.update_storage(box.source, box.iname, self.target_list_checkboxes)
		return
	def update_storage(self, image, name, target_list_checkboxes):
		'''updates checkboxes and image to be zoomed'''
		# update found statuses in actual checkbox object, using checkbox gui status
		self.update_checkboxes(target_list_checkboxes)
		# update zoom image screen
		self.zoom_image(image, name)
		return
	def zoom_image(self, image, name):
		'''opens image screen with given image'''
		# now open image screen with given image
		self.manager.screens[4].populate_image(image, name)
		self.manager.current = 'image'
	def update_checkboxes(self, target_list_checkboxes):
		'''updates actual found status from checkboxes since automatic isn't working'''
		global hunt
		for i in range(len(target_list_checkboxes)):
			# update each item in list if it's checked (ik this is dumb)
			hunt.get_hunt_item(i).set_found(target_list_checkboxes[i].active) 
		return
	def flip_checkbox(self, target_checkbox, current_item):
		# print("this item: ", current_item.get_name())
		# print("this item status: ", current_item.get_found())
		current_item.set_found(target_checkbox.active)
		print("this item status: ", current_item.get_found())
		return
	pass
class ImageScreen(ButtonBehavior, Screen):
	# ref: https://stackoverflow.com/a/48721527
	def populate_image(self, image, name):
		self.ids['zoomed_image'].source = image
		self.ids['zoomed_image_name'].text = name
	pass
class EndScreen(Screen):
	def set_score(self, found, possible):
		'''fills in final score on end screen'''
		self.ids['stats_display'].text = "Score: {}/{}".format(found, possible)
	pass

# create screen manager
class ScreenManagement(ScreenManager):
	# ref: https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html
	# ref: https://stackoverflow.com/a/38110500
	pass
# run app
class ScavengeApp(App):
	def build(self):
		return ScreenManagement()

if __name__ == '__main__':
	app = ScavengeApp()
	app.run()