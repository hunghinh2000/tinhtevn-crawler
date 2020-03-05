import logging
from configparser import SafeConfigParser

def load_config():
	"""Load all parameters for project
	
	Input:
		None
	Return:
		json_output_path: str
				Json output path
		image_output_path: str
				Folder for storing all images crawled by spider
		tinhte_category_link: str
				The start link of the category that you want to crawl
		year_limit: str
				The minimum year of a thread in category allowed spider to crawl
	Author:
	Last modified: 22:36_02/23/20
	"""

	config = SafeConfigParser()
	config.read("config/main.cfg")
	
	json_output_path = str(config.get('main', 'json_output_path'))
	image_output_path = str(config.get('main', 'image_output_path'))
	tinhte_category_link = str(config.get('main', 'tinhte_category_link'))
	year_limit = str(config.get('main', 'year_limit'))

	return json_output_path, image_output_path, tinhte_category_link, year_limit
	
