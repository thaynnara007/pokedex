from google_images_download import google_images_download
from requests import exceptions
import argparse

response = google_images_download.googleimagesdownload()

ap = argparse.ArgumentParser("search for images on google by some queries")
ap.add_argument('-q','--query', nargs='+', help='Search query', required=True)
ap.add_argument('-l', '--limit', help="limit of images per query", required=True)
args = vars(ap.parse_args())

search_queries = args['query']
limit = args['limit']

EXCEPTIONS = set([IOError, FileNotFoundError, exceptions.RequestException,
exceptions.HTTPError, exceptions.ConnectionError, exceptions.Timeout])

def download_images(query, limit):

  arguments = {
    'keywords': query,
    'format': 'jpg',
    'limit': limit,
    'print_urls': True,
    'size': 'medium',
    'aspect_ratio': 'panoramic'
  }

  try: response.download(arguments)
  except Exception as exception:

    arguments = {"keywords": query, 
              "format": "jpg", 
              "limit":limit, 
              "print_urls":True,  
              "size": "medium"} 
    
    try: response.download(arguments)
    except:
      print('[ERROR] {}'.format(exception))
      pass


for query in search_queries:
  download_images(query, limit)
  print()
  

