import requests

url = 'http://127.0.0.1:5000/b'

res = requests.post(url,files={'image_file': ('captcha.jpg', open('sample/test/0alp_15623372702032907.png', 'rb'), 'application')})
print(res.text)