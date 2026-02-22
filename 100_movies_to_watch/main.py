import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.select(selector="div > h3")
all_movies = [title.getText() for title in titles]
all_movies.reverse()

with open("movies.txt", 'w') as file:
    for movie in all_movies:
        file.write(f"{movie}\n")
        print(movie)