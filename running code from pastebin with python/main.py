import requests as r
import sys
import os

uri = sys.argv[1]
resp = r.get(uri).text

os.system(resp)
