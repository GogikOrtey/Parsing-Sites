from requests_html import HTMLSession
import pandas as pd

# ---------------------------------------------- #
#              Работа с датафреймом              #
# ---------------------------------------------- #

# # Создаем сессию
# session = HTMLSession()

# # Отправляем GET-запрос к веб-странице
# response = session.get('http://books.toscrape.com/index.html')

# # # Записываем HTML-код в файл
# # with open('output.html', 'w', encoding='utf-8') as file:
# #     file.write(response)

# # Получаем список книг
# genres = response.html.find('div.side_categories ul li')

# genres_info = {'Название': [], 'Ссылка': []}

# for genre in genres:
#     # Получаем название жанра
#     title = genre.find('a', first=True).text
#     genres_info['Название'].append(title)

#     # Получаем название жанра
#     link = genre.find('a', first=True).attrs['href']
#     genres_info['Ссылка'].append(link)

df = pd.read_csv('output_genres.csv')

# Выводим DataFrame
print(df)

df["Ссылка"] = "http://books.toscrape.com/" + df["Ссылка"]

print(df)

# Сохраняю датафрейм в файл:
df.to_csv('output_genres_2.csv', index=False, encoding='utf-8')
