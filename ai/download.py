from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os,time,sys
from pprint import pprint

key = "e9ce5667deff3be78508323090ca2c85"
secret = "4e84ad06262167d5"
wait_time = 1

file_name = sys.argv[1]
savedir = "./" + file_name

flickr = FlickrAPI(key,secret,format="parsed-json")
result = flickr.photos.search(
    text = file_name,
    per_page = 400,
    media = "photos",
    sort = "relevance",
    safe_search = 1,
    extras = "url_q,licence"
)

photos = result["photos"]
#pprint(photos)
for i,photo in enumerate(photos["photo"]):
    url_q = photo["url_q"]
    filepath = savedir + "/" + photo["id"] + ".jpg"
    if os.path.exists(filepath): continue
    urlretrieve(url_q,filepath)
    time.sleep(1)
