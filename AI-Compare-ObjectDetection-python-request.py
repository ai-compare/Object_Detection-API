import requests

# You can find the documentation here : https://documenter.getpostman.com/view/10011301/SzmiVFqh?version=latest#6571813e-96e4-4e4a-8603-41cd739bdd3b

#Enter your API Token
headers = {  'Authorization': 'Bearer your API Key'} #You can get your free API token here https://www.ai-compare.com/accounts/login/?next=/my_apis

# Select API
url = 'https://www.ai-compare.com/v1/pretrained/vision/object_detection'

# Select providers, and objects to detect
payload = {'providers': '[\'google_cloud\', \'cognitives_service\', \'aws\', \'ibm\']','objects_to_find': ''}

# Select file to test
files = [  ('files', open('Picture/example.jpg','rb'))]

# Request to AI COMPARE
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))
