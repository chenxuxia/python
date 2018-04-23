import requests


files= {"files":open("git.jpeg","rb")}
response = requests.post("http://httpbin.org/post",files=files,data=data)
print(response.text)