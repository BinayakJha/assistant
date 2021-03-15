import http.client as ht

conn = ht.HTTPSConnection("api.msg91.com")

payload = '''{
  "sender": "BJJHA1",
  "route":"4",
  "country":"977",
  "sms": [
    {
 	"message":"Just a test message",
	"to":[
		"9851222218"
    ]
    }
  ]
}'''
headers = {
    'authkey': "356263AZyTo8YwGlG6048ca98P1",
    'content-type': "application/json"
    }

conn.request("POST", "/api/v2/sendsms?campaign=&response=&afterminutes=&schtime=&unicode=&flash=&message=&encrypt=&authkey=&mobiles=&route=&sender=&country=977", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))