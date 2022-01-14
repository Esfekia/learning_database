import requests

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print (f"Status Code: {r.status_code}")

#Store the API response in a variable.
response_dict = r.json()
print (f"Total repositories: {response_dict['total_count']}")

#Examine the first repository.
repo_dicts = response_dict['items']
print (f"Repositories returned: {len(repo_dicts)}")

#Examine the first repository.
repo_dict=repo_dicts[0]
print(f"\nKeys:{len(repo_dict)}")
for key in sorted(repo_dict.keys()):
	print(key)




#Process the results.
#print (response_dict.keys())