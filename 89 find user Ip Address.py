import requests
api_url = 'https://api.ipify.org?format=json'
response = requests.get (api_url)
if response.status_code == 200:
   data = response.json()
   ip = data.get ('ip')
   print ('This your ip address', ip)

