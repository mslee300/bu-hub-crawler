import requests
URL = "https://www.bu.edu/hub/hub-courses/philosophical-aesthetic-and-historical-interpretation/"
r = requests.get(URL)
print(r.content)
