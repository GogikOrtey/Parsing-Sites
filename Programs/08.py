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
time.sleep(2)

# Фильтр по жанру
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

print("")
print("Минимальная цена книги = " + str(df_books['Цена'].min()))
print("Максимальная цена книги = "+ str(df_books['Цена'].max()))
print("")

# Фильтр по цене
while(True):
    print("Введите желаемую цену (мы сами подберём нужные критерии для выбора книг, по их стоимости):")
    price = input()
    # print("Введите максимальную цену:")
    # price_max = input()

    try:
        price = float(price)
        # price_max = float(price_max)
    except ValueError:
        print("Вы ввели неправильное число, попробуйте ещё раз!")
        continue

    if(price < 0 or price < df_books['Цена'].min() or price > df_books['Цена'].max()):
        print("Вы ввели неправильное число. Пожалуйста, введите корректные значения для цены.")
    else:
        price_min = price - 7
        price_max = price + 7
        if(price_min < df_books['Цена'].min()): price_min = df_books['Цена'].min()
        if(price_max > df_books['Цена'].max()): price_max = df_books['Цена'].max()
        break

print("")
#print(f"{price_min}, {price_max}")

# Фильтр по рейтингу
while(True):
    print("Введите минимальный рейтинг [от 1 до 5]:")
    rating_min = input()
    print("Введите максимальный рейтинг [от 1 до 5]:")
    rating_max = input()

    try:
        rating_min = int(rating_min)
        rating_max = int(rating_max)
    except ValueError:
        print("Вы ввели неправильное число, попробуйте ещё раз!")
        continue

    if(rating_min > rating_max):
        print("")
        print("Минимальный рейтинг больше максимального! Так нельзя! Попробуйте ещё раз")
        continue

    if(rating_min <= 0 or rating_max > 5):
        print("Вы ввели неправильное число. Пожалуйста, введите корректные значения для рейтинга.")
    else:
        break

print("")

# Применяем фильтры
df_filtered = df_books[(df_books['Цена'] >= price_min) & (df_books['Цена'] <= price_max) & 
                       (df_books['Рейтинг'] >= rating_min) & (df_books['Рейтинг'] <= rating_max)]
df_filtered = df_filtered.reset_index(drop=True)

print("Вот книги, которые соответствуют вашим критериям:")
print(df_filtered)

df_filtered.to_excel("MainOutputResults.xlsx", index=False)
print("")
print("Эти результаты сохранены в Excel файл, с названием 'MainOutputResults.xlsx'")
print("")