# ScavengerHunt for backyard-hacks-2020 by max
import requests
from bs4 import BeautifulSoup as bs

class ScavengerHunt(Checklist):
	'''scavenger hunt object, for use by user/player'''
	def __init__(self, location = self.check_location(), age):
		self.location = location # grabs location from OS if one is not provided
		self.age = age
	def check_location():
	'''collects location from operation system, using plyer'''
		return

	def