# ScavengerHunt for backyard-hacks-2020 by max
import nwf_tools as nwft

class ScavengerHunt(Checklist):
	'''scavenger hunt object, for use by user/player'''
	def __init__(self, huntlist = None, hunt_name = None):
		self.location = self.check_location() # grabs location from func (zip code str)
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
	def generate_huntlist(self, huntlist_name = None):
		'''generates new scavenger hunt checklist of targets'''
		# might have sublists later for diff types of targets, thus keep list names
		new_target_list = self.scrape_huntlist() # call func to scrape new target items
		if (huntlist_name == None): # if no name provided, let checklist use default
			new_huntlist = Checklist.__init__(self, new_huntlist)
		else: # otherwise, use provided name
			new_huntlist = Checklist.__init__(self, huntlist_name, new_huntlist)
		return new_huntlist # return new huntlist
	def scrape_huntlist(self):
		'''scrapes targets for huntlist based on location'''
		html_source = self.fetch_html() # get html source from nwf.org
		return
	def fetch_html(self):
		'''get and return html from nwf.org using premade cookies'''
		# create cookies for request with zip
		cookies = {'npfUser':'ZipCode={}'.format(self.get_location())}
		# fetch html with get request
		result = req.get('https://www.nwf.org/nativePlantFinder/plants', cookies=cookies)
		return result.text # return html from response
	def parse_html(self):
		'''parses html for desired results'''
		return