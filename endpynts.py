import os
import argparse
import requests

def getHTML(filenames):


def main():
	parser = argparse.ArgumentParser(description='Find broken links with endpynts. Pass a top level directory to endpynts and the tool will return a list of broken links in your HTML.')
	parser.add_argument('dir', metavar='dir', default=".", help='String for top level directory. Must be a valid system path.')
	args = vars(parser.parse_args())

	if not os.path.isdir(full_path):
		print "Argument not a directory or path does not exist. Exiting"
	else:
		for root, dirs, files in os.walk(full_path):
			

if __name__ == "__main__":
	main()