import pandas as pd
from datetime import date
import requests
from tokenfile import *
contributors_filtered = pd.read_csv("Complete_steps/contributorsfiltered.csv")
#  The following tool takes a csv file of repository names and uses the Github API to check
# for the date of the last commit
# if you want to input  a list just change the iteration , in the for loop
# i is the name of the repo .
lastContributionDays = 365
repositories = []
for i in contributors_filtered['Repository Name']:
    url = "https://api.github.com/repos/" + i + "/commits"
    res = requests.get(url, headers={"Authorization": 'token ' + tokenkey})
    jsonres = res.json()
    pulleddate = jsonres[0]['commit']['author']['date']
    year = int(pulleddate[0:4])
    month = int(pulleddate[5:7])
    day = int(pulleddate[8:10])
    testdate = date(year, month, day)
    currentdate = date(2022, 4, 25)
    delta = currentdate - testdate
    if delta.days < lastContributionDays :
        repositories.append(i)
    if delta.days<0:
        print("problem")



df = pd.DataFrame(repositories ,columns=['Repository Name'])
df.set_index('Repository Name',inplace=True)
df.to_csv('Complete_steps/commitdatefiltered.csv')