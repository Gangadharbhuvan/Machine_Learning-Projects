#import modules
import pandas as pd
import urllib.request

def url_to_jpg(i, url, file_path):
	'''
		args:
			-- i : number of images.
			-- url : a url address of a given image.
			-- file_path : where to save the final image.
	'''

	filename = "image-{}.jpg".format(i)
	full_path = '{}{}'.format(file_path, filename)
	urllib.request.urlretrieve(url, full_path)

	print('{} saved.'.format(filename))

	return None


#Set Constants
FILENAME = 'Book1.csv'   #name of csv file
FILE_PATH = 'Img_folder_(downloaded)/'

#Read list of url's as Pandas DataFrame
urls = pd.read_csv(FILENAME)

#Save Images to Directory by iterating through the list
for i, url in enumerate(urls.values):
	url_to_jpg(i, url[0], FILE_PATH)