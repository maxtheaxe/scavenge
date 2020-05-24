# ScavengerHunt for backyard-hacks-2020 by max
import nwf_tools as nwft
from Checklist import Checklist

class ScavengerHunt(Checklist):
	'''scavenger hunt object, for use by user/player'''
	def __init__(self, huntlist = None, hunt_name = None, location = None):
		if (location == None): # if no location is provided (testing, maybe more later)
			self.location = self.check_location() # grabs location from func (zip code str)
		else: # otherwise, user passed one as an arg
			self.location = location # use given location
		if (huntlist == None): # if no huntlist is provided (maybe allow sharing later)
			self.huntlist = self.generate_huntlist() # generates new huntlist based w loc
		else: # otherwise, one was already given (sharing?)
			self.huntlist = huntlist # use given huntlist
		if (hunt_name == None): # if no custom huntname provided
			self.hunt_name = "{} Hunt".format(self.get_location()) # name using zip
		else: # otherwise, use custom name
			self.hunt_name = hunt_name # given as arg
	def check_location(self):
		'''collects location: either from OS, using plyer, or user prompt'''
		cur_location = "07940" # hard-coded for now
		return cur_location
	def get_location(self):
		'''returns location field'''
		return self.location[:]
	def set_location(self, new_location):
		'''sets new location field from given arg'''
		self.location = new_location[:]
	def get_hunt_name(self):
		'''returns name of scavenger hunt'''
		return self.hunt_name[:]
	def set_hunt_name(self, new_hunt_name):
		'''sets new hunt name from given arg'''
		self.hunt_name = new_hunt_name[:]
	def get_huntlist(self):
		'''returns huntlist'''
		return self.huntlist
	def set_huntlist(self, new_huntlist):
		'''sets new huntlist from given arg'''
		self.huntlist = new_huntlist
	def mark_item(self, index):
		'''mark an item as found within the scavenger hunt'''
		self.get_huntlist().checkoff_item(index) # call child checkoff func at given index
	def generate_huntlist(self, huntlist_name = None):
		'''generates new scavenger hunt checklist of targets'''
		# might have sublists later for diff types of targets, thus keep list names
		new_target_list = self.scrape_huntlist() # call func to scrape new target items
		if (huntlist_name == None): # if no name provided, let checklist use default
			new_huntlist = Checklist()
		else: # otherwise, use provided name
			new_huntlist = Checklist(huntlist_name)
		# build new huntlist from scraped items
		for i in range(len(new_target_list)): # loop over scraped targets
			# define parts of each sublist for easy understanding
			[item_name, picture] = new_target_list[i]
			# add new item to huntlist and automatically set found to False
			new_huntlist.add_new_item(item_name, False, picture)
		return new_huntlist # return new huntlist
	def scrape_huntlist(self):
		'''builds huntlist from targets grabbed based on location, using nwf_tools'''
		scrape_results = nwft.scrape_nwf(self.get_location()) # scrape info with zip code
		return scrape_results # return list of targets (each item is [name, filename])
	def display_hunt(self):
		'''prints current scavenger hunt in readable format'''
		print("\n{}:\n".format(self.get_hunt_name())) # print hunt name
		self.get_huntlist().display_checklist() # print hunt list using checklist display