import requests
res = requests.get('https://allot.com/ass')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))