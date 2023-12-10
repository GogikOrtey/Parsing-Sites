from requests_html import HTMLSession

# ---------------------------------------------------------------------- #
#     Тестовое подключение к сайту, и сохранение его в текстовый файл    #
# ---------------------------------------------------------------------- #

# Создаем сессию
session = HTMLSession()

# Отправляем GET-запрос к веб-странице
# response = session.get('https://vgtimes.ru/news/')
response = session.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')

# Получаем HTML-код страницы
html_content = response.text

# Записываем HTML-код в файл
with open('output.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

