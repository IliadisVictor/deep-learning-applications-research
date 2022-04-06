import requests
from bs4 import BeautifulSoup
import pandas as pd
repos_list =[]
star_threshhold = 100
links=[]
url = "https://github.com/keras-team/keras-tuner/network/dependents"
# There is a small issue , we cannot differentiate the previous and next buttons after the first page
#  they are identical  so we must put a counter
button_counter=0

# current_Element = div_box[0]

while len(repos_list)<20:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    div_box = soup.find_all('div', class_="Box-row d-flex flex-items-center")
    for current_Element in div_box:
        # get repo name and repo owner
        repo_links = current_Element.find_all('span')[0].find_all('a')
        # get complete repo
        repo_Name = repo_links[0].get_text() + '/' + repo_links[1].get_text()
        repo_Stars = current_Element.find_all('span')[1].get_text().strip()
        repo_Stars = int(repo_Stars.replace(',',''))
        if repo_Stars >=star_threshhold:
            new_repo = [repo_Name,repo_Stars]
            repos_list.append(new_repo)
    try:
        url = soup.find_all('a' , class_='btn btn-outline BtnGroup-item')[button_counter]['href']
    except IndexError:
        break
    if button_counter ==0:
        button_counter +=1


df = pd.DataFrame(repos_list,columns=['Repo Name','Stars'])
df.set_index('Repo Name',inplace=True)
n=10
if n >len(repos_list):
    n=len(repos_list)

print(df.sample(n))
df.sample(n).to_csv('keras.csv', encoding='utf-8')