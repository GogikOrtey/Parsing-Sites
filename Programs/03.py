from requests_html import HTMLSession
import pandas as pd

# ---------------------------------------------- #
#    Получение всех жанров, и ссылок на них      #
# ---------------------------------------------- #

# Создаем сессию
session = HTMLSession()

# Отправляем GET-запрос к веб-странице
response = session.get('http://books.toscrape.com/index.html ')

# # Записываем HTML-код в файл
# with open('output.html', 'w', encoding='utf-8') as file:
#     file.write(response)

# Получаем список книг
books = response.html.find('ol.row li')




# # Создаем словарь для хранения информации о книгах
# books_info = {'Название': [], 'Рейтинг': [], 'Ссылка': [], 'Цена': []}

# # Словарь для преобразования рейтинга из строки в число
# rating_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

# for book in books:
#     # Получаем название книги
#     title = book.find('article h3 a', first=True).text
#     books_info['Название'].append(title)

#     # Получаем рейтинг книги
#     rating_class = book.find('article p', first=True).attrs['class']
#     rating = rating_dict[rating_class[1]] if len(rating_class) > 1 else None
#     books_info['Рейтинг'].append(rating)

#     # Получаем ссылку на книгу
#     link = book.find('article h3 a', first=True).attrs['href']
#     books_info['Ссылка'].append(link)

#     # Получаем цену книги
#     price = book.find('article div.product_price p.price_color', first=True).text
#     books_info['Цена'].append(price)

# # Создаем DataFrame
# df = pd.DataFrame(books_info)

# # Удаляем символ £ из столбца "Цена"
# df['Цена'] = df['Цена'].str.replace('£', '')

# # Заменяем ссылки с урезанных на полные
# df['Ссылка'] = df['Ссылка'].str.replace('../../../', 'http://books.toscrape.com/catalogue/')

# # Выводим DataFrame
# print(df)

# # Сохраняю датафрейм в файл:
# df.to_csv('output.csv', index=False, encoding='utf-8')

