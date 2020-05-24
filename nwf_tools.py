# nwf_tools.py for backyard-hacks-2020 by max
import requests as req
from bs4 import BeautifulSoup
import re
import sys

def scrape_nwf(zip_code):
	'''scrapes targets for huntlist based on location'''
	# get html sources from nwf.org for all species
	flowers_grass_html = fetch_html(zip_code)
	trees_shrubs_html = fetch_html(zip_code, False)
	# parse the html sources for results of all species
	found_flowers_grass = parse_html(flowers_grass_html)
	found_trees_shrubs = parse_html(trees_shrubs_html)
	# store all found species in list (all grouped together for now)
	found_species = (found_flowers_grass + found_trees_shrubs)
	# return all found species as combined list
	return found_species

def fetch_html(zip_code, flowers_grass = True):
	'''takes in zip arg, gets and returns html from nwf.org using premade cookies'''
	# look for flowers and grass by default
	webpage_link = "https://www.nwf.org/NativePlantFinder/Plants/Flowers-and-Grasses"
	if (flowers_grass == False): # otherwise, get trees and shrubs
		webpage_link = "https://www.nwf.org/NativePlantFinder/Plants/Trees-and-Shrubs"
	# create cookies for request with zip
	cookies = {'npfUser':'ZipCode={}'.format(zip_code)}
	# fetch html with get request
	result = req.get(webpage_link, cookies=cookies)
	return result.text # return html from response

# ref: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class
# ref: https://stackoverflow.com/a/24982536
def parse_html(webpage):
	'''parses html for desired results, return list of targets'''
	souped_page = BeautifulSoup(webpage, "html.parser") # parse page as bs obj
	tile_section = souped_page.find("div", class_="tiles") # store tile section for further parsing
	# compile all individual tiles into list
	all_tiles = tile_section.find_all("div", class_="tileContainer")
	# make new list of only tiles with images (maybe add scraping from elsewhere later)
	all_valid_tiles = []
	# identify regex pattern for verifying valid image url
	image_pattern = ".{46}imageRender\\.aspx\\?filename\\=.{5,}(?=')"
	# loop over all tiles to sort out invalid ones (no image)
	for i in range(len(all_tiles)):
		# get just style area for use with regex--should contain just background img url
		style_area = all_tiles[i].find("a", class_="tileImage2").get('style')
		# check if style area contains valid image url (does regex return a match?)
		if (re.search(image_pattern, style_area) == None):
			continue # if it doesn't have one, skip to next iteration
		# collect common name for this tile
		common_name = all_tiles[i].find("span", class_="commonName").get_text()
		# make sure it's not a list of similar plants--we can't handle those yet
		if ("," in common_name): # is there a comma in the common name?
			continue # if so, skip to next iteration
		# collect genera name, family names for this tile (now that we've checked)
		genera_name = all_tiles[i].find("span", class_="generaName").get_text()
		family_name = all_tiles[i].find("span", class_="familyName").get_text()
		# collect image url using regex pattern and style area from earlier
		image_url = re.search(image_pattern, style_area).group(0)
		# download image and take note of filepath
		image_path = download_image(image_url)
		# build sublist to store parsed information
		tile_info = [common_name, image_path]
		# extra information for later usage, if time to add wikipedia lookups
		extra_tile_info = [genera_name, family_name]
		# add relevant info (just main stuff for now) to master list of valid species
		all_valid_tiles.append(tile_info)
	# return info sublists for all valid species
	return all_valid_tiles

# ref: https://www.tutorialspoint.com/downloading-files-from-web-using-python
def download_image(image_url):
	'''given image url, downloads image to local directory for offline use'''
	# define regex pattern for finding filename
	filename_pattern = "(?<=filename\\=).{5,}"
	# find the filename in the url
	filename = re.search(filename_pattern, image_url).group(0)
	# fetch the image at given url
	fetched_image = req.get(image_url, allow_redirects=True)
	# specify relative local save path (removed for simplicity, prob diff in mobile os)
	# save_path = "./"
	# save the image locally, using filename found earlier (wb = binary mode; no changes)
	open(filename, 'wb').write(fetched_image.content)
	return filename # return filename for later access

def main(argv):
	if (len(argv) != 2): # if not two args
		# tell user how to use properly
		print("\n\tError − Incorrect Syntax\n\n\tUse 'python nwf_tools.py [zip code]'\n")
		sys.exit() # exit program
	print( scrape_nwf(argv[1]) ) # print found species

if __name__ == '__main__':
	main(sys.argv)