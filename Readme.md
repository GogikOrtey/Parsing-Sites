## Описание репозитория:

Все файлы с кодом лежат в папке *Programs*

#### Основными файлами с кодом являются:

**08** - Реализация консольного интерфейса, который создаёт финальный Excel файл, с результатами

**06** - Скрипт, с реализацией парсинга всех страниц, по жанрам

---

#### Описание других скриптов:

**03** - Получение всех жанров, с главной страницы, и ссылок на них

**04** - Обработка этого датафрейма, с жанрами и ссылками на них

**02** - Получение всех книг, конкретного жанра

**01** - Тестовый парсинг страницы

*Остальные скрипты - тестовые*

---

Также, в начале каждого файла с кодом, написано, что он делает, и для чего нужен.

---

#### Описание текстовых файлов:

`output.csv` - Датафрейм всех книг с одного жанра

`output_genres.csv` и `output_genres_2.csv` - Все жанры, и ссылки на них. Во втором файле ссылки полные

`mainDF.csv` - Датафрейм со всеми книгами, из всех жанров

`MainOutputResults.xlsx` - Выходной Excel файл. Генерируется, после завершения **08** скрипта - терминала
