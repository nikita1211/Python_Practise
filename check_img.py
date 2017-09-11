import urllib
import os
from mimetypes import guess_extension

def check_img (str):
	source = urllib.urlopen(url)
	extension = guess_extension(source.info()['Content-Type'])
	#print extension
	if extension == ".png" or ".jpg" or ".svg":
		print("an image")
		string1 = "file03"
		string2 = string1+extension
		resource = urllib.urlopen(url)
		output = open(string2,"wb")
		output.write(resource.read())
		output.close()

url="https://dgplug.org/assets/img/header.png"
check_img(url)
