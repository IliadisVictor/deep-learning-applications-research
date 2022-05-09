import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# This tool takes the list of dependent projects for a github project
# and scrapes them . I have also implemented a star filtering system
# input the url of the dependents graph for the desired project and
# the minimum stars in the star_threshhold var

repos_list =[]
star_threshhold = 100
url = "https://github.com/apache/incubator-mxnet/network/dependents?package_id=UGFja2FnZS01MjQxOTM3Ng%3D%3D"
# There is a small issue , we cannot differentiate the previous and next buttons after the first page
#  they are identical  so we must put a counter
button_counter=0
total_repositories = 0
# current_Element = div_box[0]

while len(repos_list)<100 and total_repositories<2800:
    response = requests.get(url)
    time.sleep(0.5)
    soup = BeautifulSoup(response.content, 'html.parser')
    time.sleep(0.5)
    div_box = soup.find_all('div', class_="Box-row d-flex flex-items-center")
    for current_Element in div_box:
        total_repositories+=1
        # get repo name and repo owner
        repo_links = current_Element.find_all('span')[0].find_all('a')
        # get complete repo
        repo_Name = repo_links[0].get_text() + '/' + repo_links[1].get_text()
        repo_Stars = current_Element.find_all('span')[1].get_text().strip()
        repo_Stars = int(repo_Stars.replace(',',''))
        if repo_Stars >=star_threshhold:
            repos_list.append(repo_Name)
    try:
        url = soup.find_all('a' , class_='btn btn-outline BtnGroup-item')[button_counter]['href']
    except IndexError:
        continue
    print(total_repositories,url)
    time.sleep(0.5)
    if button_counter ==0:
        button_counter +=1


df = pd.DataFrame(repos_list,columns=['Repository Name'])
df['Library'] = 'MXNet'
df.set_index('Repository Name',inplace=True)
print(df,len(repos_list),total_repositories)
# df.to_csv('Apache_MXNet.csv', encoding='utf-8')