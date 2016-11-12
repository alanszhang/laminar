import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{1701e248fe00499e8e8b941a78a5c076}',
}


def main(input):
	params = urllib.parse.urlencode({input})
	

	try:
    	conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
   	 	conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, "{body}", headers)
    	response = conn.getresponse()
    	data = response.read()
    	return data;
    	conn.close()
	except Exception as e:
    	print("[Errno {0}] {1}".format(e.errno, e.strerror))

