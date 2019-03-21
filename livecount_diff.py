import json
import urllib
import time
key ="AIzaSyDac3-CZQoFj8gd6cp9DBz6-HOGf2dU7aY"

while True:
        tseries_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=Tseries&key=" + key
        pew_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=PewDiePie&key=" + key
    
        tseries_data = urllib.urlopen(tseries_url).read()
        pew_data = urllib.urlopen(pew_url).read()

        tseries_subs = json.loads(tseries_data)["items"][0]["statistics"]["subscriberCount"]
        pew_subs = json.loads(pew_data)["items"][0]["statistics"]["subscriberCount"]

        print ("Tseries - " + tseries_subs)
        print ("PewDiePie- " + pew_subs)

        difference = int(tseries_subs) - int(pew_subs)
        print (" The total Difference subscribers = " + str(difference) + "\n")

        time.sleep(1)


