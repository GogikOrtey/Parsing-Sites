from requests_html import HTMLSession
import pandas as pd
import time

# ---------------------------------------------- #
#       Обработка полученного датафрейма         #
# ---------------------------------------------- #


# Загружамем все книги
df_books = pd.read_csv('mainDF.csv')

# Загружамем все жанры
df_genres = pd.read_csv('output_genres_2.csv')

# Консоль:

print("Добро пожаловать в консоль!")
print("-----")
print("Для начала, выберете желаемый жанр (только один), введя его номер.")

while(True):
    print("Вот список всех доступных жанров:")

    print("Номер : Название жанра")
    print("")

    for ind, row in df_genres.iterrows():
        print(str(ind+1) + " : " + row["Название"])

    print("")
    num_genre = input("Введите номер жанра: ")

    try:
        num_genre = int(num_genre)
    except ValueError:
        print("Вы ввели не целое число, попробуйте ещё раз!")
        print("Выберете желаемый жанр (только один), введя его номер.")
        continue

    if(num_genre < 1 or num_genre > 50):
        print("Вы ввели неправильное число. Пожалуйста, введите номер жанра, от 1 до 50")
    else:
        break


print("OK")






# # Создаём список всех книг
# mainDF = pd.DataFrame(columns=['Название', 'Рейтинг', 'Ссылка', 'Цена', 'Жанр'])

# # Выводим их
# # print(df_genre)

# int_count = 0

# for index, row in df_genre.iterrows():
#     name_genre = row["Название"]
#     link = row["Ссылка"]
#     print(name_genre + ", " + link)
#     if(True): #(int_count < 2): # Ограничитель, для тестирования
#         getAllBooksForOnceGenre(name_genre, link)
#         time.sleep(2) # Задержка в 2 секунды
#     else:
#         break
#     int_count += 1

# # getAllBooksForOnceGenre("Travel", "http://books.toscrape.com/catalogue/category/books/travel_2/index.html")

# # Выводим все книги
# print(mainDF)

# # print(f"Количество книг: {mainDF.shape[0]}")

# mainDF.to_csv('mainDF.csv', index=False, encoding='utf-8')