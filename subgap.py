#!/usr/bin/python
#
# <bitbar.title>Pewdiepie vs T-series sub gap</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Tok1</bitbar.author>
# <bitbar.author.github>tokfrans03</bitbar.author.github>
# <bitbar.desc>Displays the sub gap between Pewdiepie and T-series. Set your youtube api key in the script. You can also change the channel ids to check on other sub gaps, just make shure the bigger one is first</bitbar.desc>
# <bitbar.image>https://github.com/garythung/bitbar-age-ticker/blob/master/bitbar-age-ticker.gif?raw=true</bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.abouturl>https://github.com/garythung/bitbar-age-ticker</bitbar.abouturl>

import requests
import json
import signal
import os
import time

pewds="UC-lHJZR3Gqxm24_Vd_AJ5Yw"
tseries="UCq-Fj5jknLsUf-MWSy4_brA"
apiKey = "YOUR_API_KEY"

pewdsdata = requests.get('https://www.googleapis.com/youtube/v3/channels?part=statistics&id=' + pewds + '&key=' + apiKey)
tseriesdata = requests.get('https://www.googleapis.com/youtube/v3/channels?part=statistics&id=' + tseries + '&key=' + apiKey)
pewdssubs = json.loads(pewdsdata.text)["items"][0]["statistics"]["subscriberCount"]
tseriessubs = json.loads(tseriesdata.text)["items"][0]["statistics"]["subscriberCount"]

dif = int(pewdssubs) - int(tseriessubs)

print("{:,d}".format(int(dif)))
