import json
import urllib.request

def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"
 
  return cpuserial

myserial=getserial()

sourceURL = 'https://il5t4m4jud.execute-api.us-west-2.amazonaws.com/prod/TS-PiConfiguration'

authentication = {"id": myserial} 
parameters = json.dumps(authentication).encode('utf-8')
req = urllib.request.Request(sourceURL, data=parameters)
response = urllib.request.urlopen(req)
configfile = json.loads(response.read().decode('utf-8'))

print(configfile['uri'])

downloadURL = configfile['uri']

length = len(downloadURL)

print(length)

i = 0
while i<length:	
	name = downloadURL[i].split('/')[-1]
	f = urllib.request.urlopen(downloadURL[i])
	data = f.read()
	with open(name, "wb") as code:
		code.write(data)
	i+=1

print ("done")

