import requests

print(requests.__version__)
print(requests.get("http://www.google.com/"))
print(requests.get("https://raw.githubusercontent.com/daisylau1118/CMPUT404-Lab1/main/lab1.py").text)