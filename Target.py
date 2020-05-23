# Target for backyard-hacks-2020 by max

class Target:
	'''target object to be found by user/player'''
	def __init__(self, name, found = False, picture):
		self.name = name
		self.found = found
		self.picture = picture
	def get_name(self):
		'''returns name'''
		return self.name[:]
	def set_name(self, new_name):
		'''sets name'''
		self.name = new_name[:]
	def get_found(self):
		'''returns found status'''
		return self.found
	def set_found(self, new_status):
		'''sets found status'''
		self.found = new_status
	def flip_found(self):
		'''flips the found status to the opposite of current, returns new status'''
		if self.get_found(): # if found status is already true
			self.set_found(False) # change it to false
		else: # otherwise, it was false to begin with
			self.set_found(True) # so change it to true
		return self.get_found() # return new status, in case info is desired
	def get_picture(self):
		'''returns picture'''
		return self.picture
	def set_picture(self, new_picture):
		'''sets picture'''
		self.picture = new_picture
	def get_target(self):
		'''returns self object'''
		return self
	def target_info(self):
		'''returns target info in nice format'''
		target_string = "\tTarget: {}\n\tFound: {}".format(self.get_name(),
			self.get_found())
		return target_string
	def display_target(self):
		'''returns target info in nice format'''
		print self.target_info()