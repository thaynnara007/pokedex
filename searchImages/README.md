# Pokedex

- This package has some scripts that can be used for collecting images for the dataset.
- search_on_google.py is a script that uses a google images API, which is a free tool
- search_bing_api.py is a cript that uses [Bing Image Search API](https://azure.microsoft.com/en-us/try/cognitive-services/?api=bing-image-search-api) from Microsoft Azure, which is free just for the fisrt seven days.
---

## Usage

> search_on_google.py
```shell
$ python3 search_on_google.py  --query "bulbasaur" "bulbasaur fanart" --limit 100
```

> search_bing_api.py
```shell
$ python3 search_bing_api.py --query "bulbasaur" --output dataset/bulbasaur --limit 300
```

