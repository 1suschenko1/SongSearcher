import requests
import re

def search_song_by_lyrics(lyrics):
    query = lyrics + " lyrics"
    google_url = f"https://www.google.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(google_url, headers=headers)
    if response.status_code == 200:
        html_content = response.text
        titles = re.findall(r'<h3.*?>(.*?)<\/h3>', html_content, re.DOTALL)
        if titles:
            print("Первый найденный результат:")
            clean_title = re.sub(r'<.*?>', '', titles[0])
            print(clean_title)
        else:
            print("Результаты не найдены.")
    else:
        print("Ошибка при запросе к Google:", response.status_code)

lyrics = input("Введите строчку из песни: ")
search_song_by_lyrics(lyrics)