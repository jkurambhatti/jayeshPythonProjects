'''
    the aim of this simple project is to download an image from the url given
    save it in the current directory
    we use the urllib.request module to carry out ther operation
'''

import random
import urllib3.request
import urllib


def download_image_from_url(url):
    name = random.randrange(0,10)       #this will specify the name of image
    fullname = str(name) + ".jpg"       #this will convert int to string and add extension to file name
    urllib.urlretrieve(url,fullname)


download_image_from_url("https://qph.ec.quoracdn.net/main-qimg-298f0a1bce6b5fbbb05d2cb5cf3a1e6d")