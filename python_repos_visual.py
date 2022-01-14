import requests

from plotly.graph_objs import Bar
from plotly import offline

#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print (f"Status Code: {r.status_code}")

#Store the API response in a variable and process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [],[]
for repo_dict in repo_dicts:
	repo_names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

#Make visualization.
data =[{
	'type':'bar',
	'x':repo_names,
	'y': stars,
	}]

my_layout = {
	'title': 'Most-Starred Python Projects on GitHub',
	'xaxis': {'title':'Repository'},
	'yaxis': {'title':'Stars'},
	}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename ='python_repos.html')

#Explore information about the repositories.
#repo_dicts = response_dict['items']
#print (f"Repositories returned: {len(repo_dicts)}")

"""
print ("\nSelected information about each repository:")
for repo_dict in repo_dicts:
	print (f"\nName: {repo_dict['name']}")
	print (f"Owner: {repo_dict['owner']['login']}")
	print (f"Stars: {repo_dict['stargazers_count']}")
	print (f"Repository: {repo_dict['html_url']}")
	print (f"Description: {repo_dict['description']}")
"""
#Examine the first repository.
#repo_dict=repo_dicts[0]



#print(f"\nKeys:{len(repo_dict)}")
#for key in sorted(repo_dict.keys()):
	#print(key)


#print("\nSelected information about the first repository:")
#print (f"Name: {repo_dict['name']}")
#print (f"Owner: {repo_dict['owner']['login']}")
#print (f"Stars: {repo_dict['stargazers_count']}")
#print (f"Repository: {repo_dict['html_url']}")
#print (f"Created: {repo_dict['created_at']}")
#print (f"Updated: {repo_dict['updated_at']}")
#print (f"Description: {repo_dict['description']}")


#Process the results.
#print (response_dict.keys())
#print (f"Total repositories: {response_dict['total_count']}")
