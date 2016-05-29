import json
import urllib.request

req = urllib.request.Request('https://il5t4m4jud.execute-api.us-west-2.amazonaws.com/prod/TS-PiConfiguration')

with urllib.request.urlopen(req) as response:
	result = json.loads(response.read().decode('utf-8'))

print (result['uri'])

url=result['uri']
	
name = url.split('/')[-1]
f = urllib.request.urlopen(url)
data = f.read()
with open(name, "wb") as code:
	code.write(data)

print ("done")

