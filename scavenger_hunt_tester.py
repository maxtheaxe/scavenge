# scavenger_hunt_tester.py for backyard-hacks-2020 by max
from ScavengerHunt import ScavengerHunt
import sys

def main(argv):
	if (len(argv) != 2): # if not two args
		# tell user how to use properly
		print("\n\tError − Incorrect Syntax\n\n\tUse 'python",
			" scavenger_hunt_tester.py [zip code]'\n")
		sys.exit() # exit program
	# build hunt using zip code from cli
	local_hunt = ScavengerHunt(huntlist = None, hunt_name = None, location = argv[1])
	# display the hunt
	local_hunt.display_hunt()
	# try "finding" stuff in the hunt
	local_hunt.mark_item(2)
	# display the hunt again to make sure it updated
	local_hunt.display_hunt()

if __name__ == '__main__':
	main(sys.argv)