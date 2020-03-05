import scrapy
import logging
import json
import urllib.request
from src.items import TinhtecrawlerItem 
from utilities.image_downloader import download_image 
from utilities.json_writer import write_json_file

class TinhteSpider(scrapy.Spider):
	name = "tinhte"
	allowed_domains = ['tinhte.vn']
	img_count = 0
	thread_count = 0
	
	def __init__(self, category_url = None, json_output_path = None, image_output_path = None, year_limit = 2015, *args, **kwargs):
		super(TinhteSpider, self).__init__(*args, **kwargs)
		self.start_urls = [category_url]
		self.json_output_path = json_output_path
		self.image_output_path = image_output_path
		self.year_limit = year_limit
		

	def start_requests(self):
		opener = urllib.request.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		urllib.request.install_opener(opener)

		yield scrapy.Request(self.start_urls[0], callback=self.parse_thread)

	def parse_thread(self, response):
		for thread in response.css(".discussionListItems > li"):
			thread_address = thread.css(".title > a::attr(href)").get()
			if(thread_address.split('/')[0] != 'thread'):
				continue

			thread_url = "https://tinhte.vn/" + thread_address
			
			#get the year of the current thread
			datetime = thread.css(".startDate > a .DateTime::attr(data-datestring)").get()
			if(datetime == None):
				datetime = thread.css(".startDate > a .DateTime::text").get()
			year = datetime.split("/")[-1]

			if(year >= self.year_limit[2:]):
				yield scrapy.Request(thread_url, callback = self.parse_images_in_thread, 
												meta = {'datetime': datetime})

		#crawl the next page
		next_page = response.css(".PageNav > nav > a.text:last-child::attr(href)").get()
		if(next_page != None):
			next_url = "https://tinhte.vn/" + next_page
			yield scrapy.Request(next_url, callback=self.parse_thread)
			
	def parse_images_in_thread(self, response):
		data = {}
		data['title'] = response.css('div[class$="thread-title"]::text').get()
		data['threadUrl'] = response.request.url
		data['startDateTime'] = response.meta.get('datetime')
		data['comment'] = response.css('span[class$="comment"] > span::text').get()
		data['view'] = response.css('span[class$="view"] > span::text').get()

		cover_img_url = response.css('div[class$="thread-cover"]').css('img::attr(src)').get()
		if cover_img_url:
			img_name = str(self.thread_count) + "_" + str(self.img_count) +'.jpg'
			json_name = str(self.thread_count) + "_" + str(self.img_count) + '.json'
			
			if download_image(cover_img_url, img_name, self.image_output_path):
				self.img_count+=1
				data['imageUrl'] = cover_img_url
				write_json_file(json_name, self.json_output_path, data)

		for img in response.css('article[class$="content"]').css('img'):
			img_url = img.css('::attr(src)').get().split('/plain/')[-1]
			if img_url.startswith('http'):
				img_name = str(self.thread_count) + "_" + str(self.img_count) +'.jpg'
				json_name = str(self.thread_count) + "_" + str(self.img_count) + '.json'
				
				if download_image(img_url, img_name, self.image_output_path):
					self.img_count+=1
					data['imageUrl'] = img_url
					write_json_file(json_name, self.json_output_path, data)

		if self.img_count > 0:
			self.img_count = 0
			self.thread_count = self.thread_count + 1
