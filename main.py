import re
import argparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(
    prog='InstagramWebScrapper',
    description='Это пограмма берет данные instagram пользователя.',
    epilog='Спасибо за изпользование!'
)

parser.add_argument('nick',type=str,help="Здесь надо ввести nickname от instagram!")
args = parser.parse_args()

web = requests.get(f"https://www.instagram.com/{args.nick}/")
html = web.text

soup = BeautifulSoup(html,"html.parser")
meta_tag = soup.find("meta", attrs={"name": "description"})
content = meta_tag["content"]

followers = meta_tag["content"].split(",")[0].strip()
result_followers = [int(i) for i in followers.split() if i.isdigit()]

following = meta_tag["content"].split(",")[1].strip()
result_following = [int(i) for i in following.split() if i.isdigit()]

posts = re.search(r"Following, (.*) Posts", content)


match = re.search(r"from (.*) \(@", content)
if match:
    name = match.group(1)
else:
    match = re.search(r"\((.*?)\)", content)
    name = match.group(1)

if not name:
    match = re.search(r"\(@(.*)\)", content)
    if match:
        name = match.group(1)

inform = f'''
Followers: {followers}
Following: {following}
Posts:  {posts.group(1)}
Name: {name}
'''

print(inform)





