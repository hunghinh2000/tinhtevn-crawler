import urllib.request
import time
import socket

def download_image(img_url, img_name, img_folder_path):
	"""Download an image from a given image url
    
    Inputs:
        imgurl: str
				Image url
		img_name: str
				Image name
		img_folder_path: str
				The path of output image folder
    Return:
        If the image is downloaded successfully, return True.
		Else return False.
    Author:
    Last modified: 22:48_02/22/20
    """
	socket.setdefaulttimeout(30)
	
	img_fullpath = img_folder_path + img_name
	try:
		time.sleep(5)
		urllib.request.urlretrieve(img_url, img_fullpath)
		return True
	except urllib.error.URLError as e:
		print(e)
		return False