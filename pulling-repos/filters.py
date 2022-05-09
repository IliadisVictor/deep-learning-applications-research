from bs4 import BeautifulSoup
import requests

# Input the full name of the repository with the slash and the amount of contributors
# you want to see if it exceeds , True if it does False if it doesn't None if something went wrong
# with the scraping
# WARNING , these tools do not use the official API that is safer but much slower.
def contributors_check(repo_name,contributors_threshold):
    url = 'https://github.com/'+repo_name
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    cells=soup.find_all('a', class_="Link--primary no-underline")
    for a in cells:
        if 'Contributors' in a.get_text():
            contributors_amount = a.get_text().replace('Contributors','').strip()
            if int(contributors_amount)>contributors_threshold:
                return True
            else:
                return False
    return None

def above_stars_threshold(repo_name,stars_barrier):
    url = 'https://github.com/'+repo_name
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    cells=soup.find_all('a', class_="Link--muted")
    # looking for the link that corresponds to the stars by searching for the string star in it
    for i in range(0,len(cells)):
        if 'star' in cells[i].get_text():
            break
    # here we clean the string to get only the numeral so we can convert to an int
    stars = cells[i].get_text().replace('stars', '').strip()
    if 'star' in stars:
        stars = cells[i].get_text().replace('star', '').strip()
    #     K means a thousand so it will surely be bigger than the 3 numeral threshold we give as input
    if 'k' in stars:
        return True
    else:
        if int(stars)>stars_barrier:
            return True
        else:
            return False
    return None