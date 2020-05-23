# Checklist for backyard-hacks-2020 by max

class Checklist(Target):
	'''list of target objects to be item_list'''
	def __init__(self, label = "Current List", item_list = []):
		self.label = label
		self.item_list = item_list
	def get_label(self):
		'''returns label'''
		return self.label[:]
	def set_label(self, new_label):
		'''sets label'''
		self.label = new_label[:]
	def get_item_list(self):
		'''returns current item_list'''
		return self.item_list[:]
	def set_item_list(self, new_item_list):
		'''sets item_list status'''
		self.item_list = new_item_list
	def get_item(self, index):
		'''gets item at point in checklist'''
		return Target.get_target(self.get_item_list()[index]) # indexes current list
	def set_item(self, item, index):
		'''sets item at point in checklist'''
		cur_list = Target.get_target(self.get_item_list()) # gets list as it stands now
		cur_list.insert(index, item) # inserts item at given point in list
		self.set_item_list(cur_list) # set class field to modified list 
	def display_checklist(self):
		'''prints checklist items in nice format'''
		target_string = "\t{}:\n".format(self.get_label())
		for i in range(len(self.get_item_list())): # loop over items in checklist
			cur_item = self.get_item(i) # get item at current index in loop
			# add string version of item to string that will be printed
			target_string += "\tList Item #{}:\n{}\n".format(cur_item.target_info())
		print(target_string)