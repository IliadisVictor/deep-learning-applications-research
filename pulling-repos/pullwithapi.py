import requests
import time
import pandas as pd
from tokenfile import *
calls=[]
page=1
# Using the GithubAPI we search in configuration package management code files
# to get repositories dependent on a desired library , and then exports it on a csv
# WARNING , duplicate occur filter before using.
libraryname='BigDL'
filetosearch='setup.py'
while True:
  time.sleep(10)
  url = "https://api.github.com/search/code?q="+libraryname+"+filename:"+filetosearch+"&page="+str(page)
  res = requests.get(url, headers={"Authorization": 'token ' + tokenkey})
  jsonres = res.json()
  if 'items' in jsonres:
      print("request accepted",page)
      page = page + 1
      calls.append(jsonres)
      if not jsonres['items']:
          print(jsonres['items'])
          break
  else:
      print("request denied")
      time.sleep(20)
      continue

count = 0
repos_name=[]
for data in calls:
    for item in data['items']:
        count =count+1
        repository = item['repository']
        repository_name = repository['full_name']
        repos_name.append(repository_name)
        print(repository_name)
df = pd.DataFrame(libraryname,columns=['Repository Name'])
df.set_index('Repository Name',inplace=True)
df.to_csv('setup.csv')
print(count,page-1)
# Closing file
