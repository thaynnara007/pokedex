import argparse, os
import requests, cv2
from requests import exceptions

ap = argparse.ArgumentParser("Search images to build a dataset of pokemons")
ap.add_argument('-q','--query', required=True, help="Search query to search Bing Image API for")
ap.add_argument('-o', '--output', required=True, help='path to output directory images')
ap.add_argument('-l', '--limit', required=True, help="limit of images per query")
args = vars(ap.parse_args())

API_KEY = os.environ.get("BING_API_KEY")
MAX_RESULTS = args['limit']
GROUP_SIZE = 50
URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

EXCEPTIONS = set([IOError, FileNotFoundError, exceptions.RequestException,
exceptions.HTTPError, exceptions.ConnectionError, exceptions.Timeout])

'''
store the search term in a convenience variable then set the
headers and search parameters
'''
term = args["query"]
headers = {"Ocp-Apim-Subscription-Key" : API_KEY}
params = {'q':term, 'offset':0, 'count':GROUP_SIZE }

# Searching
print("[INFO] searching Bing API for '{}'".format(term))
search = requests.get(URL, headers=headers, params=params)
search.raise_for_status()

# grab the results from the search
results = search.json()
estimated_number_results = min(results["totalEstimatedMatches"], MAX_RESULTS)
print ("[INFO] {} total results for '{}'".format(estimated_number_results, term))

# a counter of the images downloaded 
total = 0

# loop over the estimated number of results in `GROUP_SIZE` groups
for offset in range(0, estimated_number_results, GROUP_SIZE):
  '''
  update the search parameters using the current offset, then
	make the request to fetch the results
  '''
  print ("[INFO] making request for group {}-{} of {}...".format(offset,
  offset + GROUP_SIZE, estimated_number_results))
  params['offset'] = offset

  search = requests.get(URL, headers=headers, params=params)
  search.raise_for_status()
  results = search.json()

  print ("[INFO] saving images for group {}-{} of {}...".format(offset,
  offset + GROUP_SIZE, estimated_number_results))

  for value in results["value"]:
    # try to download the image
    try:
      # make a request to download the image
      print ('[INFO] fetching: {}'.format(value["contentUrl"]))
      request = requests.get(value["contentUrl"], timeout=30)

      ext = value["contentUrl"][(value["contentUrl"].rfind(".")):]
      output_path = os.path.sep.join([args["output"], "{}{}".format(
        str(total).zfill(8), ext)])

      file = open(output_path, "wb")
      file.write(request.content)
      file.close()

    except Exception as exception:
      if (type(exception) in EXCEPTIONS):
        print ("[INFO] skipping: {}".format(value["contentUrl"]))
        print ("[ERROR] {}".format(exception))
        continue
    
    image = cv2.imread(output_path)
    if (image is None):
      print ("[INFO] deleting: {}".format(output_path))
      if (os.path.exists(output_path)):
        os.remove(output_path)
      continue
    
    total += 1


